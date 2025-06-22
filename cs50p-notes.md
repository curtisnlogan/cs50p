# cs50p-notes

(12:35) https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@ea6fc5c250bc4fc786575db3b93611a5/block-v1:HarvardX+CS50P+Python+type@vertical+block@ae607d49594541069761d6077d6c1fee

## Week 0: Introduction to Python Basics

- **Code as Text**: Code is essentially plain text, but it’s typically written in specialized editors or Integrated Development Environments (IDEs) rather than tools like Google Docs, which aren’t designed for execution or compilation.
- **Terminal (CLI)**: The terminal, or Command-Line Interface (CLI), allows you to interact with your operating system (e.g., PC or Mac) by entering commands.
- **Python Interpreter**: When you write `print("hello, world")`, the Python interpreter processes it through several stages—lexical analysis, parsing, compilation to bytecode, and interpretation—ultimately converting it to binary (0s and 1s) for the hardware to execute.
- **Functions**: Much of coding involves creating functions—reusable blocks of code that take inputs, process them, and return outputs. Think of them as actions in a program.
- **Built-in Functions**: Python provides built-in functions like `print()` to perform common tasks.
- **`return` Statement**: The `return` keyword retrieves a value from a function, which can then be assigned to a variable. Note that not all functions need to return a value—some just perform actions.
- **Indentation**: Python requires indentation (typically 4 spaces) to define code structure syntactically, unlike many languages where it’s just stylistic.
- **Scope of `return`**: The `return` keyword can only be used inside a function.
- **Global Variables**: Avoid modifying global variables within functions; it makes debugging difficult when multiple functions alter the same variable. Instead, pass variables as arguments and return results.
- **Arguments**: Functions can accept arguments—values passed in to influence their behavior. These can be positional (order matters) or keyword-based (named).
- **Methods**: Methods are functions tied to objects (e.g., string methods like `.strip()` or `.title()` belong to `str` objects).
- **Nested Functions**: You can nest function calls, where the result of one becomes the argument for another, e.g., `print(len(str(12345)))`.
- **Interactive Mode**: Test Python code line-by-line in the terminal using Python’s interactive mode.
- **Indentation Standard**: Use 4 spaces for indentation within functions, ensuring consistency across your code.
- **Readability**: Avoid overly minimalist code (e.g., cramming everything into one line); prioritize clarity over brevity.
- **Data Types**:
  - **`int`**: Whole numbers, arbitrarily large in Python (limited only by memory), from negative to positive infinity.
  - **`float`**: Numbers with decimal points, representing real numbers with precision limitations.
  - **`str`**: Text, defined using single (`'`) or double (`"`) quotes—be consistent in your choice.
- **Mathematical Operations**: Python supports `+` (addition), `-` (subtraction), `/` (true division, yields floats), `*` (multiplication), `//` (floor division), `%` (modulo, remainder), and `**` (exponentiation).
- **Division and Modulo**:
  - `/` performs true division (e.g., `5 / 2 = 2.5`).
  - `%` returns the remainder after division (e.g., `5 % 2 = 1`).
- **Parameters**: Parameters are variables in a function definition that specify what arguments it accepts. See Python’s official documentation for details.
- **Positional Parameters**: Must be passed in the order defined in the function.
- **Keyword Parameters**: Can have default values, allowing optional arguments that you can override when calling the function.
- **Bugs**: Mistakes in code are inevitable, even for professionals. Debugging is a core skill in programming.
- **Literal Interpretation**: Computers execute code exactly as written—a missing parenthesis can crash a program, unlike casual human communication.
- **GUI vs CLI**: Code doesn’t require a Graphical User Interface (GUI); many programs run via the CLI, though GUIs enhance user experience in some cases.
- **Function Calls**: Parentheses `()` trigger a function’s execution.
- **`input()`**: This function allows users to enter data, making programs interactive.
- **Variables**: Variables store data for later use or modification, acting as labeled containers.
- **Naming**: Use descriptive variable names (e.g., `name` instead of `x`) for clarity.
- **Assignment**: The `=` operator assigns the value on the right to the variable on the left (e.g., `name = "Curtis"`).
- **Comments**: Use `#` for comments, which Python ignores. Place brief comments inline and longer explanations above code blocks.
- **Scope**: Variables defined inside a function are local and inaccessible outside it.
- **Pseudocode**: Write logical, language-agnostic plans in natural language to outline a program’s structure.
- **Docstrings**: Triple-quoted strings (`"""…"""`) document classes, functions, or methods, enhancing code readability.
- **Problem-Solving**: Programming offers multiple solutions to a problem—it’s a creative process.
- **String Concatenation**: Use `+` to join strings, though **f-strings** are often clearer and more efficient. Concatenation is useful for building lists iteratively.
- **Newlines**: The `\n` character inserts a new line in text.
- **F-Strings**: Introduced in Python 3.6, f-strings (e.g., `f"Name: {name}"`) are the preferred way to embed variables in strings, though concatenation may suit specific cases like list iteration.
- **Terminal Navigation**: Use `↑` and `↓` arrow keys to scroll through your command history in the terminal.

### F-String Formatting Example: `f'{z:,.2f}'`
- `,` : Adds a thousands separator.
- `.2f` : Formats the number with exactly 2 decimal places.

```python
z = 1234.56789
print(f'{z:,.2f}')  # Output: 1,234.57
```

### Terminal Commands
- **Unix/Linux**: `ls` (list), `cp` (copy), `mv` (move), `rm` (remove), `mkdir` (make directory), `cd` (change directory), `rmdir` (remove directory), `clear` (clear screen).
- **Windows**: `dir` (list), `copy` (copy), `move` (move), `del` (delete), `mkdir` (make directory), `cd` (change directory), `rmdir` (remove directory), `cls` (clear screen).
- **Tab-Completion**: Autocompletes commands in the terminal.
- **Parent Directory**: `..` refers to the directory above the current one.
- **Home Directory**: Typing `cd` alone returns you to your home directory.

---

## Week 1: Conditionals

- **Conditionals**: These create decision points in a program, like forks in a road.
- **Comparison Operators**:
  - `>` (greater than)
  - `>=` (greater than or equal to)
  - `<` (less than)
  - `<=` (less than or equal to)
  - `==` (equal to)
  - `!=` (not equal to)
- **`if` Statements**: Execute indented code if a condition is true, allowing Python to “ask questions.”
- **Booleans**: Named after George Boole, these are `True` or `False` values.
- **Truthiness**: Python automatically evaluates expressions for their truth value in conditions.
- **`elif`**: Follows an `if` statement and checks additional conditions only if prior ones fail, improving efficiency.
- **`else`**: Executes when all previous conditions are false; no condition is specified (just `else:`).
- **Logical Operators**:
  - **`or`**: True if at least one condition holds.
  - **`and`**: True only if both conditions hold.
  - **`not`**: Negates a condition’s truth value.
- **Chained Comparisons**: More readable and efficient than multiple `and` statements (e.g., `80 <= score < 90` vs. `score >= 80 and score < 90`).

```python
score = 85
if 80 <= score < 90:  # Pythonic
    print("B")
```

- **`match` Statement** (Python 3.10+): Simplifies code by matching a value against multiple cases.

---

## Week 2: Loops and Data Structures

- **`while` Loops**: Repeat code as long as a condition is true—ideal when the number of iterations is unknown.
- **`for` Loops**: Perfect for iterating over sequences like lists.
- **Lists**: Ordered collections defined with square brackets, e.g., `[1, 2]`.
- **Infinite Loops**: `while True` runs forever until interrupted with `break`. Avoid nesting these, as it complicates debugging.
- **Data Structures**:
  - **List**: An ordered sequence of values.
  - **Dictionary**: An unordered collection of key-value pairs.
- **`range()` vs `enumerate()`**:
  - **`range()`**: Generates a number sequence for looping a set number of times or accessing items by index.

    ```python
    my_list = ["a", "b", "c"]
    for i in range(len(my_list)):
        print(i, my_list[i])
    ```

  - **`enumerate()`**: Provides both index and value, making loops cleaner.

    ```python
    for i, value in enumerate(my_list):
        print(i, value)
    ```

  - Use `enumerate()` when you need both index and item; use `range()` for numbers or index-only access.
- **Dictionaries**:
  - Access values with keys, e.g., `f"{spacecraft['name']}"`.
  - **`.get(key, default)`**: Retrieves a value, returning a fallback if the key isn’t found.
  - **`.update()`**: Adds new key-value pairs to a dictionary.
  - **`.keys()`**: Returns a view of keys, iterable in a loop.
  - **`.values()`**: Returns a view of values.
  - **`.pop(key)`**: Removes and returns a value by key.
  - **`.clear()`**: Empties the dictionary.
  - **`.items()`**: Yields key-value pairs for iteration.

    ```python
    words = {"cat": 3, "dog": 4}
    for word, points in words.items():
        print(word, points)
    ```

- **List Methods**:
  - **`.append(item)`**: Adds one item to the end.
  - **`.remove(item)`**: Removes the first occurrence of an item.
  - **`.extend(iterable)`**: Adds multiple items from an iterable.
  - **`.insert(index, item)`**: Adds an item at a specific index, e.g., `list.insert(0, "Bowser")`.
  - **`.count(item)`**: Counts occurrences of an item.
  - **`.pop()`**: Removes and returns the last item (or a specific index if provided).
- **List Comprehensions**: Create new lists concisely.

  ```python
  names = ["WEF", "WEFWF", "WFWF"]
  names_lower = [name.lower() for name in names]  # ["wef", "wefwf", "wfwf"]
  ```

  With a condition:

  ```python
  names_lower = [name.lower() for name in names if len(name) > 3]  # ["wefwf", "wfwf"]
  ```

- **String Slicing**: `string[start:stop]`—`start` is inclusive, `stop` is exclusive, indexing starts at 0. Omitting `start` defaults to 0.
- **Tuples**: Immutable sequences (e.g., `(1, 2)`), memory-efficient for fixed data. Unpack them into variables:

  ```python
  coordinates = (40.7128, -74.0060)
  latitude, longitude = coordinates
  ```

---

## Notes on Pseudocode in Python

### Where to Place Pseudocode
1. **Top of File**: High-level overview of the program.

   ```python
   # Pseudocode:
   # 1. Load data
   # 2. Clean data
   # 3. Train model
   # 4. Evaluate results
   ```

2. **Above Functions**: Describe the function’s purpose.

   ```python
   # Pseudocode:
   # If input is valid:
   #   Process input
   #   Return result
   def my_function(input):
       ...
   ```

3. **Inline**: Explain step-by-step logic within functions.

   ```python
   def calculate_average(data):
       # Pseudocode: ignore None values
       clean_data = [x for x in data if x is not None]
   ```

### How to Write Pseudocode
- Use `#` to mark comments.
- Keep it clear, logical, and language-agnostic.
- Use indentation or lists for structure.

### What to Avoid
- Don’t write pseudocode without `#`—it’ll cause syntax errors.
- Don’t blend pseudocode and code confusingly.
- Keep it simple, not overly detailed.

---

## `return` vs `break`
- **`return`**: Exits a function entirely, breaking any loop within it and returning a value.
- **`break`**: Exits only the nearest enclosing loop, allowing the function to continue.

---

## Week 3: Exceptions and Debugging

- **Syntax Errors**: Mistakes in code structure (e.g., a typo or missing colon), like grammatical errors in English. They must be fixed for the code to run.
- **Runtime Errors**: Occur during execution, often from invalid input or logic errors (e.g., division by zero). Defensive coding helps prevent them.
- **Exception Handling**:
  - **`try`**: Wraps code that might fail.
  - **`except`**: Catches specific errors you anticipate.

    ```python
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not a number")
    else:
        print(f"x is a number: {x}")
    ```

  - **`else`**: Runs if no exceptions occur.
- **Best Practices**:
  - Avoid broad `except` clauses—specify errors (e.g., `except ValueError`) for clarity.
  - Limit `try` blocks to only the code that might raise an exception.
- **Common Errors**:
  - **`ValueError`**: Often from invalid user input (e.g., entering "abc" when a number is expected).
  - **`NameError`**: Using an undefined variable or function.
  - **`KeyError`**: Accessing a non-existent dictionary key.
- **Loop Control**:
  - **`break`**: Exits a loop immediately.
  - **`return`**: Exits a function, breaking any loop inside it.
- **`pass`**: A no-op statement to silently ignore an exception or placeholder code.
- **Pythonic Approach**: Prefer “Easier to Ask for Forgiveness than Permission” (EAFP)—use `try`/`except` over pre-checking conditions (e.g., `.isnumeric()`).
- **Debugging**:
  - **Breakpoints**: In VS Code, red dots next to code lines pause execution, letting you inspect variables and program state.

---

NEW NOTES

* raising an error alone doesn't handle it. one needs to use it in an 'except' as something like 'e' to decide what to do with that error
* otherwise program simply stops running by default

NEW NOTES LIBRARIES

* modules exist to stop us from having to endlessly copy and paste code that we often want to reuse
* there are some in-built libraries like 'random' for-example but you have to 'import' them
* you don't have to write all of your code yourself, pretty much nobody does this at the proffesional level
* video games are often built with a ton of reused code from numerous places, in-house and external
* 'seq' usually used to refer to something that is list like
* 'from' allows you to import specific things from modules, more memory efficient
* not using 'from' also means you always have to type in the module name to access a function from it
* 'from random import choice'
* though importing an entire library stops naming conflicts with your own functions for example
as the module name also has to be written out before you call the function
* for large programs this 'import' would likely be the better option
* random.randit(a, b) both numbers are inclusive a = 1 b = 10 the answer could be from 1 to 10 when called
* 
