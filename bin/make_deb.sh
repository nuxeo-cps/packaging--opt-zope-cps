# Make a .deb package by expanding the CPS tarball in it
# arguments: the directory to use, e.g, debian/lenny or ubuntu/hardy
if [ -z "$1" ]; then
   echo "Please provide the target .deb skeleton (see README.txt)"
   exit 1
fi

start_wd=$PWD
deb_dir=$1
cps_version=`cat common/CPS-VERSION`
deb_version=`grep Version $deb_dir/DEBIAN/control | sed -e "s/.*[ ]//g"`
user_id=`id -u`
user_grp=`id -g`

# preparations
mkdir -p $deb_dir/opt/cps-3.5/bin $deb_dir/etc/opt/cps-3.5
find $deb_dir/DEBIAN -type f -executable | xargs chmod 755

cd $deb_dir/opt/cps-3.5
echo Unpacking the tarball
tar xzf $start_wd/tarballs/CPS-Standard-$cps_version.tgz
mv CPS-Standard-$cps_version Products

# instance creation script (cannot be in the product itself, because
# has to know where to find mkzopeinstance.py, and that's installation
# dependent
cp $start_wd/common/mkcpsinstance bin
chmod 755 bin/mkcpsinstance

# 3.5.1-rc2 specific
cp $start_wd/common/makecpssite.py Products/CPSDefault/jobs

echo Byte-compiling
python2.4 $start_wd/common/compilezpy.py > /dev/null
echo Copying the instance skeleton
cd $start_wd
cp -r $start_wd/common/zope_instance_skel $deb_dir/etc/opt/cps-3.5/zope-skel

echo "Producing the .deb (version $deb_version)"

chmod -R a+r $deb_dir
sudo chown -R root:root $deb_dir/*
mkdir -p packages/$1
sudo dpkg -b $deb_dir packages/$1

# getting back to normal ownership so that cleaning does not mean
# playing with rm -r as root
sudo chown -R $user_id:$user_grp $deb_dir/*

