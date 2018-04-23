# Script generated with Bloom
pkgdesc="ROS - tf2 is the second generation of the transform library, which lets the user keep track of multiple coordinate frames over time. tf2 maintains the relationship between coordinate frames in a tree structure buffered in time, and lets the user transform points, vectors, etc between any two coordinate frames at any desired point in time."
url='http://www.ros.org/wiki/tf2'

pkgname='ros-kinetic-tf2'
pkgver='0.6.1_0'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('console-bridge'
'ros-kinetic-catkin>=0.5.68'
'ros-kinetic-geometry-msgs'
'ros-kinetic-rostime'
'ros-kinetic-tf2-msgs'
)

depends=('console-bridge'
'ros-kinetic-geometry-msgs'
'ros-kinetic-rostime'
'ros-kinetic-tf2-msgs'
)

conflicts=()
replaces=()

_dir=tf2
source=()
md5sums=()

prepare() {
    cp -R $startdir/tf2 $srcdir/tf2
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

