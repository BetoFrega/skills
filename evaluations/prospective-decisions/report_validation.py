"""Validate the complete JSON Schema subset used by frozen response formats."""


def validate_schema(value, rule, path="$"):
    supported = {"type", "properties", "required", "additionalProperties", "items", "maxItems", "enum"}
    if set(rule) - supported:
        raise ValueError(f"Unsupported response schema keyword at {path}")
    types = {"object": dict, "array": list, "string": str}
    kind = rule.get("type")
    if kind not in types or type(value) is not types[kind]:
        raise ValueError(f"Invalid report type at {path}: expected {kind}")
    if "enum" in rule and value not in rule["enum"]:
        raise ValueError(f"Invalid report value at {path}")
    if kind == "object":
        properties = rule.get("properties", {})
        if set(rule.get("required", [])) - value.keys():
            raise ValueError(f"Missing required report fields at {path}")
        if rule.get("additionalProperties") is False and value.keys() - properties.keys():
            raise ValueError(f"Unexpected report fields at {path}")
        for key, item in value.items():
            if key in properties:
                validate_schema(item, properties[key], f"{path}.{key}")
    if kind == "array":
        if "maxItems" in rule and len(value) > rule["maxItems"]:
            raise ValueError(f"Too many report items at {path}")
        for index, item in enumerate(value):
            validate_schema(item, rule["items"], f"{path}[{index}]")
