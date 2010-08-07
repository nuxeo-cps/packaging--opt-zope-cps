#!/bin/sh
bin/get_tarball.sh

# debs that are common among distributions
bin/clean.sh deb/common
bin/make_deb.sh deb/common
bin/include_deb.sh opt-debian lenny packages/deb/common/current.deb
bin/include_deb.sh opt-ubuntu karmic packages/deb/common/current.deb
