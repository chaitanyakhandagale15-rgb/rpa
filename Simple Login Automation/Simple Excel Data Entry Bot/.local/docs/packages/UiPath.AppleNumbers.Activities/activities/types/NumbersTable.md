# NumbersTable

**Namespace:** `UiPath.AppleNumbers.Activities.Models`
**Kind:** `class`

Represents a table inside an Apple Numbers sheet. Apple Numbers organizes cells into named tables within each sheet — the value of this type's `Name` property is what `TableName` arguments on other activities ([ReadCell](../ReadCell.md), [ReadRange](../ReadRange.md), [WriteCell](../WriteCell.md), [WriteRange](../WriteRange.md)) expect.

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `Name` | `String` | The name of the table (e.g. `"Table 1"`). Init-only. |

## Cross-References

- Used as the element type of `NumbersSheet.Tables` on [NumbersSheet](NumbersSheet.md).
- The `Name` value feeds the `TableName` property on [ReadCell](../ReadCell.md), [ReadRange](../ReadRange.md), [WriteCell](../WriteCell.md), and [WriteRange](../WriteRange.md).
