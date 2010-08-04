This repository holds the files used to generate packages for various
operating systems. It must stay light.

One should be able to regenerate packages simply by using hg up and
at most correcting some download URLs.

Directories
-----------

bin/                     packaging scripts
common/                  resources that are shared among different distros
debian/xxx               .deb skeleton for debian version xxx
ubuntu/xxx               .deb skeleton for ubuntu version xxx

Commands
--------
All commands are meant to be launched from the repository root

bin/build.sh             builds everything (calls sudo)
bin/get_tarball.sh       retrieve the current CPS tarball
bin/make_deb.sh <dir>    create the .deb for skeleton at <dir> (calls sudo)
                         example: bin/make_deb.sh debian/lenny


