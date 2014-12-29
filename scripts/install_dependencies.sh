#!/bin/bash

sudo apt-get update
sudo apt-get install libmpc-dev libmpfr-dev libgmp3-dev
pip install  -r '../requirements.txt'
