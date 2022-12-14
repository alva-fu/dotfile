# Get Linux system information in terminal with neofetch
neofetch

# Configurations of brew (package manager for MacOS or Linux)
# Homebrew configuration should load first.
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ]; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ]; then
    PATH="$HOME/.local/bin:$PATH"
fi

# Configurations of pyenv (version manager of python)
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Configuration of composer
export PATH="$HOME/.config/composer/vendor/bin:$PATH"
