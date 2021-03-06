#!/bin/sh

cps_version=`cat common/CPS-VERSION`
mkdir -p tarballs
cd tarballs

# retrieval
tarball_name=CPS-Standard-$cps_version.tbz
if [ -f $tarball_name ]; then
  echo "Tarball already there, no download"
else
  url=http://download.cps-cms.org/CPS-$cps_version/$tarball_name
  wget $url
  wget $url.asc
  wget $url.md5
fi

# integrity checks
echo Checking MD5
md5sum -c - < $tarball_name.md5
echo Checking PGP
gpg --verify $tarball_name.asc
