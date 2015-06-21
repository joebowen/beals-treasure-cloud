#!/bin/bash

cd ~/app-root/runtime/repo

rm -rf beals-treasure-cloud

git clone https://github.com/joebowen/beals-treasure-cloud.git

cp -r beals-treasure-cloud/* ~/app-root/runtime/repo/
