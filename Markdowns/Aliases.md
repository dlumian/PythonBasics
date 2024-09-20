# Efficient Development with Aliases

Aliases are a powerful way to streamline development process. Aliases typically shorter common commands or provide a more memorable command.

Aliases are defined in your shell configuration file (e.g., `.bashrc`, `.zshrc`) to allow you to execute complex or repetitive commands with simple keywords, saving time during development.

Example alias definition:
```bash
alias <shortcut>='<command>'
```
Once the file is updated, `source` must be run for effects to take effect:
```bash
source ~/.zshrc  # For zsh users
source ~/.bashrc  # For bash users
```

Updates can also be applied with a restart.

Without this, commands will not be available.

<span style="color:red">**WARNING:** Be careful not to override existing commands. This can result in unexpected behaviors.</span>

## Common Aliases for Development

### 1. **Navigate to a Specific Directory**
Instead of typing the full path to a directory, you can create an alias to jump to frequently used locations:

```bash
alias proj='cd ~/path/to/your/project'
alias docs='cd ~/Documents'
alias repos='cd ~/Documents/GitHub'
```
### 2. **Common List Operations**
The `ls` command doesn’t show hidden files (those that start with a `.`) by default. You can create an alias to always show hidden files:

```bash
alias ll='ls -la'  # Long listing format, including hidden files
alias ls='ls -G'  # Add colors to `ls` output
```

### 3. **Get the Current Date and Time**
Print the current date and time with a quick command:

```bash
alias now='date "+%Y-%m-%d %H:%M:%S"'
```

### 4. **Update and Upgrade Packages**
Alias examples for updating and upgrading packages:

For macOS with Homebrew:

```bash
alias brewup='brew update && brew upgrade'
```

For Ubuntu:
```bash
alias update='sudo apt update && sudo apt upgrade -y'
```

### 5. **Open Files or Directories in VS Code**
Open files or directories with `code`:

```bash
alias codeproj='code ~/path/to/your/project'
```

### 6. **Show Disk Usage**
View the disk usage of a directory in a human-readable format:

```bash
alias duh='du -h --max-depth=1'
```

### 7. **Extract Compressed Files**
Create a quick alias for extracting different types of compressed files (`.tar`, `.gz`, `.zip`, etc.):

```bash
alias extract='tar -xzvf'
alias unzipit='unzip -d'
```

### 8. **Commonly Used Git Commands**
Git commands can be long, so here are some helpful aliases to speed things up:

```bash
alias gs='git status'
alias ga='git add .'
alias gc='git commit -m'
alias gp='git push'
alias gl='git pull'
```

### 9. **Reboot or Shutdown System (Linux/macOS)**

```bash
alias rebootnow='sudo reboot'
alias shutdownnow='sudo shutdown -h now'
```

## Key Aliases for Python Development

### 1. **Alias for Activating a Virtual Environment**
Activate a commonly used virtual environment.

For virtual environments:
```bash
alias venv='source ~/path/to/your/env/bin/activate'
```
For conda environments:
```bash
alias cenv='conda activate cenv_name'
```

### 2. **Conda Environment Setup**
Automate the creation and activation of a conda environment with a specific Python version.

```bash
alias mkconda='conda create -n dev_env python=3.11 -y && conda activate dev_env'
```
This will create and activate a new conda environment named `dev_env`.

### 3. **Alias for Running Python Scripts**
Instead of typing `python3` every time, shorten the command.

```bash
alias py='python3'
```

### 4. **Alias for Running Unit Tests**
This alias runs tests using `pytest` in your project directory.

```bash
alias test='pytest tests/'
```
You can also specify detailed test output or generate reports:

```bash
alias testv='pytest -v tests/'  # Verbose output
alias cov='pytest --cov=your_package tests/'  # Coverage report
```

### 5. **Building and Uploading Python Packages**
For package development, building and uploading packages to PyPI or Test PyPI are common tasks. This alias simplifies both:

```bash
alias buildpkg='python setup.py sdist bdist_wheel'
alias uploadtest='twine upload --repository testpypi dist/*'
alias uploadpypi='twine upload dist/*'
```

### 6. **Alias for Formatting with `black`**
For Python code formatting, using `black` is common. This alias auto-formats all Python files in your current directory.

```bash
alias fmt='black .'
```

### 7. **Running Flake8 for Linting**
For quick linting to check for PEP 8 compliance.

```bash
alias lint='flake8 your_package/'
```

### 8. **Clean Build Artifacts**
After building a package, you often want to clean up build artifacts such as `.pyc` files or `dist/` directories.

```bash
alias cleanbuild='rm -rf build/ dist/ *.egg-info'
alias cleanpyc='find . -name "*.pyc" -exec rm -f {} \;'
```

### 9. **Push Changes to GitHub**
For frequent `git` users, shorten push commands for a faster workflow.

```bash
alias gp='git push origin main'
alias gc='git commit -m'
alias gs='git status'
```

### 10. **Docker Aliases for Python Development**
If you use Docker for Python development, here are some handy aliases to run containers or build images quickly:

```bash
alias dcup='docker-compose up -d'
alias dcdown='docker-compose down'
alias dcb='docker-compose build'
```

### 11. **Install Dependencies from `requirements.txt` or `environment.yml`**
Quickly install dependencies with these aliases.

```bash
alias pipi='pip install -r requirements.txt'
alias condaenv='conda env create -f environment.yml && conda activate dev_env'
```

### 12. **Running Jupyter Notebooks**
If you frequently work with Jupyter notebooks, this alias starts the notebook server:

```bash
alias nb='jupyter notebook'
```

## Using Aliases in Practice

### Example Development Cycle with Aliases

1. **Set up your environment:**
   ```bash
   mkconda
   ```

2. **Run tests and linting:**
   ```bash
   test
   lint
   ```

3. **Format your code:**
   ```bash
   fmt
   ```

4. **Build and upload to Test PyPI:**
   ```bash
   buildpkg
   uploadtest
   ```

5. **Push changes to GitHub:**
   ```bash
   gc "Fixed tests and pushed final changes"
   gp
   ```

## Summary

Aliases can greatly speed up development by reducing the time spent typing out long commands, especially for repetitive tasks. By integrating these aliases into your workflow, you’ll be able to focus more on coding and less on managing your development environment.
