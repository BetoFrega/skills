# When to Mock

Mock only system boundaries: external APIs, time/randomness, and sometimes filesystem
or databases (prefer a test database). Never mock your own modules, internal
collaborators, or dependencies you control.

## Designing for Mockability

Inject external dependencies rather than constructing them internally:

```typescript
function processPayment(order, paymentClient) {
  return paymentClient.charge(order.total);
}
```

Prefer an SDK-style operation interface (`getUser`, `getOrders`, `createOrder`) over
one generic conditional `fetch(endpoint, options)` mock. Each operation gets its
own return shape, clear test coverage, and type safety without conditional setup.
