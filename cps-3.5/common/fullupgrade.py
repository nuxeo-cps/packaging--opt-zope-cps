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

Relays to the standard cpsupgrade job
This is kept for two reasons:
  - name differs, existing instances will still call the old one ;
  - potential for debian version number usage
"""

import logging
from Products.CPSUtil import cpsjob
from Products.CPSDefault.jobs.cpsupgrade import Upgrader

logger = logging.getLogger('CPSDefault.jobs.fullupgrade')

def upgrade(portal):
    Upgrader(portal, None).apply_all_steps()

def main():
    """CPS job bootstrap"""

    optparser = cpsjob.optparser
    optparser.add_option('--debian-version-scheme', dest='debian_versions',
                         action='store_true',
                         help="use debian package version scheme")
    portal, options, arguments = cpsjob.bootstrap(app)

    if arguments:
        from_version = arguments[0]
        logger.info("Starting upgrades. Previous version of package: %r "
                    "The current upgrade logic is currently independent of "
                    "that version number, in favor of the information "
                    "stored in ZODB (as in portal_setup tool ZMI view).",
                    from_version)

    upgrade(portal)

if __name__ == '__main__':
    main()
