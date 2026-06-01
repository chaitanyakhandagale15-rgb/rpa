# NumbersSheet

**Namespace:** `UiPath.AppleNumbers.Activities.Models`
**Kind:** `class`

Represents a sheet in an Apple Numbers document, together with the tables it contains. Returned by [GetSheets](../GetSheets.md).

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `Name` | `String` | The name of the sheet. |
| `Tables` | `List<`[`NumbersTable`](NumbersTable.md)`>` | The list of tables on this sheet. Initialized to an empty list by the constructor; never `null` from `GetSheets`. |

## Constructors

| Signature | Description |
|-----------|-------------|
| `NumbersSheet(string name)` | Creates a sheet with the given name and an empty `Tables` list. |

## Cross-References

- Returned (as `IList<NumbersSheet>`) by [GetSheets](../GetSheets.md).
- `Tables` contains [NumbersTable](NumbersTable.md) entries.
