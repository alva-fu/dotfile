# Check if exa is installed for making aliases
if type -q exa
  alias ll "exa -l -g --icons"
  alias lla "ll -a"
end

# Check if nvim is installed for making aliases
if type -q nvim
  alias vim nvim
  set -gx EDITOR nvim
end

# Load pyenv
if [ -d "$HOME/.pyenv" ]
  set -gx PYENV_ROOT $HOME/.pyenv
  set -gx PATH $PYENV_ROOT/bin $PATH
  pyenv init - | source
end