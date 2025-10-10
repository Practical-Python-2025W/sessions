# Setting up our environment

## How to open a native Terminal on your os

Resources for native Terminals:
- **Windows**: [Cmd commands under Windows](https://www.thomas-krenn.com/en/wiki/Cmd_commands_under_Windows)  
- **Mac**: [Bash Shell Tutorial (might be outdated)](https://mmuratarat.github.io/2020-04-01/bash_shell_tutorial) and [Zsh Tutorial](https://academind.com/tutorials/terminal-zsh-basics)

### On Windows
- **Method 1**: Press `Win + R`, type `cmd`, and press Enter.
- **Method 2**: Press `Win + X` and select "Command Prompt" or "Windows PowerShell."
- **Method 3**: Search for "Command Prompt" or "PowerShell" in the Start menu.

### On macOS
- **Method 1**: Press `Cmd + Space`, type "Terminal," and press Enter.
- **Method 2**: Go to Applications → Utilities → Terminal.

---

## Bash/Zsh
On some of the common UNIX-Systems (Linux distros and MacOS) bash is already the default. 
On newer MacOs Versions Zsh is the default, but Bash should still be installed for compatibility reasons. Also a lot of the basics are the same between zsh/bash. You can access the terminals like described above.

On **Windows**, you can either:
* run a virtual Linux machine using WSL (Windows Subsystem for Linux) and quickly test Linux from the CLI
* use Git Bash:
  - Right-click a folder in Explorer and select “Git Bash Here”
  - Open the Start menu, type “Git Bash”, and press Enter


## Some Basic Commands

- **History**  
  `↑` / `↓` to scroll through previous commands

- **Autocomplete**  
  `Tab` to complete file/folder names

- **Listing files**  
  `ls` show files  
  `ls -la` include hidden & permissions

- **Changing directories**  
  `cd <dir>` enter a directory  
  `cd ..` go up one level

- **Creating directories**  
  `mkdir <dir>` make a new directory

- **Removing files and directories**  
  **WARNING:** This is permanent!  
  `rm <file>` delete a file  
  `rm -r <dir>` delete a directory and its contents

- **Moving/Renaming**  
  `mv <source> <destination>` move or rename files/directories

- **Searching**  
  `grep "pattern" <filname>` find text recursively

- **Wildcards**  
  Use `*` in expressions as wildcard:  
  ```bash
  grep -R "import" *.py
  # this will 
  # search (grep) 
  # all python files ("*.py") 
  # recursively (-R) 
  # for a pattern/string ("import") and 
  # return the filename ahd matching lines (default)
  ```

- **Piping**  
  Use `|` to send the output of one command to another, e.g.:  
  `ls | grep 'pattern'`

- **Redirecting output**  
  `command > file` — overwrite (or create) file with output  
  `command >> file` — append output to file

- **Finding files**  
  `find <path> -name "pattern"` — locate files by name (e.g., `find . -name "*.txt"`)

- **Sorting and unique**  
  `sort input.txt | uniq` — sort and remove duplicates

- **Counting lines**  
  `wc -l file.txt` count lines

