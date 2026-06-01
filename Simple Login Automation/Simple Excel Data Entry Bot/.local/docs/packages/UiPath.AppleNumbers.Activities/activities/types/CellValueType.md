# CellValueType

**Namespace:** `UiPath.AppleNumbers.Activities.Enums`
**Kind:** `enum`

Specifies the expected data type of a cell value when reading. Used by [ReadCell](../ReadCell.md) to drive the generic result type and the coercion applied to the cell.

## Values

| Value | CLR type mapping | Description |
|-------|------------------|-------------|
| `General` | `object` | Detects the cell value type automatically based on the cell format. |
| `Text` | `string` | Reads the cell value as text (string). |
| `Number` | `decimal` | Reads the cell value as a decimal number. |
| `Integer` | `int` | Reads the cell value as an integer. |
| `Date` | `DateTime` | Reads the cell value as a date (without time component). |
| `Time` | `DateTime` | Reads the cell value as a time (without date component). |
| `DateAndTime` | `DateTime` | Reads the cell value as a date with time component. |

## Cross-References

- Used by [ReadCell](../ReadCell.md) (`CellValueType` property); the chosen value also determines the `T` of `ReadCell<T>.Result`.
