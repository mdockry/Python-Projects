# 🐚 SimplePyShell

A lightweight, interactive shell implemented in Python. **SimplePyShell** supports **built-in commands**, external command execution, proper shell-like argument parsing using `shlex`, and error handling.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)

## 🚀 Features

✅ **Built-in Commands:**
- `cd` – Change directory, supports absolute, relative paths, and `~` for home.
- `pwd` – Print the current working directory.
- `echo` – Print text to the terminal, supporting quoted strings.
- `type` – Identify if a command is a shell builtin or an external executable.
- `exit` – Exit the shell.

✅ **External Command Execution:**
- Runs external programs using `$PATH` lookup.
- Supports running executables like `ls`, `cat`, `grep`, etc.

✅ **Shell-Like Argument Parsing:**
- Handles **single-quoted** arguments (e.g., `echo 'hello world'`).
- Preserves spaces inside quoted strings (`echo 'this   is   a   test'`).

✅ **Error Handling:**
- Proper error messages for unknown commands and invalid directories.
- Handles missing arguments for commands like `cd` and `type`.

---

## 📥 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/SimplePyShell.git
   cd SimplePyShell
