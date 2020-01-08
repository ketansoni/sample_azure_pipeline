#!/bin/bash

cd /tmp
rm -rf $1
echo Creating Directory: "$1"
mkdir $1
touch $1/test.txt
echo "hello world" >> $1/test.txt

