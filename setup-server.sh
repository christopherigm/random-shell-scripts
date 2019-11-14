#! /bin/bash

# Server initial setup
sudo apt update
sudo apt -y upgrade

sudo apt -y install supervisor python3 nginx postgresql postgresql-contrib postgis
sudo apt -y install libpq-dev python-dev python3-dev build-essential python-setuptools postgresql-server-dev-all

echo "alias python=python3" >> ~/.bashrc
echo "alias pip=pip3" >> ~/.bashrc

git clone https://github.com/tj/n.git
cd n
sudo make install
sudo n 10.13.0
cd ..
sudo rm -rf n

wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
rm get-pip.py

sudo pip install virtualenv
sudo pip install virtualenvwrapper

echo "VIRTUALENVWRAPPER_PYTHON=/usr/bin/python" >> ~/.bashrc
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

. ~/.bashrc

ssh-keygen
cat ~/.ssh/id_rsa.pub
