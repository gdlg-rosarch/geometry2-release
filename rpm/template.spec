Name:           ros-indigo-tf2-bullet
Version:        0.5.6
Release:        0%{?dist}
Summary:        ROS tf2_bullet package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/tf2_bullet
Source0:        %{name}-%{version}.tar.gz

Requires:       bullet-devel
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-tf2
BuildRequires:  bullet-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-tf2

%description
tf2_bullet

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Sep 18 2014 Tully Foote <tfoote@osrfoundation.org> - 0.5.6-0
- Autogenerated by Bloom

