sudo sed -i 's/jessie/stretch/g' /etc/apt/sources.list
sudo sed -i 's/jessie/stretch/g' /etc/apt/sources.list.d/raspi.list
sudo apt-get update
sudo apt-get -y dist-upgrade
sudo apt-get install -y fonts-droid-fallback
sudo apt-get autoremove
sudo reboot