#!/usr/bin/env python3
"""Call the user back with a page in their browser and a soft, repeating sound.

    call_user.py start "message"   open the page and ring until it closes
    call_user.py stop              silence the alarm and close the page's server

The alarm stops when the user closes the page or presses Silence, when the agent
runs `stop`, or after CALL_USER_GIVE_UP seconds (1800). The first ring waits
CALL_USER_GRACE seconds (20); the gap then starts at CALL_USER_FIRST (30) and doubles
up to CALL_USER_MAX (300). CALL_USER_SOUND picks a sound file. One alarm runs per
working directory; a new start replaces it.
"""

import hashlib
import html
import http.server
import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
import webbrowser
from pathlib import Path

STATE = Path(tempfile.gettempdir()) / (
    "call-user-" + hashlib.sha1(os.getcwd().encode()).hexdigest()[:12] + ".json"
)


def seconds(name, default):
    value = os.environ.get(name, "")
    return int(value) if value.isdigit() else default


def play():
    sound = os.environ.get("CALL_USER_SOUND", "")
    player = os.environ.get("CALL_USER_PLAYER", "")
    if player:
        cmd = [player, sound]
    elif shutil.which("afplay"):
        cmd = ["afplay", "-v", "0.6", sound or "/System/Library/Sounds/Glass.aiff"]
    elif shutil.which("paplay"):
        cmd = ["paplay", sound or "/usr/share/sounds/freedesktop/stereo/message.oga"]
    elif shutil.which("canberra-gtk-play"):
        cmd = ["canberra-gtk-play", "-i", "message"]
    else:
        return
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agent needs you</title>
<style>
  body { font: 18px/1.5 system-ui, sans-serif; margin: 0; min-height: 100vh;
         display: grid; place-items: center; background: #fdf6e3; color: #222; }
  main { max-width: 36rem; padding: 2rem; }
  h1 { font-size: 1.4rem; }
  p.msg { white-space: pre-wrap; font-size: 1.2rem; }
  button { font: inherit; padding: .5rem 1.2rem; }
  @media (prefers-color-scheme: dark) { body { background: #1e1e1e; color: #eee; } }
</style></head>
<body><main>
  <h1>Your agent needs you</h1>
  <p class="msg">__MESSAGE__</p>
  <p>Close this page or press Silence to stop the alarm.</p>
  <button id="silence">Silence</button>
</main>
<script>
  new EventSource("/events");
  document.getElementById("silence").onclick = async () => {
    await fetch("/stop", { method: "POST" });
    document.querySelector("main").innerHTML = "<h1>Alarm off</h1><p>You can close this page.</p>";
    window.close();
  };
</script></body></html>"""


def run(message):
    stop = threading.Event()
    lock = threading.Lock()
    clients = {"open": 0, "seen": False, "last_close": 0.0}
    page = PAGE.replace("__MESSAGE__", html.escape(message)).encode()

    class Handler(http.server.BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_GET(self):
            if self.path == "/events":
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                with lock:
                    clients["open"] += 1
                    clients["seen"] = True
                try:
                    while not stop.is_set():
                        self.wfile.write(b": ping\n\n")
                        self.wfile.flush()
                        time.sleep(1)
                except OSError:
                    pass
                finally:
                    with lock:
                        clients["open"] -= 1
                        clients["last_close"] = time.monotonic()
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(page)

        def do_POST(self):
            if self.path == "/stop":
                stop.set()
            self.send_response(204)
            self.end_headers()

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    server.daemon_threads = True
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{server.server_address[1]}/"
    STATE.write_text(json.dumps({"pid": os.getpid(), "url": url}))
    signal.signal(signal.SIGTERM, lambda *_: stop.set())

    if not os.environ.get("CALL_USER_NO_BROWSER"):
        webbrowser.open(url)

    def page_closed():
        # A reload drops the connection for a moment, so wait before calling it closed.
        with lock:
            return (clients["seen"] and clients["open"] == 0
                    and time.monotonic() - clients["last_close"] > 3)

    def wait(duration):
        end = time.monotonic() + duration
        while time.monotonic() < end:
            if stop.wait(0.5) or page_closed():
                return False
        return True

    grace = seconds("CALL_USER_GRACE", 20)
    gap = max(seconds("CALL_USER_FIRST", 30), 1)
    cap = seconds("CALL_USER_MAX", 300)
    give_up = seconds("CALL_USER_GIVE_UP", 1800)
    elapsed = grace
    if wait(grace):
        while elapsed < give_up:
            play()
            if not wait(gap):
                break
            elapsed += gap
            gap = min(gap * 2, cap)
    stop.set()
    server.shutdown()
    try:
        if json.loads(STATE.read_text())["pid"] == os.getpid():
            STATE.unlink()
    except (OSError, ValueError, KeyError):
        pass


def silence():
    try:
        pid = json.loads(STATE.read_text())["pid"]
        os.kill(pid, signal.SIGTERM)
    except (OSError, ValueError, KeyError):
        pass
    STATE.unlink(missing_ok=True)


def main():
    action = sys.argv[1] if len(sys.argv) > 1 else ""
    if action == "start":
        if os.environ.get("CLAUDE_CODE_REMOTE") == "true":
            sys.exit("Remote session: the alarm would ring where the user can't hear it.")
        silence()
        message = " ".join(sys.argv[2:]) or "Come back to the session."
        subprocess.Popen(
            [sys.executable, __file__, "_run", message],
            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL, start_new_session=True,
        )
        for _ in range(50):
            if STATE.exists():
                print(f"Alarm on: {json.loads(STATE.read_text())['url']}")
                print("It stops when the user closes the page. Run 'stop' once they answer.")
                return
            time.sleep(0.1)
        sys.exit("The alarm did not start.")
    elif action == "stop":
        silence()
        print("Alarm off.")
    elif action == "_run":
        run(" ".join(sys.argv[2:]))
    else:
        sys.exit("usage: call_user.py start [message] | stop")


if __name__ == "__main__":
    main()
