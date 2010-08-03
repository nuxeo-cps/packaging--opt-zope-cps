# Make a .deb package by expanding the CPS tarball in it
# arguments: the directory to use, e.g, debian/lenny or ubuntu/hardy
start_wd=$PWD
deb_dir=$1
cps_version=`cat common/CPS-VERSION`

mkdir -p $deb_dir/opt

cd $deb_dir/opt
tar xzf $start_wd/tarballs/CPS-Standard-$cps_version.tgz
python2.4 $start_wd/common/compilezpy.py > /dev/null
cp -r $start_wd/zope-instance_skel $deb_dir/etc/opt/cps-3.5/skel
