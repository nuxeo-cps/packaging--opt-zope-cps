This repository holds the files used to generate packages for various
operating systems. It must stay light.

One should be able to regenerate packages simply by using hg up and
at most correcting some download URLs.

Directories
-----------

cps-3.5/                 resources for opt-zope-cps-3.5
cps-3.5-dev-setup/       resources for opt-zope-cps-3.5
bin/                     utilities shared among packages
repos/                   package systeme repositories

Being started
-------------
Make repos/deb a link to your local apt repository

Commands
--------
All commands are meant to be launched from the directory where this
README lies:

bin/include_deb.sh       includes a deb in the local repo
