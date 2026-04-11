---
title: Create a script that lists out notifications from the queue
status: open
priority: normal
dateCreated: 2026-03-31T20:11:54.555+07:00
dateModified: 2026-03-31T20:11:54.555+07:00
tags:
  - task
sr-due: 2026-04-29
sr-interval: 18
sr-ease: 250
---

# Dunst History JSON Schema

This document describes the structure of the JSON returned by:

```sh
dunstctl history
```

Dunst exports notification history as a D-Bus variant type `aa{sv}` (array of array of string→variant maps). ([Dunst](https://dunst-project.org/documentation/dunstctl/?utm_source=chatgpt.com "Documentation · Dunst"))

---

## Overview

```json
{
  "type": "aa{sv}",
  "data": [
    [
      { …notification object… }
    ],
    [
      { …notification object… }
    ],
    …
  ]
}
```

- **type**: Always `"aa{sv}"`, indicating an array of arrays of dictionaries with string keys and variant values.
    
- **data**: A list of lists; each inner list contains exactly one notification object.
    
- Each notification object maps **field names** to objects with `type` and `data`.
    

---

## Notification Object Fields

Each notification object may include the following fields:

|Field|D-Bus Type|Description|
|---|---|---|
|`body`|`s`|Main notification text (may be empty).|
|`message`|`s`|Combined title/body with markup.|
|`summary`|`s`|Notification title.|
|`appname`|`s`|Application that sent the notification.|
|`category`|`s`|Category hint (often empty).|
|`default_action_name`|`s`|Default action label.|
|`icon_path`|`s`|Path to the notification icon (may be empty).|
|`id`|`i`|Internal notification ID.|
|`timestamp`|`x`|Internal timestamp (not a wall-clock timestamp).|
|`timeout`|`x`|Timeout in milliseconds.|
|`progress`|`i`|Progress value or −1 if unused.|
|`urgency`|`s`|Urgency level (e.g., `"LOW"`, `"NORMAL"`, `"CRITICAL"`).|
|`stack_tag`|`s`|Stack tag hint (may be empty).|
|`urls`|`s`|URLs associated with the notification (may be empty).|

> Not every notification will have every field; absent fields simply won’t appear in that object.

---

## Field Semantics

### Variant Objects

Each field value in a notification object looks like:

```json
"summary": {
  "type": "s",
  "data": "Example title"
}
```

- **type**: The D-Bus variant type (`s` = string, `i` = 32-bit integer, `x` = 64-bit integer).
    
- **data**: The actual value.
    

### Common Field Meanings

- **body**: The body text of the notification.
    
- **message**: Title + body (often with markup).
    
- **summary**: The title or short summary.
    
- **appname**: The sender’s name.
    
- **id**: Unique identifier within Dunst’s history.
    
- **timestamp**: Dunst’s internal timestamp; community reports indicate it’s relative to session/uptime rather than absolute wall-clock time. ([Reddit](https://www.reddit.com/r/suckless/comments/1g5s57t?utm_source=chatgpt.com "Dunst notification timestamp"))
    

---

## Example Entry

```json
{
  "body": { "type": "s", "data": "" },
  "message": { "type": "s", "data": "<b>mouse layer exited</b>" },
  "summary": { "type": "s", "data": "mouse layer exited" },
  "appname": { "type": "s", "data": "notify-send" },
  "category": { "type": "s", "data": "" },
  "default_action_name": { "type": "s", "data": "default" },
  "icon_path": { "type": "s", "data": "" },
  "id": { "type": "i", "data": 32835 },
  "timestamp": { "type": "x", "data": 120591819109 },
  "timeout": { "type": "x", "data": 500000 },
  "progress": { "type": "i", "data": -1 },
  "urgency": { "type": "s", "data": "NORMAL" },
  "stack_tag": { "type": "s", "data": "" },
  "urls": { "type": "s", "data": "" }
}
```

---

## Notes for Parsing

- Because the outer structure is `aa{sv}`, you’ll typically loop over `data`, then extract the single object inside each sub-array.
    
- You can use a JSON parser (e.g., `jq`, Python `json`) to iterate and extract fields by their `data` values.
    
- For timestamps, you may need to convert relative time to a real timestamp using system uptime or Dunst start time (community scripts exist for this). ([Reddit](https://www.reddit.com/r/suckless/comments/1g5s57t?utm_source=chatgpt.com "Dunst notification timestamp"))
    

---

## Sample jq Extraction

To list titles and bodies:

```sh
dunstctl history | jq '.data[][] | {title: .summary.data, body: .body.data}'
```

---

## References

- `dunstctl history` exports history as JSON. ([Dunst](https://dunst-project.org/documentation/dunstctl/?utm_source=chatgpt.com "Documentation · Dunst"))
    
- Dunst keeps history in memory and allows recall up to the configured limit. ([Dunst](https://dunst-project.org/documentation/?utm_source=chatgpt.com "Documentation · Dunst"))
    

---

If you want a **JSON Schema (Draft 7 / 2019-09)** file based on this document for validation or code generation, I can generate that next.
