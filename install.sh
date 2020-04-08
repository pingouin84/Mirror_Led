#!/bin/bash

echo ""
echo "Installation des packet"
sudo apt-get -y install python3 python3-dev python3-pip
sudo apt-get install libsdl2-2.0-0 libsdl2-image-2.0-0 libsdl2-mixer-2.0-0 libsdl2-ttf-2.0-0

echo ""
echo "Installation des dépendances python"
pip3 install -r requirements.txt

echo ""
echo "Copy dans .config/autostart"
cp ~/Mirror_Led/Mirror_led.desktop ~/.config/autostart/Mirror_led.desktop