#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5D2EEE6F6F349D7C (tim@centricular.com)
#
Name     : gst-python
Version  : 1.20.5
Release  : 20
URL      : https://gstreamer.freedesktop.org/src/gst-python/gst-python-1.20.5.tar.xz
Source0  : https://gstreamer.freedesktop.org/src/gst-python/gst-python-1.20.5.tar.xz
Source1  : https://gstreamer.freedesktop.org/src/gst-python/gst-python-1.20.5.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: gst-python-lib = %{version}-%{release}
Requires: gst-python-license = %{version}-%{release}
Requires: gst-python-python = %{version}-%{release}
Requires: gst-python-python3 = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : gst-plugins-base-dev
BuildRequires : gstreamer-dev
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : pypi(pillow)
BuildRequires : python3-dev

%description


%package lib
Summary: lib components for the gst-python package.
Group: Libraries
Requires: gst-python-license = %{version}-%{release}

%description lib
lib components for the gst-python package.


%package license
Summary: license components for the gst-python package.
Group: Default

%description license
license components for the gst-python package.


%package python
Summary: python components for the gst-python package.
Group: Default
Requires: gst-python-python3 = %{version}-%{release}

%description python
python components for the gst-python package.


%package python3
Summary: python3 components for the gst-python package.
Group: Default
Requires: python3-core
Requires: pypi(pillow)

%description python3
python3 components for the gst-python package.


%prep
%setup -q -n gst-python-1.20.5
cd %{_builddir}/gst-python-1.20.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671552983
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dlibpython-dir=/usr/lib64  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gst-python
cp %{_builddir}/gst-python-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gst-python/a38bf62fc86fcde6fe8b09b6a8732d3c24edfd95 || :
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/gstreamer-1.0/libgstpython.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gst-python/a38bf62fc86fcde6fe8b09b6a8732d3c24edfd95

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
