# Script generated with Bloom
pkgdesc="ROS - KDL binding for tf2"
url='http://ros.org/wiki/tf2'

pkgname='ros-lunar-tf2-kdl'
pkgver='0.5.17_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('eigen3'
'ros-lunar-catkin>=0.5.68'
'ros-lunar-cmake-modules'
'ros-lunar-orocos-kdl'
'ros-lunar-rostest'
'ros-lunar-tf2'
'ros-lunar-tf2-ros'
)

depends=('eigen3'
'ros-lunar-orocos-kdl'
'ros-lunar-tf2'
'ros-lunar-tf2-ros'
)

conflicts=()
replaces=()

_dir=tf2_kdl
source=()
md5sums=()

prepare() {
    cp -R $startdir/tf2_kdl $srcdir/tf2_kdl
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

