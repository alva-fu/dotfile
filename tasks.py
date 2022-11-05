from invoke import task


@task(
    name="BuildZsh",
    help={
        "plugins": "Install the autosuggestions, completions and highlightings plugins.",
        "theme": "Install the powerlevel10k theme."
    }
)
def BuildZsh(context, plugins=False, theme=False):
    """
    Installing "Oh My Zsh", and plugins or theme optionally.
    """

    commands = {
        "install_omz": "sh -c '$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)'",
        "zsh_autosuggestions": "git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions",
        "zsh_completions": "git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting",
        "zsh_highlighting": "git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting",
        "zsh_powerlevel10k": "git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"
    }

    # Install Oh My Zsh.
    context.run(commands["install_omz"])

    # Install zsh plugins.
    if plugins:
        context.run(commands["zsh_autosuggestions"])
        context.run(commands["zsh_completions"])
        context.run(commands["zsh_highlighting"])

    # Install powerlevel10k theme.
    if theme:
        context.run(commands["zsh_powerlevel10k"])


@task(
    name="MakeSoftlink",
    help={
        "zshrc": "Backup the original $HOME/.zshrc file which will be renamed to .zshrc_backup, and make a softlink to $HOME/.dotfiles/zsh/.zshrc.",
        "zprofile": "Backup the original $HOME/.zprofile file which will be renamed to .zprofile_backup, and make a softlink to $HOME/.dotfiles/zsh/.zprofile."
    }
)
def MakeSoftlink(context, zshrc=False, zprofile=False):
    """
    Making softlinks of $HOME/.zshrc or $HOME/.zprofile.
    """

    if zshrc == False and zprofile == False:
        print("No softlink made.")
        return

    # Make softlink of $HOME/.zshrc.
    if zshrc:
        context.run('mv $HOME/.zshrc $HOME/.zshrc_backup')
        context.run('ln -s $HOME/.dotfiles/zsh/.zshrc $HOME/.zshrc')

    # Make softlink of $HOME/.zprofile.
    if zprofile:
        context.run('mv $HOME/.zprofile $HOME/.zprofile_bachup')
        context.run('ln -s $HOME/.dotfiles/zsh/.zprofile $HOME/.zprofile')


@task(
    name="InstallFont",
    help={
        "cascadia-code": "Install the CascadiaCode font.",
        "fira-code": "Install the FiraCode font.",
        "meslo": "Install the Meslo font."
    }
)
def InstallFont(context, cascadia_code=False, fira_code=False, meslo=False):
    """
    Install the selected "Nerd Fonts".
    """

    if cascadia_code == False and fira_code == False and meslo == False:
        print("No font installed.")
        return

    if cascadia_code and fira_code and meslo:
        context.run(
            'mkdir -p $HOME/.local/share/fonts/truetype/ $HOME/.local/share/fonts/opentype/')
        context.run(
            'cp -r $HOME/.dotfiles/font/CascadiaCode/ $HOME/.local/share/fonts/opentype/')
        context.run(
            'cp -r $HOME/.dotfiles/font/FiraCode/ $HOME/.local/share/fonts/truetype/')
        context.run(
            'cp -r $HOME/.dotfiles/font/Meslo/ $HOME/.local/share/fonts/truetype/')
        context.run('fc-cache -f -v')
        return

    # Install fonts
    if cascadia_code:
        context.run('mkdir -p $HOME/.local/share/fonts/truetype/')
        context.run(
            'cp -r $HOME/.dotfiles/font/CascadiaCode/ $HOME/.local/share/fonts/truetype/')
        context.run('fc-cache -f -v')

    if fira_code:
        context.run('mkdir -p $HOME/.local/share/fonts/truetype/')
        context.run(
            'cp -r $HOME/.dotfiles/font/FiraCode/ $HOME/.local/share/fonts/truetype/')
        context.run('fc-cache -f -v')

    if meslo:
        context.run('mkdir -p $HOME/.local/share/fonts/truetype/')
        context.run(
            'cp -r $HOME/.dotfiles/font/Meslo/ $HOME/.local/share/fonts/truetype/')
        context.run('fc-cache -f -v')


@task(name="BuildVim")
def BuildVim(context):
    """
    Customize vim code editor.
    """
    context.run('rm -rf $HOME/.vim/')
    context.run('ln -s $HOME/.dotfiles/vim/ $HOME/.vim')
    context.run(
        'mkdir -p ~/.vim ~/.vim/autoload ~/.vim/backup ~/.vim/colors ~/.vim/plugged')
    context.run('ln -s $HOME/.dotfiles/vim/.vimrc $HOME/.vimrc')
