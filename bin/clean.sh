#!/bin/sh
if [ -z "$1" ]; then
   echo "Please provide the target .deb skeleton (see README.txt)"
   exit 1
fi

rm -r $1/opt
rm -r $1/etc/opt
