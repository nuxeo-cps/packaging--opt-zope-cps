# Make a .deb package by expanding the CPS tarball in it
# arguments: the directory to use, e.g, debian/lenny or ubuntu/hardy
if [ -z "$1" ]; then
   echo "Please provide the target .deb skeleton (see README.txt)"
   exit 1
fi

start_wd=$PWD
deb_dir=$1
user_id=`id -u`
user_grp=`id -g`

mkdir -p packages/$deb_dir
chmod -R a+r $deb_dir

sudo chown -R root:root $deb_dir
dpkg -b $deb_dir packages/$deb_dir/current.deb
sudo chown -R $user_id:$user_grp $deb_dir
