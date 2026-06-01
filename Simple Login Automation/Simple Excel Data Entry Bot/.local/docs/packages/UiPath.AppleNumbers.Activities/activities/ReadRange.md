# Read Range

`UiPath.AppleNumbers.Activities.ReadRange`

Reads a range of cells from an Apple Numbers spreadsheet into a `DataTable`. When `CellRange` is omitted, reads the entire target table.

**Package:** `UiPath.AppleNumbers.Activities`
**Category:** `Integrations.AppleNumbers.Numbers`
**Platform:** macOS only

## Properties

### Input

| Name | Display Name | Kind | Type | Required | Default | Description |
|------|-------------|------|------|----------|---------|-------------|
| `FilePath` | File (local path) | `InArgument` | `String` | Yes (mode A) | | The path to the Apple Numbers file. Part of `OverloadGroup("FilePath")`. |
| `ResourceFile` | File | `InArgument` | `ILocalResource` | Yes (mode B) | | The spreadsheet file resource (resolved to a local path at runtime). Part of `OverloadGroup("ResourceFile")`. |
| `Sheet` | Sheet | `InArgument` | `String` | Yes | | The name of the sheet to read from (e.g. `"Sheet1"`). |
| `CellRange` | Cell range | `InArgument` | `String` | No | | The cell range in A1 notation (e.g. `"A1:C3"`). If empty, reads the entire target table. |
| `TableName` | Table name | `InArgument` | `String` | No | | The name of the table on the sheet to read from (e.g. `"Table 1"`). Omit to target the default/first table. |

### Configuration

| Name | Display Name | Type | Default | Description |
|------|-------------|------|---------|-------------|
| `HasHeaders` | Has headers | `InArgument<Boolean>` | `True` | If true, the first row of the range is used as column headers in the resulting `DataTable`. Otherwise columns are named `Column1`, `Column2`, etc. |

### Output

| Name | Display Name | Type | Description |
|------|-------------|------|-------------|
| `Result` | Result | `DataTable` | The data read from the range. |

## Valid Configurations

Exactly one of `FilePath` or `ResourceFile` must be set (enforced via `[OverloadGroup]`).

## XAML Example

**Mode A — FilePath, entire table with headers:**

```xml
<applenumbers:ReadRange DisplayName="Read Range"
    FilePath="[&quot;/Users/me/Documents/report.numbers&quot;]"
    Sheet="[&quot;Sheet1&quot;]"
    HasHeaders="[True]"
    Result="[dt]" />
```

**Mode B — ResourceFile, explicit range, specific table, no headers:**

```xml
<applenumbers:ReadRange DisplayName="Read Range"
    ResourceFile="[spreadsheetResource]"
    Sheet="[&quot;Data&quot;]"
    TableName="[&quot;Table 1&quot;]"
    CellRange="[&quot;A1:D20&quot;]"
    HasHeaders="[False]"
    Result="[rawData]" />
```

## Notes

- When `CellRange` is empty, the activity reads the entire target table on the named sheet. Use `TableName` to disambiguate when the sheet contains more than one table.
- `Data` from AppleScript is brought back as text; cell values surface as strings in the `DataTable` unless the AppleScript template coerces them. Callers needing typed values should use `ReadCell` with an explicit `CellValueType` per cell.
