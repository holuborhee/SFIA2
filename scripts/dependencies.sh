#!/bin/bash

sudo apt-get update
sudo apt-get -y upgrade
sudo apt install -y python3 python3-pip

cd service1
python3 create.py
cd ..