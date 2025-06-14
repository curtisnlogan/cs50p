Week 0
• Code is just text; you could even write it in Google Docs.
• The terminal (CLI) is how you access the underlying PC/Mac.
• The Python interpreter takes print("hello, world") and ultimately turns it into 0 s and 1 s at the hardware level.
• A lot of coding is just producing things that take inputs and return outputs; these are often called functions.
• Functions are like verbs and adverbs. Languages come with pre-installed functions, like print.
• return allows you to get back some kind of value from a function. That value can be assigned to a variable.
• Python demands indentation unlike some other languages.
• return can only be used inside a function and nowhere else.
• Global variables modified by functions are undesirable; they can be incredibly hard to debug. Imagine numerous functions manipulating the same global variable—how will you pinpoint which one causes problematic behaviour?
• You can pass arguments into a function to influence its behaviour.
• Methods are functions tied to classes like str; examples are .strip() or .title().
• You can use multiple parentheses to call functions inside other functions. The first call becomes an argument inside the second, e.g. print(len(str(12345))).
• You can test code one line at a time in the terminal; this is called interactive mode.
• Indentation inside functions has a standard of 4 spaces; all code must line up.
• Sometimes it isn’t a good idea to be too minimalist, e.g. squeezing everything onto one line can hurt readability.
• int: any whole number up to positive infinity and down to negative infinity.
• float: numbers with a decimal point.
• Python supports standard mathematical operations: +, -, /, \*.
• / is true division and yields floats; % is the modulo operator and gives the remainder after all possible whole numbers of what you’re dividing by have been accounted for.
• Parameters define the kinds of things you can pass into functions as arguments; see the official docs for details.
• A positional parameter must be passed in the order it appears.
• Named parameters can have default values that you reference and override as needed.
• Bugs are mistakes in programs. You will never avoid them entirely, even at a professional level; debugging is a major part of programming.
• One can use single quotes or double quotes for strings—just be consistent.
• str (string) is simply text.
• Computers take things literally; one missing parenthesis can break a whole program (unlike texting a friend).
• Code doesn’t need a GUI, though in many cases a GUI benefits the end-user.
• Parentheses () tell the computer to execute a function.
• The input() function lets users influence a program by entering information.
• A variable is a container for information; it can be referenced later and modified.
• Clear naming matters: using x for something that will hold a name is obscure.
• The assignment operator = means “the thing on the left becomes the thing on the right,” e.g. name = "Curtis". Assignment is right-to-left.
• Comments start with #; Python ignores them.
• Brief comments can sit on the same line; longer explanations belong above the code block.
• Variables defined in functions demonstrate scope; they cannot be accessed outside that function.
• Pseudocode is natural language used to map out a program. It should be thoughtful and logical, not a random riff.
• Triple-quoted strings """…""" are docstrings for classes, functions, and methods. Good documentation is key; your code shouldn’t be an enigma.
• There is almost always more than one way—often many ways—to solve a problem in programming; it’s a creative endeavour.
• + concatenation joins strings; you can embed variables this way, but f-strings are usually better. Concatenation is good for building lists iteratively.
• \n creates a newline in text.
• F-strings are the gold standard for embedding variables seamlessly; in specific cases concatenation may be preferable (e.g. when iterating over lists).
• Use the arrow keys ↑ and ↓ in the terminal to scroll through your command history.

Python f-string: f'{z:,.2f}' Explained
• , → adds a thousands separator
• .2f → formats as a fixed-point number with exactly 2 decimal places

z = 1234.56789
print(f'{z:,.2f}') # Output: 1,234.57

    •	Some terminal (CLI) commands: ls, cp, mv, rm, mkdir, cd, rmdir, clear.
    •	Tab-completion in the terminal can autocomplete commands even if you don’t see suggestions like in IntelliSense.
    •	.. is the parent directory in the terminal.
    •	cd by itself returns you to your default (home) directory.

⸻

Week 1
• Conditionals let us create forks in the road in a program.
• Comparison operators: > greater than, >= greater or equal, < less than, <= less or equal, == equality, != not equal.
• if statements let Python “ask questions”; if something is true, execute the indented code.
• Booleans, named after mathematician George Boole, give two possibilities: True or False.
• Python checks truthiness automatically.
• elif can follow an if. The elif blocks are only evaluated if the preceding if didn’t trigger—more efficient.
• else can be used when you know there’s no other option left. You don’t specify a condition—just else:.
• or lets you check two things at once: if this or that, do something.
• and checks that both things are true; however, chained comparisons are usually more efficient.
• not is logical negation; it checks if something isn’t true.
• Example of a chained comparison (more Pythonic):

elif 80 <= score < 90:
...

versus the less-Pythonic

elif score >= 80 and score < 90:
...

    •	match (Python 3.10+) lets you write clearer code when matching one thing against multiple possibilities to produce specific results.

⸻

Week 2
• while is a construct that lets you keep asking something again and again.
• for is good for iterating through a list.
• [1, 2] is an example of a list (square brackets).
• while True creates an infinite loop until break is used.
Be careful about nesting such loops as it can break the complication rule.
• A list is just values; a dict is keywords with values.
• Sure! Here’s a short and clear note:
• 🔁 range() vs enumerate() in Python
• range() generates a sequence of numbers—handy for looping a specific number of times or for index-based access.

for i in range(len(my_list)):
print(i, my_list[i])

    •	enumerate() gives both the index and the value, making the loop cleaner and more readable.

for i, value in enumerate(my_list):
print(i, value)

✅ Use enumerate() when you need both index and item.
✅ Use range() when you only need numbers or index-based access.

    •	One can access a global dictionary in a Python function by referencing the dictionary variable, e.g. spacecraft, and then writing its key with subscript syntax. Example: f"{spacecraft['name']}" inside an f-string.
    •	.get() on dictionaries lets you pass the expected key as the first argument and a fallback value if the key isn’t found.
    •	.update() can be run on a dictionary; it adds all the new key-value pairs provided.
    •	Dictionaries have built-in methods like .keys(), which you can loop through:

for spacecraft in spacecrafts.keys():
...

    •	You can also use .values() the same way to access values instead of keys.
    •	.pop() returns the value associated with a key and removes the key-value pair.
    •	.clear() removes all key-value pairs in a dictionary.
    •	.items() gives you both key and value:

for word, points in words.items():
...

    •	for loops are extremely powerful for anything iterable.
    •	Lists: .append() adds one item to the end of the list.
    •	.remove() likewise removes an item you pass as an argument.
    •	To add multiple items at once, use .extend() (not .append(), which would nest lists).
    •	.insert() is subscriptable; if you want Bowser in first place of a list of lap finishes, you could do list.insert(0, "Bowser").
    •	List comprehensions let you easily take one list and create a new one:

names = ["wef", "wefwf", "wfwf"]
names_lower = [name.lower() for name in names]

A list of strings names is defined, and the list comprehension makes names_lower, containing all names converted to lowercase.

    •	You can add a condition inside the comprehension:

names_lower = [name.lower() for name in names if len(name) > 2]

    •	The .count() method on lists counts how many times a specific element appears.

Syntax

list_name.count(element)

Example

names = ["wef", "wefwf", "wfwf", "wef"]
count_wef = names.count("wef") # returns 2

.count() is handy when you want to quickly check the frequency of an item.

    •	.pop() can also remove (and return) the last item from a list.
    •	Python string slicing: the first index is inclusive, the second is exclusive. Indexing starts at 0. If you omit the first index, Python assumes you want to start at 0.
    •	You can unpack a tuple into multiple variables:

latitude, longitude = coordinates

coordinates is a tuple in this case.

    •	Tuples are immutable data and cannot be modified; they take up less space in memory and should be used when you don’t need mutability.
    •	While loops are great when you’re not sure how many times you want to loop.
    •	(duplicate of the previous point intentionally preserved) While loops are great for when you’re not sure how many times you want to loop.

---

## 📝 Notes on Including Pseudocode in Python

### ✅ **Where to Place Pseudocode**

1. **Top of the File**

   - Use for a **high-level overview** of the script or program.
   - Helps explain the general algorithm or process flow.

   ```python
   # Pseudocode:
   # 1. Load data
   # 2. Clean data
   # 3. Train model
   # 4. Evaluate results
   ```

2. **Above Function Definitions**

   - Describe **what the function is supposed to do**.
   - Helps others (and future you) understand the intent before reading the code.

   ```python
   # Pseudocode:
   # If input is valid:
   #   Process input
   #   Return result
   def my_function(input):
       ...
   ```

3. **Inline Within Functions**

   - Use for **step-by-step logic** or to explain complex operations.
   - Written as comments next to relevant code.

   ```python
   def calculate_average(data):
       # Pseudocode: ignore None values
       clean_data = [x for x in data if x is not None]
   ```

### ✅ **How to Write Pseudocode in Python**

- Always write pseudocode as **comments** (using `#`).
- Be **language-agnostic and clear**: focus on logic, not syntax.
- Use indentation and lists for readability.

---

### ❌ **What Not to Do**

- Don’t write pseudocode **without comment markers** (`#`) — will cause errors.
- Don’t mix pseudocode **within code** without separation or clarity.
- Avoid overly complex pseudocode; keep it **simple and understandable**.

⸻

return statement:
When executed inside a while True loop (or any loop), it immediately exits the entire function, returning the specified value. This means the loop and the rest of the function won’t continue.

break statement:
To exit only the loop (not the entire function), use break. This stops the loop but allows the function to keep running.

Week 3

https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@bd6e4b312f2b4e8d9e89ec63708a367a/block-v1:HarvardX+CS50P+Python+type@vertical+block@cb3e9f779e7a46ff9af9a64d3efbee01

* syntex error means theres something wrong with the way you've typed your code. like making a grammatical mistake in English
* syntex errors MUST be fixed
* runtime errors are different as they can stem from bad human input. we must take pre-emptive defensive measures against them
* 'try' keyword can be used to catch runtime errors, such as user input mistake
* then use 'except' to catch things that you preemptive think may go wrong
* LOADS of different errors that you will encounter over the years but the WAY inwhich you handle them largely the same
* BAD PRACTICE: if you use general 'except' instead of being specific, you won't know what exactly is going wrong in your code
* the 'try' block should ONLY include the things that could raise the value error
* value error tends to be problem with what others entered
* name error doing something with your code that you shouldn't maybe using a variable that doesn't exist for example
* one can use 'else' statememt after except block to tell python what to do if code does not encounter errors
* try:
    x = int(input("Whats x question mark? "))
except ValueError:
    print("x is not a number")
else:
    print(f'x is a number: {x}')
  * 'break' keyword to get out of loops
  * 'return' also breaks a loop just like it closes off a function
  * you can ignore a warning whilst still catching it with 'pass'
