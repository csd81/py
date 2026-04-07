# Coding Style Guidelines for Agents

When contributing to this Python repository, follow the style rules below.
These apply to all new code and to any code you modify.

## Indentation

- Use **4 spaces** per indentation level.
- Never use tabs.

## Line Length

- Limit all lines to **79 characters**.
- For docstrings and comments, limit to **72 characters**.

## Blank Lines

- Surround top-level function and class definitions with **two blank lines**.
- Method definitions inside a class are surrounded by **one blank line**.
- Use blank lines sparingly inside functions to indicate logical sections.

## Imports

- Place imports at the top of the file, after any module docstring and before module globals and constants.
- Group imports in this order, with a blank line between each group:
  1. Standard library imports
  2. Related third-party imports
  3. Local application/library imports
- Use one import per line.
- Prefer absolute imports over relative imports.

```python
# Good
import os
import sys

import requests

from mypackage import mymodule
```

## Naming Conventions

| Identifier        | Style         | Example              |
|-------------------|---------------|----------------------|
| Variables         | `snake_case`  | `user_count`         |
| Functions         | `snake_case`  | `get_user_name()`    |
| Constants         | `UPPER_SNAKE` | `MAX_RETRIES`        |
| Classes           | `PascalCase`  | `UserProfile`        |
| Private members   | `_single_leading_underscore` | `_cache` |

## String Quotes

- Use **double quotes** (`"`) for strings by default.
- Use single quotes only when the string itself contains a double quote to avoid backslash escaping.

## Whitespace in Expressions

- No spaces immediately inside parentheses, brackets, or braces.
- No spaces before a comma, semicolon, or colon.
- One space on each side of binary operators (`=`, `+`, `-`, `==`, etc.).
- No space around the `=` in keyword arguments or default parameter values.

```python
# Good
result = value_one + value_two
def connect(host, port=8080):
    ...
```

## Type Hints

- Add type hints to all new function signatures.
- Use `Optional[X]` (or `X | None` for Python 3.10+) for values that may be `None`.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

## Docstrings

- Write docstrings for all public modules, classes, and functions.
- Use triple double-quotes (`"""`).
- Follow the [Google-style docstring format](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).

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

## Comments

- Write comments in English.
- Keep inline comments minimal; prefer self-documenting code.
- Inline comments should be separated by at least two spaces from the statement and start with `# `.

## Error Handling

- Catch specific exception types rather than bare `except:`.
- Avoid silently swallowing exceptions.

```python
# Good
try:
    data = fetch_data()
except ValueError as exc:
    logger.error("Invalid data: %s", exc)
    raise
```

## Miscellaneous

- Avoid mutable default arguments (`def f(x=[])`); use `None` as default and initialize inside the function.
- Prefer list/dict/set comprehensions over `map`/`filter` when readability is equal.
- End every file with a single newline character.
