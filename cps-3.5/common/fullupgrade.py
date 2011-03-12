# Copyright (c) 2010 Georges Racinet <http://www.racinet.fr>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.
#
# $Id$
"""Upgrade a CPS Site.

This applies all relevant upgrade steps and doesn't replay any profile by
default.
Note that upgrade steps can themselves alter the configuration of technical
objects.

With no argument, this will replay the upgrade steps whose target is the current
version (useful for RC process, in-between versions upgrades etc.)
"""

import logging
import sys

import transaction
from Products.CPSUtil import cpsjob
logger = logging.getLogger('CPSDefault.jobs.fullupgrade')

def upgrade(portal, category='cpsplatform'):
    stool = portal.portal_setup
    upgrades = stool.listUpgrades()
    ids = [up['id'] for up in upgrades]
    stool.doUpgrades(ids, category, do_commit=True)

    logger.warn("Upgrade steps for category %r done. Portal %r marked as "
                "upgraded up to %s", category, portal.getId(),
                '.'.join([str(x) for x in stool._getCurrentVersion(category)]))

def main():
    """CPS job bootstrap"""

    optparser = cpsjob.optparser
    optparser.add_option('-m', '--replay-meta-profiles', dest='meta_profiles',
                         action='store_true',
                         help="Replay meta profiles first")
    optparser.add_option('--debian-version-scheme', dest='debian_versions',
                         action='store_true',
                         help="use debian package version scheme")
    portal, options, arguments = cpsjob.bootstrap(app)

    if arguments:
        from_version = arguments[0]
        logger.info("Starting upgrades. Previous version of package: %r "
                    "The current upgrade logic is currently independent of "
                    "that version number, inf favor of the information "
                    "stored in ZODB (as in portal_setup tool ZMI view)"
                    "instead.", from_version)

    upgrade(portal)

if __name__ == '__main__':
    main()
