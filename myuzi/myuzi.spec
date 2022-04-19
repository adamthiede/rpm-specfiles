Summary: Free Spotify alternative for Linux with no ads.
Name: myuzi
Version: v0.1.4
Release: 1%{?dist}
License: MIT
URL: https://gitlab.com/zehkira/%{name}
Source: %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: gtk3-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: gtk3
Requires: python
Requires: python3-beautifulsoup4
Requires: python3-gobject

%description
Free Spotify alternative for Linux with no ads.

%prep
%setup -q

%build
sed -i -e 's/env python3/python3/' bin/myuzi.py

%install
DESTDIR=%{buildroot}/ make install

%files
%{_bindir}/myuzi
%{_datadir}/applications/myuzi.desktop
%{_datadir}/icons/hicolor/scalable/apps/myuzi.svg
%{_datadir}/icons/hicolor/*/apps/myuzi.png
%{_prefix}/lib/python3.10/site-packages/myuzi/*.py
%{_prefix}/lib/python3.10/site-packages/myuzi-0.1.4-py3.10.egg-info/*
%{_prefix}/lib/python3.10/site-packages/myuzi/*/*
%license LICENSE
%doc README.md

%changelog
* Sun Apr 17 2022 Adam Thiede <adamj@mailbox.org>
- Created spec file

