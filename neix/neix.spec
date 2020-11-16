Summary: a RSS/Atom feed reader for your terminal.
Name: neix
Version: 0.1.3
Release: 1%{?dist}
License: GPL
URL: https://github.com/tomschwartz/neix
Source: https://github.com/tomschwarz/neix/archive/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: g++
BuildRequires: make
BuildRequires: cmake
BuildRequires: libcurl-devel
BuildRequires: ncurses-devel

Requires: ncurses-base

%global debug_package %{nil}

%description
a RSS/Atom feed reader for your terminal.

%prep
%setup -q

%build
#cmake .
%cmake
#make PREFIX=%{_prefix} DESTDIR=%{buildroot}

%install
%cmake_install
#make install PREFIX=%{_prefix} DESTDIR=%{buildroot} 

%files
%{_bindir}/neix
%doc README.md
%license LICENSE.md

%changelog
* Sun Nov 1 2020 Elagost <me@elagost.com>
- Created spec file
