Summary: Automatically suspend inactive X11 applications
Name: xsuspender
Version: 1.3
Release: 1%{?dist}
License: WTFPL
URL: https://github.com/kernc/xsuspender
Source: https://github.com/kernc/xsuspender/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  procps-ng
BuildRequires:  glib2-devel
BuildRequires:  libwnck-devel
BuildRequires:  libwnck3-devel

Requires: xorg-x11-server-Xorg
Requires: desktop-file-utils

%global debug_package %{nil}

%description
Automatically suspend inactive X11 applications.

%prep
%setup -q

cd build

cmake .. -DCMAKE_INSTALL_PREFIX=/usr/local
%make_build
%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/xsuspender

%changelog
* Mon Jan 24 2022 Elagost <me@elagost.com>
- Created spec file
