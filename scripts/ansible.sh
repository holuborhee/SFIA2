#!/bin/bash

mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
sudo chown -R $(whoami):$(whoami) ~/*
source ~/.bashrc

sudo pip3 install --user ansible