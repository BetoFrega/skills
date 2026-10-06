# Worked example: receive signup credits

This is a fictional example, not a statement about any existing product. Assume the
product owner approved a signup grant of 20 credits on 2026-10-06, replacing an earlier
amount recorded in the destination's native history. The living record below is the
result; the introductory assumption is not part of that record.

---

# Receive signup credits

## Identity and approved intent

- Reference: CREDITS-SIGNUP; capability: listing credits.
- Decision state: approved product intent.
- Authority: example product owner; approval date: 2026-10-06.
- Effective timing: intended for initial delivery; release timing is unassigned.

## Audience and need

- Role: a seller registering an account and verifying its email.
- Segment: new sellers trying the marketplace.
- Job to be done: when joining the marketplace, obtain credits to try its listing services.
- User story: As a new seller, I want signup credits so I can try listing services before paying.

## Current rules

- A newly registered account receives 20 credits after its email is verified.
- Each account receives the signup grant once. Repeated requests or delivery attempts
  do not create additional credits.
- Accounts with unverified email remain ineligible until verification.
- Receiving credits does not itself publish a listing. Credit use follows its own contract.

## Scenarios

- Eligible account verifies its email → receives 20 credits.
- Account has not verified its email → receives no signup credits yet.
- Grant processing repeats for an already credited account → balance does not increase again.

## Value and cost

### User value

The seller can try listing services with an initial credit balance. The benefit is
expected; no user-outcome measurement is available.

### User cost

The seller completes registration and email verification. Credit sufficiency depends
on the selected listing service's price.

### Business value

The grant is intended to encourage first use by new sellers. This is a hypothesis
without a measured conversion effect.

### Business cost

The product must support grant processing, balance integrity, abuse handling, and
support. Build and operating costs have not been estimated.

## Delivery and exposure

| Dimension | State, scope, and evidence |
| --- | --- |
| Implementation | Unverified; no implementation or test evidence supplied. |
| Deployment | Unverified; no environment or provider observation supplied. |
| Authorized release | Unassigned; no audience or rollout approval supplied. |
| Observed exposure | Unverified; no audience availability check supplied. |
| Flag observations | Unknown; no control inventory or configuration supplied. |

## Open questions

- What recovery behavior applies if grant processing fails? The product owner must decide.
- Credit expiry and permitted spending need their own product contracts.

## Evidence and maintenance

- Approval metadata above represents the fictional input; there is no live approval source.
- Evidence coverage is limited to the assumed product intent. Delivery remains unqualified.
- Responsible maintainer: product documentation agent; refresh after accepted rule changes
  and supported implementation, deployment, release, or exposure observations.

## Change log

- 2026-10-06 — Increased the signup credit grant.
