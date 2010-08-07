This directory for the opt-zope-cps-3.5 packages

Directories
-----------

bin/                     packaging scripts
common/                  resources that are shared among different distros
deb/                     deb package skeletons
deb/common               the common deb package skeleton to spawn most variants


Commands
--------
All commands are meant to be launched from the directory where this
README lies:

bin/build.sh             builds everything (calls sudo)
bin/get_tarball.sh       retrieve the current CPS tarball
bin/make_deb.sh <dir>    create the .deb for skeleton at <dir> (calls sudo)
                         example: bin/make_deb.sh debian/lenny
bin/clean.sh <dir>       cleans intermediate files generated during the
                         release process for <dir>


