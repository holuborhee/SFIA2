#!/bin/bash

mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
sudo chown -R $(whoami):$(whoami) ~/*
source ~/.bashrc

sudo pip3 install --user ansible

source /home/jenkins/.ssh/config
/home/jenkins/.local/bin/ansible-playbook -i inventory.cfg playbook.yaml