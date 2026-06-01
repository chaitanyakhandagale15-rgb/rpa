# Write Cell

`UiPath.AppleNumbers.Activities.WriteCell`

Writes a value to a single cell in an Apple Numbers spreadsheet. The value is stringified via `ToString()` before being passed to the AppleScript template — cell type inference is performed by Numbers based on the text content.

**Package:** `UiPath.AppleNumbers.Activities`
**Category:** `Integrations.AppleNumbers.Numbers`
**Platform:** macOS only

## Properties

### Input

| Name | Display Name | Kind | Type | Required | Default | Description |
|------|-------------|------|------|----------|---------|-------------|
| `FilePath` | File (local path) | `InArgument` | `String` | Yes (mode A) | | The path to the Apple Numbers file. Part of `OverloadGroup("FilePath")`. |
| `ResourceFile` | File | `InArgument` | `IResource` | Yes (mode B) | | The spreadsheet file resource (resolved to a local path at runtime via `ToLocalResource()`). Part of `OverloadGroup("ResourceFile")`. |
| `Sheet` | Sheet | `InArgument` | `String` | Yes | | The name of the sheet to write to (e.g. `"Sheet1"`). |
| `Cell` | Cell | `InArgument` | `String` | Yes | | The cell to write to in A1 notation (e.g. `"A1"`, `"B3"`). |
| `WhatToWrite` | What to write | `InArgument` | `Object` | Yes | | The value to write. Converted to string via `ToString()` before being sent to Numbers. |
| `TableName` | Table name | `InArgument` | `String` | No | | The name of the table on the sheet to write to (e.g. `"Table 1"`). Omit to target the default/first table. |

### Output

This activity has no visible output. (A `Result` of type `Boolean` exists internally but is set to `IsVisible = false` by the metadata — do not rely on it.)

## Valid Configurations

Exactly one of `FilePath` or `ResourceFile` must be set (enforced via `[OverloadGroup]`).

## XAML Example

**Mode A — FilePath:**

```xml
<applenumbers:WriteCell DisplayName="Write Cell"
    FilePath="[&quot;/Users/me/Documents/report.numbers&quot;]"
    Sheet="[&quot;Sheet1&quot;]" Cell="[&quot;B2&quot;]"
    WhatToWrite="[total]" />
```

**Mode A — FilePath, write into a specific table:**

```xml
<applenumbers:WriteCell DisplayName="Write Cell"
    FilePath="[&quot;/Users/me/Documents/report.numbers&quot;]"
    Sheet="[&quot;Summary&quot;]"
    TableName="[&quot;Totals&quot;]"
    Cell="[&quot;A1&quot;]"
    WhatToWrite="[&quot;Updated&quot;]" />
```

## Notes

- `WhatToWrite` is stringified with `ToString()` and then passed to the AppleScript template; Numbers infers the cell's stored type from the text (numbers, dates, booleans). To force a specific format, write the string in the locale used by Numbers on the host.
- Each invocation shells out a fresh `osascript` call, which opens Numbers, writes the cell, saves, and lets Numbers close the document. For batches of writes, prefer `WriteRange` over many `WriteCell` calls.
- `ResourceFile` accepts the broader `IResource` interface on write activities (rather than `ILocalResource`) — it is resolved to a local file via `ToLocalResource()` at runtime.
