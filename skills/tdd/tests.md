# Good and Bad Tests

## Good Tests

Integration-style tests describe what users/callers can observe through public
interfaces. Use one logical assertion; survive refactors without behavior changes.

```typescript
test("createUser makes user retrievable", async () => {
  const user = await createUser({ name: "Alice" });
  expect((await getUser(user.id)).name).toBe("Alice");
});
```

## Bad Tests

Implementation tests mock internal collaborators, inspect private methods, assert
internal call counts/order, or verify by querying storage past the interface. Their
names describe how code works; internal refactors break them.

Tautological tests repeat the implementation to derive the expectation:

```typescript
// Bad: same reduction as the implementation.
const items = [{ price: 10 }, { price: 5 }];
expect(calculateTotal(items)).toBe(items.reduce((sum, i) => sum + i.price, 0));
// Good: independent known value.
expect(calculateTotal(items)).toBe(15);
```
