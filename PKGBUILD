# Script generated with Bloom
pkgdesc="ROS - tf2_msgs"
url='http://www.ros.org/wiki/tf2_msgs'

pkgname='ros-lunar-tf2-msgs'
pkgver='0.5.17_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-actionlib-msgs'
'ros-lunar-catkin'
'ros-lunar-geometry-msgs'
'ros-lunar-message-generation'
)

depends=('ros-lunar-actionlib-msgs'
'ros-lunar-geometry-msgs'
'ros-lunar-message-generation'
)

conflicts=()
replaces=()

_dir=tf2_msgs
source=()
md5sums=()

prepare() {
    cp -R $startdir/tf2_msgs $srcdir/tf2_msgs
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

