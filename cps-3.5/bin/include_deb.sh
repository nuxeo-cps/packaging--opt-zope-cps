#!/bin/sh
if [ -z "$1" ]; then
   echo "Sample usage: $0 opt-ubuntu lucid mypackage.deb"
   exit 1
fi

reprepro --ignore=undefinedtarget -Vb repos/deb/$1 includedeb $2 $3
