#!/bin/sh
bin/get_tarball.sh

# debs that are common among distributions
bin/clean.sh deb/common
bin/make_deb.sh deb/common
cd ..
bin/include_deb.sh opt-debian lenny cps-3.5/packages/deb/common/current.deb
bin/include_deb.sh opt-ubuntu karmic cps-3.5/packages/deb/common/current.deb
