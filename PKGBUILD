# Script generated with Bloom
pkgdesc="ROS - Small lib to transform sensor_msgs with tf. Most notably, PointCloud2"
url='http://www.ros.org/wiki/tf2_ros'

pkgname='ros-kinetic-tf2-sensor-msgs'
pkgver='0.5.17_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('eigen3'
'ros-kinetic-catkin>=0.5.6'
'ros-kinetic-cmake-modules'
'ros-kinetic-geometry-msgs'
'ros-kinetic-rostest'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf2'
'ros-kinetic-tf2-ros'
)

depends=('eigen3'
'ros-kinetic-python-orocos-kdl'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf2'
'ros-kinetic-tf2-ros'
)

conflicts=()
replaces=()

_dir=tf2_sensor_msgs
source=()
md5sums=()

prepare() {
    cp -R $startdir/tf2_sensor_msgs $srcdir/tf2_sensor_msgs
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

