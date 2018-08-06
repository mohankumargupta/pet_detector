#!/bin/bash

set -x
sudo apt update
sudo python3 -m pip install --upgrade pip setuptools

#Install Tensorflow
sudo apt install -y libatlas-base-dev
sudo pip3 install tensorflow

#Install OpenCV
sudo apt install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt install -y libxvidcore-dev libx264-dev
sudo apt install -y qt4-dev-tools
sudo pip3 install opencv-python

#Install Protobuf compiler
sudo apt install protobuf-compiler

# Install Tensorflow Object Model API dependencies
sudo apt install -y python3-pil python3-lxml python3-tk cython3
sudo pip3 install jupyter matplotlib



