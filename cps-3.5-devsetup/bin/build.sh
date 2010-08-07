#!/bin/sh
bin/make_deb.sh deb/common
cd ..
bin/include_deb.sh opt-debian lenny cps-3.5-devsetup/packages/deb/common/current.deb
bin/include_deb.sh opt-ubuntu karmic cps-3.5-devsetup/packages/deb/common/current.deb
