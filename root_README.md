# Developer Learning

This repository tracks my programming study journey toward becoming a software developer.

The goal is not only to complete exercises, but to build strong fundamentals through:

- reading official and book-based material
- writing code by hand
- solving exercises
- reviewing and refactoring code
- writing notes
- practicing Git and GitHub workflow
- building small projects over time

---

# Current Focus

## Python Fundamentals

Current study path:

```text
Python Crash Course
Exercism Python Track
Custom drills
Code review and refactoring
Small projects
```

The current Python phase focuses on:

- Python syntax
- variables
- strings
- numbers
- functions
- lists
- loops
- ranges
- slicing
- tuples
- basic testing with `assert`
- clean code habits

---

# Repository Structure

```text
developer-learning/
├── python/
│   ├── python-crash-course/
│   │   ├── chapter-01-getting-started/
│   │   ├── chapter-02-variables-simple-data-types/
│   │   ├── chapter-03-introducing-lists-exercises/
│   │   └── chapter-04-working-with-lists/
│   │
│   ├── exercism/
│   │   └── python/
│   │
│   ├── drills/
│   │   ├── week-01/
│   │   └── week-02/
│   │
│   └── reviews/
│
├── README.md
└── .gitignore
```

---

# Study Workflow

For each topic, I follow this cycle:

```text
read → type examples → solve exercises → test → review → refactor → commit
```

## 1. Read

Read the relevant chapter, documentation, or exercise instructions.

## 2. Type examples

Type examples manually instead of only copying them.

## 3. Solve exercises

Write a separate Python file for each exercise when possible.

## 4. Test

Run the files from the terminal.

Example:

```bash
python3 python/python-crash-course/chapter-04-working-with-lists/pizzas.py
```

For simple practice tests:

```bash
python3 python/drills/week-01/test_week_01_drills.py
```

For Exercism tests:

```bash
python3 -m pytest -o markers=task exercise_test.py
```

## 5. Review

Check:

- Does the code run?
- Are variable names clear?
- Is indentation correct?
- Are there unnecessary `print()` calls?
- Should a function use `return` instead?
- Is there repeated logic?
- Can I explain every line?

## 6. Refactor

Improve code after it works.

## 7. Commit

Commit meaningful progress.

```bash
git add .
git commit -m "Complete Chapter 4 loop exercises"
git push
```

---

# Python Study Sources

The main learning sources are:

- Python Crash Course
- Official Python Documentation
- Exercism Python Track
- Custom drills and review questions

Official Python documentation:

```text
https://docs.python.org/3/
```

Exercism Python Track:

```text
https://exercism.org/tracks/python
```

---

# Naming Conventions

Python files should use lowercase letters and underscores.

Good:

```text
simple_message.py
name_cases.py
exercise_3_1_names.py
counting_to_twenty.py
```

Avoid:

```text
SimpleMessage.py
name-cases.py
Exercise 3.py
```

---

# Python Style Rules

Basic style habits:

- use 4 spaces for indentation
- use clear variable names
- keep files organized
- avoid excessive blank lines
- use comments when they explain why something exists
- use `snake_case` for variables and functions
- use uppercase names for constants

Examples:

```python
favorite_language = "Python"
expected_bake_time = 40
EXPECTED_BAKE_TIME = 40
```

Use constants when a value should stay fixed:

```python
EXPECTED_BAKE_TIME = 40
MINUTES_IN_HOUR = 60
```

---

# Git Workflow

Check project status:

```bash
git status
```

Stage changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Describe the work completed"
```

Push to GitHub:

```bash
git push
```

Recommended commit message examples:

```bash
git commit -m "Complete Chapter 3 list exercises"
git commit -m "Add Chapter 4 exercises README"
git commit -m "Refactor Week 1 drills"
git commit -m "Complete Currency Exchange exercise"
```

---

# Generated Files

Do not commit generated Python cache files.

Ignored examples:

```text
__pycache__/
*.pyc
.DS_Store
.venv/
.env
```

If cache files appear, remove them:

```bash
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -r {} +
```

---

# Reviews

Weekly or chapter reviews are stored in:

```text
python/reviews/
```

A review should include:

- what I studied
- exercises completed
- what I understand well
- what still feels weak
- bugs I fixed
- code I refactored
- questions for review
- next focus

---

# Long-Term Roadmap

The long-term goal is to build toward full-stack development.

Planned areas:

```text
Python fundamentals
Django
PostgreSQL
JavaScript review
React
Testing
Git workflow
Small projects
Portfolio projects
Job preparation
```

---

# Definition of Good Progress

Good progress means:

- code runs
- exercises are completed
- mistakes are reviewed
- code is cleaned up
- concepts can be explained
- GitHub is up to date
- weak areas are identified
- practice continues consistently

The goal is not speed.

The goal is clean, tested, explainable code.
