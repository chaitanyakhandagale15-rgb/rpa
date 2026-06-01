# Write Range

`UiPath.AppleNumbers.Activities.WriteRange`

Writes a `DataTable` to a range in an Apple Numbers spreadsheet starting at a given cell. Values are stringified and passed through an AppleScript template; Numbers infers each cell's stored type from the text.

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
| `StartingCell` | Starting cell | `InArgument` | `String` | Yes | | The starting cell in A1 notation (e.g. `"A1"`). The `DataTable` is written with this cell as the top-left. |
| `Data` | Data | `InArgument` | `DataTable` | Yes | | The `DataTable` containing the data to write. |
| `TableName` | Table name | `InArgument` | `String` | No | | The name of the table on the sheet to write to (e.g. `"Table 1"`). Omit to target the default/first table. |

### Configuration

| Name | Display Name | Type | Default | Description |
|------|-------------|------|---------|-------------|
| `UseHeaders` | Use headers | `InArgument<Boolean>` | `True` | If true, the DataTable's column names are written as the first row, and the data rows follow below. |

### Output

This activity has no visible output. (A `Result` of type `Boolean` exists internally but is set to `IsVisible = false` by the metadata — do not rely on it.)

## Valid Configurations

Exactly one of `FilePath` or `ResourceFile` must be set (enforced via `[OverloadGroup]`).

## XAML Example

**Mode A — FilePath with headers:**

```xml
<applenumbers:WriteRange DisplayName="Write Range"
    FilePath="[&quot;/Users/me/Documents/report.numbers&quot;]"
    Sheet="[&quot;Sheet1&quot;]"
    StartingCell="[&quot;A1&quot;]"
    Data="[dt]"
    UseHeaders="[True]" />
```

**Mode A — FilePath into a specific table, no headers:**

```xml
<applenumbers:WriteRange DisplayName="Write Range"
    FilePath="[&quot;/Users/me/Documents/report.numbers&quot;]"
    Sheet="[&quot;Sheet1&quot;]"
    TableName="[&quot;Table 1&quot;]"
    StartingCell="[&quot;B2&quot;]"
    Data="[payload]"
    UseHeaders="[False]" />
```

## Notes

- `Data` is a non-literal WF type — in hand-written XAML bind it to a `DataTable` variable; in the designer it can only be set via VB expression (not a literal value).
- Cell values are converted to strings before being written; Numbers infers the stored type from the text. Use formatting that Numbers recognizes for the host locale if you need deterministic storage.
- The activity only writes the cells inside the destination rectangle — it does not clear cells outside the written region. If you need a "replace" semantic, clear the existing range separately first.
- Each invocation shells out a fresh `osascript` call, which opens Numbers, writes the range, and saves. There is no long-lived scope container in this pack.
- `ResourceFile` accepts the broader `IResource` interface on write activities (rather than `ILocalResource`) — it is resolved to a local file via `ToLocalResource()` at runtime.
