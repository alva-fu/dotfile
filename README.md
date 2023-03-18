# Alva's dotfiles

## Shell setup

### macOS & Linux

1. Clone this repo to `$HOME`

    ```sh
    cd
    git clone git@github.com:alva-fu/dotfile.git ~/.dotfile
    ```

2. Install [Homebrew](https://brew.sh/)

   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. Install the packages below:

    - [fish shell](https://fishshell.com/), [exa](https://the.exa.website/), [tree-sitter](https://tree-sitter.github.io/), and [peco](https://github.com/peco/peco)

        ```sh
        brew install fish
        brew install exa
        brew install tree-sitter
        brew install peco
        ```

4. Start up fish and install [fisher](https://github.com/jorgebucaran/fisher)

    ```sh
    curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher install jorgebucaran/fisher
    ```

5. Install the plugins below:

    - [tide](https://github.com/IlanCosman/tide), [z](https://github.com/jethrokuan/z), and [nvm](https://github.com/jorgebucaran/nvm.fish)

        ```sh
        fisher install ilancosman/tide@v5
        fisher install jethrokuan/z
        fisher install jorgebucaran/nvm.fish
        ```

6. Configure shell theme with `tide configure`

7. Restart the terminal

8. Make symbolic links to config files

    ```sh
    ln -s $HOME/.dotfile/config/fish/config.fish $HOME/.config/fish/config.fish; \
    ln -s $HOME/.dotfile/config/fish/config-linux.fish $HOME/.config/fish/config-linux.fish; \
    ln -s $HOME/.dotfile/config/fish/config-osx.fish $HOME/.config/fish/config-osx.fish; \
    ln -s $HOME/.dotfile/config/fish/conf.d/tide.fish $HOME/.config/fish/conf.d/tide.fish; \
    ln -s $HOME/.dotfile/config/fish/functions/fish_user_key_bindings.fish $HOME/.config/fish/functions/fish_user_key_bindings.fish; \
    ln -s $HOME/.dotfile/config/fish/functions/peco_change_directory.fish $HOME/.config/fish/functions/peco_change_directory.fish; \
    ln -s $HOME/.dotfile/config/fish/functions/peco_select_history.fish $HOME/.config/fish/functions/peco_select_history.fish; \
    ```
