# GitHub Copilot Instructions

Follow these coding style guidelines for all Python code in this repository.

## Indentation

- Use **4 spaces** per indentation level — never tabs.

## Line Length

- Maximum **79 characters** per line.
- Maximum **72 characters** for docstrings and comments.

## Blank Lines

- Two blank lines before and after top-level functions and classes.
- One blank line between methods inside a class.

## Imports

- One import per line, at the top of the file.
- Group in this order (blank line between groups):
  1. Standard library
  2. Third-party packages
  3. Local modules
- Prefer absolute imports.

## Naming

| Identifier      | Convention              |
|-----------------|-------------------------|
| Variables       | `snake_case`            |
| Functions       | `snake_case`            |
| Constants       | `UPPER_SNAKE_CASE`      |
| Classes         | `PascalCase`            |
| Private members | `_leading_underscore`   |

## Strings

- Use **double quotes** by default.

## Whitespace

- No extra spaces inside brackets/parentheses.
- Spaces around binary operators; no space around `=` in keyword arguments.

## Type Hints

- Annotate all new function signatures with type hints.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

## Docstrings

- Use triple double-quotes for all public modules, classes, and functions.
- Follow Google-style docstrings.

```python
def add(a: int, b: int) -> int:
    """Return the sum of two integers.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The sum of a and b.
    """
    return a + b
```

## Error Handling

- Catch specific exception types (never bare `except:`).

## Miscellaneous

- No mutable default arguments — use `None` and initialize inside the function.
- Prefer comprehensions over `map`/`filter` where readability is equal.
- End every file with a single newline.
