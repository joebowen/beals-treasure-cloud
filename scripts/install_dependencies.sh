#!/bin/bash

apt-get update
apt-get install libmpc-dev libmpfr-dev libgmp3-dev
pip install  -r '../requirements.txt'
