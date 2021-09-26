Summary: Send and Receive Files across the Network
Name: warpinator
Version: 1.2.4
Release: 0%{?dist}
License: GPL
URL: https://github.com/linuxmint/warpinator
Source: %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: gcc
BuildRequires: meson
BuildRequires: gettext 
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils


Requires: python3-grpcio
Requires: python3-cryptography
Requires: python3-netifaces
Requires: python3-pynacl
Requires: python3-zeroconf
Requires: python3-google-api-core
Requires: python3-packaging
Requires: python3-xapp
Requires: python3-xapps-overrides
Requires: python3-setproctitle


%description
Warpinator allows you to easily connect multiple computers
on a local area network and share files quickly and securely.

%prep
%setup -q

%build
%meson -Dinclude-firewall-mod=false
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/*.desktop
appstream-util validate --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license  COPYING
%{_bindir}/warpinator
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/glib-2.0/schemas/org.x.Warpinator.gschema.xml
%{_datadir}/applications/*.desktop
%{_metainfodir}/*
%{_datadir}/warpinator/
%{_libexecdir}/warpinator/*.py
%{_sysconfdir}/xdg/autostart/*


%changelog
* Sat Sep 25 2021 Adam Thiede <adamj@mailbox.org>
- Created spec file

* Mon Sep 07 2020 Elagost <me@elagost.com>
- Created spec file
