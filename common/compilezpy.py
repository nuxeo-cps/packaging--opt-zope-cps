##############################################################################
#
# Copyright (c) 2002 Zope Corporation and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################

import logging
import compileall, os, sys

def compile_non_test(dir):
    """Byte-compile all modules except those in test directories."""
    success = compileall.compile_dir(dir, maxlevels=0)
    try:
        names = os.listdir(dir)
    except os.error:
        print "Can't list", dir
        names = []
    names.sort()
    for name in names:
        fullname = os.path.join(dir, name)
        if (name != os.curdir and name != os.pardir and
            os.path.isdir(fullname) and not os.path.islink(fullname) and
            name not in ('tests', 'skins', 'profiles', 'CPS_examples')):
            success = success and compile_non_test(fullname)
    return success

print
print '-'*78
print 'Compiling python modules'
try:
    success = compile_non_test(sys.argv[1])
    success = True
except:
    success = False
    logging.exception("Error while compiling")

if not success:
    print
    print '!' * 78
    print 'There were errors during Python module compilation.'
    print '!' * 78
    print
    sys.exit(1)
