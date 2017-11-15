# Post install setup of powerline fonts

mkdir -p ~/.config/fontconfig/conf.d
cp 10-powerline-symbols.conf ~/.config/fontconfig/conf.d/10-powerline-symbols.conf
fc-cache -vf ~/.fonts

#
