#!/usr/bin/fakeroot /usr/bin/python
import os
import shutil
from subprocess import call
from optparse import OptionParser

optparser = OptionParser()
optparser.add_option('--source-dir', help="Source directory for CPS Products")
optparser.add_option('--dest-dir', help="Directory to store the produced .deb")
optparser.add_option('--pkg-skeleton',
                     help="Directory holding the package skeleton, "
                     "including control files.")
optparser.add_option('--sandbox-dir', help="Where to build the package itself.")

class DebianBuilder(object):

    def __init__(self, options, arguments):
        for k, v in options.__dict__.items():
            setattr(self, k, v)
        self.arguments = arguments

    def read_version(self):
        """Read the version string as produced by hgbundler in products dir.
        """
        vfile = open(os.path.join(self.source_dir, 'version.txt'))
        vstring = vfile.readline().strip()
        assert vstring.startswith('CPS-')
        self.version_str = vstring[4:]
        self.version = tuple(int(i) for i in self.version_str.split('.'))
        self.major_version = '.'.join((str(i) for i in self.version[:2]))

    def update_control(self):
        """Update the version in control file and set it on self."""
        path = os.path.join(self.build_dir, 'DEBIAN', 'control')
        control = open(path)
        lines = control.readlines()
        control.close()

        prefix = 'Version: '
        for i, line in enumerate(lines):
            if line.startswith(prefix):
                line = line % self.version_str
                lines[i] = line
                self.deb_version = line[len(prefix):].strip()

        control = open(path, 'w')
        control.write(''.join(lines))
        control.close()

    def do_copies(self):
        shutil.copytree(self.pkg_skeleton, self.build_dir, symlinks=True)
        products_dest = os.path.join(self.build_dir, 'opt',
                                     'cps-%s' % self.major_version, 'Products')
        shutil.copytree(self.source_dir, products_dest, symlinks=True)

    def clean(self):
	if os.path.exists(self.build_dir):
            shutil.rmtree(self.build_dir)

    def build(self):
        self.read_version()
        call(['mkdir', '-p', options.sandbox_dir], shell=True)

        self.build_dir = os.path.join(options.sandbox_dir, self.version_str)

        self.clean() 
        self.do_copies()
        self.update_control()
        call('dpkg -b %s opt-zope-cps-3.5_%s_all.deb' % (self.build_dir, self.deb_version), shell=True)


if __name__ == '__main__':
    options, arguments = optparser.parse_args()
    builder = DebianBuilder(options, arguments)
    builder.build()
