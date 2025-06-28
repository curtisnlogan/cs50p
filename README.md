## 1. HTML Foundations

### 1.1 HTML Mindset — _Structure First, Shine Later_

- **Core Idea:** Finish HTML structure before styling or scripting to avoid bugs.
- **Headings:** Use `<h1>` once per page; `<h2>`–`<h6>` for subsections.
- **Images:** Add `alt="description"` for accessibility (e.g., `"Profile photo"`); use `alt=""` for decoration.
- **Classes:** Assign a class to every `<div>` (e.g., `.container`) for styling ease.

**Debugging Tip:**

- Check for unclosed tags in Chrome DevTools if layout breaks.

**Mini-Exercise:**

- Build a webpage with a header, nav, main content, and footer. Use proper heading hierarchy.

---

### 1.2 Boilerplate Starter

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css" />
    <script src="app.js" defer></script>
  </head>
  <body>
    <!-- Content here -->
  </body>
</html>
```

- **Key Elements:**
  - `<!DOCTYPE html>`: Ensures modern rendering.
  - `lang="en"`: Boosts accessibility/SEO.
  - `defer`: Loads JS after HTML.

**Debugging Tip:**

- If JS doesn’t work, confirm `defer` is on `<script>`.

---

### 1.3 Core Elements & Semantics

| **Type**  | **Elements**                              | **Tip**                     |
| --------- | ----------------------------------------- | --------------------------- |
| Metadata  | `<title>`, `<meta>`, `<link>`             | Keep in `<head>`            |
| Structure | `<header>`, `<nav>`, `<main>`, `<footer>` | Use for accessibility       |
| Text      | `<h1>`–`<h6>`, `<p>`, `<ul>`, `<li>`      | Match list type to content  |
| Media     | `<img>`, `<video>`                        | Always add `alt` to `<img>` |
| Forms     | `<form>`, `<input>`, `<label>`            | Link `<label>` to `<input>` |

**Mini-Exercise:**

- Create a form with a labeled text input and button.

---

## 2. CSS Essentials

### 2.1 Stylesheet Basics

- **Preferred Method:** External CSS via `<link rel="stylesheet" href="styles.css">`.
- **Syntax:** Use `;` between rules; comment sections (e.g., `/* Layout */`).

**Mini-Exercise:**

- Create a `styles.css` file with sections for reset, typography, and layout.

---

### 2.2 Box Model

- **Layers:** Content → Padding → Border → Margin.
- **Reset:** Add `box-sizing: border-box;` globally.
- **Height:** Avoid fixed heights to prevent overflow.

**Debugging Tip:**

- Use DevTools to tweak padding/margins live.

---

### 2.3 Units

| **Unit** | **Relative To** | **Use Case**         |
| -------- | --------------- | -------------------- |
| `px`     | Absolute        | Borders, fixed sizes |
| `rem`    | Root font-size  | Typography, spacing  |
| `%`      | Parent size     | Responsive layouts   |
| `vh`     | Viewport height | Full-screen elements |

**Mini-Exercise:**

- Style a button with `rem` for padding and font-size.

---

### 2.4 Layouts

- **Flexbox:**
  ```css
  .container {
    display: flex;
    gap: 1rem;
    justify-content: space-between;
  }
  ```
- **Grid:**
  ```css
  .grid {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 1rem;
  }
  ```

**Mini-Exercise:**

- Build a two-column layout with Grid.

---

### 2.5 Responsive Design

- **Mobile-First:** Write base styles, then add breakpoints:
  ```css
  @media (min-width: 768px) {
    /* Desktop styles */
  }
  ```

**Mini-Exercise:**

- Make a navbar collapse on mobile with a media query.

---

## 3. JavaScript Fundamentals

### 3.1 Variables

- **Default:** `const`; use `let` for reassignment.
- **Types:** `number`, `string`, `boolean`, `null`, `undefined`, `array`, `object`.

**Mini-Exercise:**

- Create an array with `const` and modify it with `.push()`.

---

### 3.2 Functions

- **Arrow Syntax:**
  ```javascript
  const sum = (a, b) => a + b;
  ```

**Debugging Tip:**

- If `this` fails, check arrow function scope.

---

### 3.3 DOM & Events

- **Select:** `document.querySelector('.btn')`
- **Event:**
  ```javascript
  document.querySelector(".btn").addEventListener("click", () => alert("Hi"));
  ```

**Mini-Exercise:**

- Add a button that changes the page’s background color on click.

---

## 4. Python Basics

### 4.1 Input & Output

- **F-Strings:** `f"Hello, {name}"`
- **Input:** `name = input("Name: ")`

**Mini-Exercise:**

- Write a script to greet a user by name.

---

### 4.2 Loops & Conditionals

- **If:**
  ```python
  if x > 0: print("Positive")
  else: print("Negative")
  ```
- **Loop:** `[x * 2 for x in range(5)]`

**Mini-Exercise:**

- Generate a list of even numbers using comprehension.

---

## 5. General Tips

### 5.1 Git Basics

- **Workflow:** `git add .` → `git commit -m "msg"` → `git push`
- **Check:** `git status`

**Debugging Tip:**

- Run `git pull` if `push` fails.

---

### 5.2 Coding Habits

- **Rest:** Take breaks every 20 minutes.
- **Practice:** Spend 60-70% of time coding, not note-taking.

---

## 6. Using These Notes

- **Review:** Check weekly; update with a “Last Updated” date.
- **Practice:** Do mini-exercises after each section.
- **Store:** Keep in a searchable tool (e.g., Notion).
- **Share:** Post on GitHub for feedback.

---

Keep coding, stay concise, and build small projects to solidify these concepts!
