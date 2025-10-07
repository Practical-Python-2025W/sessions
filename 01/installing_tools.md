# Setting up our environment

## 0. How to open a Terminal (you will need that for the installation)

If you never worked with the CMD/PowerShell/Bash terminal on your OS read a bit about these command line interfaces when you find the time. Its always useful to know how to navigate through folders or use them for simple tasks etc.
Eg. for Windows:
https://www.thomas-krenn.com/en/wiki/Cmd_commands_under_Windows
Eg. for Mac:
https://mmuratarat.github.io/2020-04-01/bash_shell_tutorial

(Both are a bit to extensive, just pick what you want or ask a LLM.)

### On Windows
- **Method 1**: Press `Win + R`, type `cmd` and press Enter
- **Method 2**: Press `Win + X` and select "Command Prompt" or "Windows PowerShell"
- **Method 3**: Search for "Command Prompt" or "PowerShell" in the Start menu

### On macOS
- **Method 1**: Press `Cmd + Space`, type "Terminal" and press Enter
- **Method 2**: Go to Applications → Utilities → Terminal


## 1. Download & Install VS-Code
1. Download your installer from [the official website](https://code.visualstudio.com/).
2. Run the installer. The default settings should be fine.



## 2. Download & Install GIT
### !Check if Git is installed first!
Open a terminal, type the following and hit enter.
```bash
git --version
```
If Git is installed, you'll see something like `git version 2.x.x`. If not, you'll get an error message saying the command is not found. If git is installed, you 'don't need to reinstall it.

### Installation on Linux 
It should be installed. If not: I guess you know what to do.

### Installation on Windows
1. Download GIT for Windows from [the official page](https://git-scm.com/downloads/win).
2. Run the installer. Most of the defaults should work, check [Configuration during the installation](#configuration-during-the-installation) for some exceptions.
3. After installation, open a new terminal and verify the installation with `git --version`.
4. Great! Now jump to [Configuration after the installation](#configuration-after-the-installation)

### Installation on macOS
- **Method 1**: Install using Homebrew. Open a terminal and type
  ```bash
  brew install git
  ```
- **Method 2**: Download from [the official page](https://git-scm.com/downloads/mac) and run the installer. Most of the defaults should work, check [Configuration during the installation](#configuration-during-the-installation) for some exceptions.


*After the installation jump to [Configuration after the installation](#configuration-after-the-installation)*


### Configuration during the installation
1. While most of the defaults are alright we have to make VS-Code our default editor for git:

![choosing vs code as default text editor for git](git_1.png "default editor")

2. We should also follow the currently more common convention and name our default branch "main":

![choosing default branch name "main"](git_2.png "default branch")

If you run the installation in the terminal on mac or linux you can change the defaults by using the following commands after finishing the installation.
```bash
git config --global core.editor "code"
```
and
```bash
git config --global init.defaultBranch "main"
```
### Verify Installation
After installing Git on any platform, open a new terminal and run:
```bash
git --version
```
You should see the Git version number if the installation was successful.

### Configuration after the installation
After we installed git, we should make some really basic configurations. These are necessary to let other people know who altered something in a github repository.
1. set the default user name. Just use your github user name for now. 
```bash
git config --global user.name "Alice Bob"
```
2. We also need to add a default email address. Just use the one you created your github account with.
```bash
git config --global user.email "alice@example.com"
```

If you forgot you could check your settings by typing 
```bash
git config --global user.name
```
etc.


## 3. Download & Install Python

### Check if & which python is installed
You should be running something like Python 3.10.3. Everything that has a 3 at the beginning is fine for us. (Version 2 is old and different in a lot of aspects. We will stick with 3.)
#### On Linux
Open a terminal and run:
```bash
python3 --version
```
If that returns an error, try:
```bash
python --version
```

#### On macOS
Open the Terminal and run:
```bash
python3 --version
```

#### On Windows
Open Command Prompt or PowerShell and run:
```powershell
python --version
```
Or use the Python launcher:
```powershell
py --version
```

### Did this result in an error? Then install python please. 
On MacOs and Linux you are on your own. Keep in mind, that running multiple Python versions on one system might lead to problems. Aks me, if you run into difficulties.
#### On Windows
1. Download Python from [the official website](https://www.python.org/downloads/windows/).
2. Run the installer.
3. Make sure that Python is added to path.

![Add Python to path](python_1.png "adding python to path")

4. Click on "Install Now" (the defaults should be fine.)

![Start the installation by clicking on "Install Now"](python_2.png "starting the installation")
