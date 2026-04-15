![[Home logo.jpg | float-center | 200]]
# Todo stuff
> [!info] Get things done:
> Tasks: [[tn-tasks.base|Default]]
> Kanban: [[tn-kanban.base#Inbox|Inbox]], [[tn-kanban.base#Fleeting Notes|Fleeting]], [[tn-kanban.base#Atomic Notes|Atomic]]
> Calendar: [[tn-calendar.base|Calendar]]

# Notes
Recently edited
```base
properties:
  file.mtime:
    displayName: modified
views:
  - type: table
    name: Table
    filters:
      and:
        - file.inFolder("00 Notes")
    order:
      - file.name
      - categories
      - file.tags
    sort:
      - property: file.mtime
        direction: DESC
    limit: 10
  - type: table
    name: All notes
    order:
      - file.name
      - file.mtime
    sort:
      - property: file.mtime
        direction: DESC

```

Unstable notes
```base
formulas:
  linkDiff: file.backlinks.length - file.links.length
  absLinkDiff: if(formula.linkDiff < 0, -formula.linkDiff, formula.linkDiff)
views:
  - type: table
    name: Table
    filters:
      not:
        - file.tags.contains("categories")
        - file.inFolder("99 Templates")
    order:
      - file.name
      - formula.linkDiff
      - file.backlinks
      - file.links
    sort:
      - property: formula.absLinkDiff
        direction: DESC
    limit: 10

```