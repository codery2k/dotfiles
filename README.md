# barebones-dotfiles

These are my dotfiles. Use them as you like, at your own risk!

## Installation

Add the following to your `~/.bash_profile`:
```bash
export DOTFILES_DIR=$HOME/dev/bash/barebones-dotfiles
for f in $DOTFILES_DIR/.* ;
do
    if [ -f $f ]; then
        source $f;
    fi
done
```
Replace DOTFILES_DIR with the path of folder where you clone this repo.


## Credits
A massive thank you to [@mathiasbynens](https://github.com/mathiasbynens) and [@webpro](https://github.com/webpro) for uploding their own dotfiles on github (that I'm guilty of blatantly copying in some places) and motivating me to create my own dotfiles project.

You can find their dotfiles at:
* https://github.com/webpro/dotfiles
* https://github.com/mathiasbynens/dotfiles

Additional Resources:
* [.bashrc generator](http://bashrcgenerator.com/)
* [Awesome Dotfiles](https://github.com/webpro/awesome-dotfiles)