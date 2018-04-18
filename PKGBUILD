# Script generated with Bloom
pkgdesc="ROS - This package contains the ROS bindings for the tf2 library, for both Python and C++."
url='http://www.ros.org/wiki/tf2_ros'

pkgname='ros-melodic-tf2-ros'
pkgver='0.6.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-melodic-actionlib'
'ros-melodic-actionlib-msgs'
'ros-melodic-catkin>=0.5.68'
'ros-melodic-geometry-msgs'
'ros-melodic-message-filters>=1.11.1'
'ros-melodic-roscpp'
'ros-melodic-rosgraph'
'ros-melodic-rospy'
'ros-melodic-rostest'
'ros-melodic-std-msgs'
'ros-melodic-tf2'
'ros-melodic-tf2-msgs'
'ros-melodic-tf2-py'
'ros-melodic-xmlrpcpp'
)

depends=('ros-melodic-actionlib'
'ros-melodic-actionlib-msgs'
'ros-melodic-geometry-msgs'
'ros-melodic-message-filters'
'ros-melodic-roscpp'
'ros-melodic-rosgraph'
'ros-melodic-rospy'
'ros-melodic-std-msgs'
'ros-melodic-tf2'
'ros-melodic-tf2-msgs'
'ros-melodic-tf2-py'
'ros-melodic-xmlrpcpp'
)

conflicts=()
replaces=()

_dir=tf2_ros
source=()
md5sums=()

prepare() {
    cp -R $startdir/tf2_ros $srcdir/tf2_ros
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/melodic/setup.bash ] && source /opt/ros/melodic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/melodic \
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

