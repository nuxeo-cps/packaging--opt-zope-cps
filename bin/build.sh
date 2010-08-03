#!/bin/sh
sudo bin/clean.sh
bin/get_tarball.sh
sudo bin/make_deb.sh debian/lenny
