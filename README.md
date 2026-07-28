# Dependency Checker

A simple one-file Python tool that scans Python files, finds dependencies, checks if they are installed, installs missing packages, and can generate a `requirements.txt` file.

Made to keep Python projects simple. One file. One command. Done.

## Features

✅ Scan Python files for imports
✅ Detect installed packages
✅ Detect missing packages
✅ Install missing dependencies with `--fix`
✅ Generate `requirements.txt` with `--requirements`
✅ Detect Python built-in modules
✅ No configuration files needed

## Installation

Clone the repository:

```bash
git clone https://github.com/MAXFEVASIGMA000/dependency-checker.git
```

Enter the folder:

```bash
cd dependency-checker
```

No extra packages required.

## Usage

### Check dependencies

```bash
python dependency_checker.py your_file.py
```

Example:

```text
=========================
  Dependency Checker
=========================

File:
main.py

Dependencies:

✓ os - Python built-in
✓ requests - installed
✗ numpy - missing
```

---

### Automatically install missing packages

```bash
python dependency_checker.py your_file.py --fix
```

Example:

```text
Missing packages:

 - numpy

Install missing packages? (y/n): y

Installing:
numpy

✓ Installation complete!
```

---

### Create requirements.txt

```bash
python dependency_checker.py your_file.py --requirements
```

Creates:

```text
requirements.txt
```

Example:

```text
requests
numpy
pillow
```

## How It Works

Dependency Checker uses Python's built-in tools:

* `ast` to read Python imports
* `importlib` to check installed packages
* `pip` to install missing dependencies

It does not execute the code being scanned.

## Example Workflow

Clone a project:

```bash
git clone project
```

Check dependencies:

```bash
python dependency_checker.py main.py
```

Install missing packages:

```bash
python dependency_checker.py main.py --fix
```

Create requirements:

```bash
python dependency_checker.py main.py --requirements
```

