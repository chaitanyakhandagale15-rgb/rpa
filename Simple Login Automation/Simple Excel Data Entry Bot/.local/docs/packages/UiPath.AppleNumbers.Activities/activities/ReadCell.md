# Read Cell

`UiPath.AppleNumbers.Activities.ReadCell<T>`

Reads the value of a single cell from an Apple Numbers spreadsheet. Generic over the return type `T`; the designer picks `T` from the selected `CellValueType`.

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
| `Cell` | Cell | `InArgument` | `String` | Yes | | The cell to read in A1 notation (e.g. `"A1"`, `"B3"`). |
| `TableName` | Table name | `InArgument` | `String` | No | | The name of the table on the sheet to read from (e.g. `"Table 1"`). Omit to target the default/first table. |

### Configuration

| Name | Display Name | Type | Default | Description |
|------|-------------|------|---------|-------------|
| `CellValueType` | Cell value type | [`CellValueType`](types/CellValueType.md) | `General` | The expected type of the cell value. Controls the `T` of the output — see [CellValueType](types/CellValueType.md) for the CLR type mapping. |

### Output

| Name | Display Name | Type | Description |
|------|-------------|------|-------------|
| `Result` | Result | `T` | The cell value. The runtime CLR type of `T` is determined by `CellValueType` (see Enum Reference). |

## Valid Configurations

Exactly one of `FilePath` or `ResourceFile` must be set (enforced via `[OverloadGroup]`).

- **Mode A — FilePath**: pass a local `.numbers` file path. `Sheet`, `Cell` required. `TableName`, `CellValueType` optional.
- **Mode B — ResourceFile**: pass an `ILocalResource`. Same other properties as Mode A.

See [CellValueType](types/CellValueType.md) for all values and their CLR type mapping.

## XAML Example

**Mode A — FilePath, read a string:**

```xml
<applenumbers:ReadCell x:TypeArguments="x:String" DisplayName="Read Cell"
    FilePath="[&quot;/Users/me/Documents/report.numbers&quot;]"
    Sheet="[&quot;Sheet1&quot;]" Cell="[&quot;A1&quot;]"
    CellValueType="Text"
    Result="[cellValue]" />
```

**Mode A — FilePath, specific table, read a decimal:**

```xml
<applenumbers:ReadCell x:TypeArguments="s:Decimal" DisplayName="Read Cell"
    FilePath="[&quot;/Users/me/Documents/report.numbers&quot;]"
    Sheet="[&quot;Summary&quot;]"
    TableName="[&quot;Totals&quot;]"
    Cell="[&quot;B5&quot;]"
    CellValueType="Number"
    Result="[total]" />
```

## Notes

- The designer registers a dependency on `CellValueType` and updates `T` via `IDesignerStaticTypesService` — switching the enum in the designer changes the generic type of `Result`. In hand-written XAML, `x:TypeArguments` must match the chosen `CellValueType`.
- `General` returns a CLR `object` whose concrete type depends on the cell's Numbers format — callers need to `DirectCast`/`CType` or compare with `TypeOf`.
- Apple Numbers organizes cells inside named tables on each sheet. Without `TableName`, the activity targets the default/first table of the sheet; set `TableName` to read from a specific table when the sheet contains more than one.
