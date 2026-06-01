# Get Sheets

`UiPath.AppleNumbers.Activities.GetSheets`

Returns the list of sheets in an Apple Numbers document, each together with the tables it contains.

**Package:** `UiPath.AppleNumbers.Activities`
**Category:** `Integrations.AppleNumbers.Numbers`
**Platform:** macOS only

## Properties

### Input

| Name | Display Name | Kind | Type | Required | Default | Description |
|------|-------------|------|------|----------|---------|-------------|
| `FilePath` | File (local path) | `InArgument` | `String` | Yes (mode A) | | The path to the Apple Numbers file. Part of `OverloadGroup("FilePath")`. |
| `ResourceFile` | File | `InArgument` | `ILocalResource` | Yes (mode B) | | The spreadsheet file resource (resolved to a local path at runtime). Part of `OverloadGroup("ResourceFile")`. |

### Output

| Name | Display Name | Type | Description |
|------|-------------|------|-------------|
| `Result` | Result | `IList<`[`NumbersSheet`](types/NumbersSheet.md)`>` | A list of sheets contained in the document, each with the [tables](types/NumbersTable.md) it contains. |

## Valid Configurations

Exactly one of `FilePath` or `ResourceFile` must be set (enforced via `[OverloadGroup]`).

## XAML Example

**Mode A — FilePath:**

```xml
<applenumbers:GetSheets DisplayName="Get Sheets"
    FilePath="[&quot;/Users/me/Documents/report.numbers&quot;]"
    Result="[sheets]" />
```

**Mode B — ResourceFile:**

```xml
<applenumbers:GetSheets DisplayName="Get Sheets"
    ResourceFile="[spreadsheetResource]"
    Result="[sheets]" />
```

## Notes

- A Numbers document is a list of sheets; each sheet hosts one or more named tables (the equivalent of Excel worksheet tables). Use this activity to discover the sheet + table names before wiring `Sheet` / `TableName` into `ReadRange`, `ReadCell`, `WriteRange`, or `WriteCell`.
- The returned [`NumbersTable`](types/NumbersTable.md) currently carries only the table name — there is no used-range or size information returned.
