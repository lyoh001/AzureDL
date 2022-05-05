sudo apt-get update && sudo apt-get dist-upgrade -y \
&& wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add - \
&& wget -q https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb \
&& wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
&& wget -q https://github.com/lxylxy123456/cariboublocker/releases/download/auto-release-1ec655a3e8af4888099a78095c16d6bed75ee1fe/3.36.3.zip \
&& wget -q https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh \
&& sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" \
&& sudo apt-get install ./google-chrome-stable_current_amd64.deb -y \
&& sudo apt-get install ./mysql-apt-config_0.8.22-1_all.deb -y \
&& sudo apt-get update && sudo apt-get dist-upgrade -y \
&& sudo apt-get install cifs-utils -y \
&& sudo apt-get install code -y \
&& sudo apt-get install docker.io -y \
&& sudo apt-get install git -y \
&& sudo apt-get install gnome-shell-extensions -y \
&& sudo apt-get install htop -y \
&& sudo apt-get install mysql-workbench-community -y \
&& sudo apt-get install python3.8 -y \
&& sudo apt-get install python3-pip -y \
&& sudo apt-get install python3-venv -y \
&& sudo apt-get install zsh -y \
&& gsettings set org.gnome.settings-daemon.plugins.media-keys home "['<Super>e']" \
&& gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-down "['']" \
&& gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-left "['']" \
&& gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-right "['']" \
&& gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-up "['']" \
&& gsettings set org.gnome.shell.extensions.dash-to-dock click-action "minimize" \
&& gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 64 \
&& gsettings set org.gnome.shell.extensions.dash-to-dock dock-fixed false \
&& gsettings set org.gnome.shell.extensions.dash-to-dock dock-position BOTTOM \
&& gsettings set org.gnome.shell.extensions.dash-to-dock extend-height false \
&& gsettings set org.gnome.shell.extensions.dash-to-dock transparency-mode FIXED \
&& gsettings set org.gnome.shell.extensions.dash-to-dock unity-backlit-items true \
&& gsettings set org.gnome.shell.extensions.desktop-icons show-home false \
&& gsettings set org.gnome.shell.extensions.desktop-icons show-trash false \
&& gnome-extensions install ./3.36.3.zip --force \
&& sudo sh ./install.sh