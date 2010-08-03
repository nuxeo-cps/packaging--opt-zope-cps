#!/bin/sh

mkdir -p tarballs
cd tarballs

# retrieval
cps_version=3.5.1-rc2
tarball_name=CPS-Standard-$cps_version.tgz

url=http://download.cps-cms.org/CPS-$cps_version/$tarball_name
#wget $url
wget $url.sig
wget $url.md5

# integrity checks
echo Checking MD5
md5sum -c - < $tarball_name.md5
echo Checking PGP
gpg --check-sig $tarball_name
