# barebones-dotfiles

These are my dotfiles. Use them as you like, at your own risk!

## Installation

Add the following to your `~/.bash_profile`:
```bash
DOTFILES_DIR=$HOME/dev/bash/barebones-dotfiles
for f in $DOTFILES_DIR/.* ;
do
    if [ -f $f ]; then
        source $f;
    fi
done
```
Replace DOTFILES_DIR with the path of folder where you clone this repo.