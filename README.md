# Alva's dotfiles

## Getting Started

1. Clone this repo to `$HOME`

    ```sh
    cd
    git clone git@github.com:alva-fu/dotfile.git ~/.dotfile
    ```

2. Install [Homebrew](https://brew.sh/)

   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

### Shell Setup

#### macOS & Ubuntu

1. Install the packages below:

    - [fish shell](https://fishshell.com/), [exa](https://the.exa.website/), [tree-sitter](https://tree-sitter.github.io/), and [peco](https://github.com/peco/peco)

        ```sh
        brew install fish exa tree-sitter peco
        ```

2. Start up fish shell and install the plugin manager [fisher](https://github.com/jorgebucaran/fisher)

    ```sh
    curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher install jorgebucaran/fisher
    ```

3. Install the plugins below:

    - [tide](https://github.com/IlanCosman/tide), [z](https://github.com/jethrokuan/z), and [nvm](https://github.com/jorgebucaran/nvm.fish)

        ```sh
        fisher install ilancosman/tide@v5
        fisher install jethrokuan/z
        fisher install jorgebucaran/nvm.fish
        ```

4. Configure shell theme via `tide configure` command

5. Restart the terminal

6. Symlinks the config files into `~/.config/fish`

    ```sh
    ln -s $HOME/.dotfile/config/fish/config.fish $HOME/.config/fish/config.fish; \
    ln -s $HOME/.dotfile/config/fish/config-linux.fish $HOME/.config/fish/config-linux.fish; \
    ln -s $HOME/.dotfile/config/fish/config-osx.fish $HOME/.config/fish/config-osx.fish; \
    ln -s $HOME/.dotfile/config/fish/conf.d/tide.fish $HOME/.config/fish/conf.d/tide.fish; \
    ln -s $HOME/.dotfile/config/fish/functions/fish_user_key_bindings.fish $HOME/.config/fish/functions/fish_user_key_bindings.fish; \
    ln -s $HOME/.dotfile/config/fish/functions/peco_change_directory.fish $HOME/.config/fish/functions/peco_change_directory.fish; \
    ln -s $HOME/.dotfile/config/fish/functions/peco_select_history.fish $HOME/.config/fish/functions/peco_select_history.fish
    ```

### Tmux Setup

_Note_: Requires [tmux](https://github.com/tmux/tmux) >= 3.2a

1. Install `tmux`

    ```sh
    brew install tmux # for macOS
    sudo apt update -y && sudo apt install tmux # for Ubuntu
    ```

2. Symlinks the config files into `~/.config/tmux`

    ```sh
    ln -s $HOME/.dotfile/config/tmux $HOME/.config/tmux
    ```

### Neovim Setup

_Note_: Requires [Neovim](https://neovim.io/) >= 0.8

1. Install `neovim`

    - macOS

        ```sh
        brew install neovim
        ```

    - Ubuntu

        Since the `noevim` of Ubuntu (22.04 LTS) package is < 0.8, it should be installed from source. The details of installation could be found at [Neovim's home page](https://neovim.io/).

        1. Download [nvim-linux64.tar.gz](https://github.com/neovim/neovim/releases/tag/stable)

        2. Extract the tarball

            ```sh
            tar xzvf nvim-linux64.tar.gz
            ```

        3. Install `neovim`

            ```sh
            ./nvim-linux64/bin/nvim
            ```

2. Symlinks the config files into `~/.config/nvim`

    ```sh
    ln -s $HOME/.dotfile/config/nvim $HOME/.config/nvim
    ```