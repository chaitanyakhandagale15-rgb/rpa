# UiPath.AppleNumbers.Activities — Overview

`UiPath.AppleNumbers.Activities`

A set of activities for automating Apple Numbers spreadsheets (`.numbers`) by driving the Numbers.app via AppleScript. Each activity runs a templated `osascript` invocation against the user's local Numbers install — no cloud service and no Microsoft Office dependency. The pack is macOS-only.

## Documentation

- [Activities](activities/) — per-activity reference.
- [Types](activities/types/) — reference for the input enum ([CellValueType](activities/types/CellValueType.md)) and the output shapes returned by GetSheets ([NumbersSheet](activities/types/NumbersSheet.md), [NumbersTable](activities/types/NumbersTable.md)).

## Activities

### Apple Numbers

| Activity | Description |
|----------|-------------|
| [Read Cell](activities/ReadCell.md) | Reads the value of a single cell. |
| [Read Range](activities/ReadRange.md) | Reads a range of cells into a `DataTable`. |
| [Write Cell](activities/WriteCell.md) | Writes a value to a single cell. |
| [Write Range](activities/WriteRange.md) | Writes a `DataTable` to a range starting at a given cell. |
| [Get Sheets](activities/GetSheets.md) | Returns the list of sheets in a document, together with the tables each sheet contains. |

## Common Patterns

All activities identify the target document in one of two **mutually exclusive modes**, declared as `[OverloadGroup]` attributes on each activity:

1. **`FilePath`** — pass a local file system path to a `.numbers` document.
2. **`ResourceFile`** — pass a Studio-managed resource (`UiPath.Platform.ResourceHandling.ILocalResource` on read activities and `GetSheets`; `IResource` on `WriteCell` / `WriteRange`). The resource is resolved to a local path at runtime.

In the designer, the `File (local path)` and `File` (resource) fields offer a menu action to toggle between the two modes — only one is visible at a time, matching the mutually exclusive wiring in the runtime.

All activities that operate on a single sheet accept an optional **`TableName`**. Apple Numbers organizes cells inside named tables on a sheet (each sheet can host multiple tables). When omitted, the activity targets the default/first table; when set, the activity targets that specific table on the sheet.

## Platform

**macOS only.** All activities shell out to `osascript` to drive Numbers.app. The host must have Apple Numbers installed. There is no Windows or Linux support.
