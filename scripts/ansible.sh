#!/bin/bash

mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc

sudo pip3 install --user ansible
ansible --version

sudo ansible-playbook -i inventory.cfg playbook.yaml