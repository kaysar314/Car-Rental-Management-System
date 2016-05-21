#!/usr/bin/env sh
export XMODIFIERS="@im=fcitx"
export GTK_IM_MODULE="fcitx"
export QT_IM_MODULE="fcitx"
/usr/bin/wpp "$1"
