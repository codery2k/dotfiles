#!/usr/bin/env bash

cd Downloads || exit

# chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

sudo apt update && sudo apt upgrade

sudo apt-get install apt-transport-https

sudo apt install -y vanilla-gnome-desktop

# sudo apt install -y numix-icon-theme
sudo apt install -y gnome-tweak-tool
# https://chrome.google.com/webstore/detail/gnome-shell-integration/gphhapmejobijbbhgpjhcjognlahblep
# https://extensions.gnome.org/extension/615/appindicator-support/
# https://extensions.gnome.org/extension/1401/bluetooth-quick-connect/
# https://extensions.gnome.org/extension/307/dash-to-dock/
# https://extensions.gnome.org/extension/442/drop-down-terminal/
# https://extensions.gnome.org/extension/1253/extended-gestures/
# https://extensions.gnome.org/extension/120/system-monitor/
# https://extensions.gnome.org/extension/21/workspace-indicator/

sudo apt-get install -y build-essential curl file git locate tree adb

#  homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# thefuck
brew install thefuck

# npm, node
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
nvm install --lts

# TODO add py, other languages, development requirements

# sublime
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update && sudo apt install -y sublime-text

# vscode
sudo apt install vscode

# syncthing
sudo curl -s -o /usr/share/keyrings/syncthing-archive-keyring.gpg https://syncthing.net/release-key.gpg
echo "deb [signed-by=/usr/share/keyrings/syncthing-archive-keyring.gpg] https://apt.syncthing.net/ syncthing stable" | sudo tee /etc/apt/sources.list.d/syncthing.list
printf "Package: *\nPin: origin apt.syncthing.net\nPin-Priority: 990\n" | sudo tee /etc/apt/preferences.d/syncthing
sudo apt update && sudo apt install syncthing syncthing-gtk

# notable
# download from https://github.com/notable/notable-insiders/releases
# sudo dpkg -i notable_1.9.0-beta.0_amd64.deb

# taskboard
https://chrome.google.com/webstore/search/taskboard

# mailspring
sudo snap install mailspring

# skype
sudo snap install --classic skype

# chrome-beta
sudo apt install google-chrome-beta

# toggl
flatpak install flathub com.toggl.TogglDesktop

# proton vpn
sudo apt install -y openvpn dialog python3-pip python3-setuptools
sudo pip3 install protonvpn-cli

# joplin
wget -O - https://raw.githubusercontent.com/laurent22/joplin/master/Joplin_install_and_update.sh | bash

# vlc
sudo apt install -y vlc

# telegram
sudo snap install telegram-desktop

# calibre
sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin

# webtorrent
# download from https://webtorrent.io/desktop-download/linux

# foliate
snap install foliate

# TODO :{
# shortcuts

# - bluetooth CA+b

# - workspacer -> awesomewm/tiling window manager
# }

# gitlab cli
curl -s https://raw.githubusercontent.com/zaquestion/lab/master/install.sh | sudo bash

# github cli
brew install gh

# gdebi
sudo apt install gdebi
