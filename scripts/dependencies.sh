#!/bin/bash

sudo apt-get update
sudo apt-get -y upgrade
sudo apt install -y python3 python3-pip

sudo chown -R $(whoami):$(whoami) ~/*
source ~/.bashrc
