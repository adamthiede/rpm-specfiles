%define name alephone-marathon-launcher
%define version 1.3a
%define release 1
Summary: Launcher for AlephOne
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Amusements/Games
URL: https://gitlab.com/elagost/alephone-marathon-launcher/
Source: %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

Requires: gtk3
Recommends: alephone
BuildRequires: make gtk3-devel vala

%description
Aleph One is an Open Source 3D first-person shooter game, based on the game
Marathon 2 by Bungie Software. It is set in a Sci-Fi universe dominated by
deviant computer AIs and features a well thought-out plot. Aleph One
supports, but doesn't require, OpenGL for rendering.

Aleph One requires additional data -- shape, sound, and map
information -- in order to run. The easiest way to get this is to go
to http://source.bungie.org/get/, and download one of the scenario zip
files there. Unzip it, and pass the resulting directory as an argument
to alephone. For example:

alephone "~/Marathon Infinity"

%global debug_package %{nil}
%global __brp_mangle_shebangs %{nil}

%prep
%setup -q

%build
%make_build

%install
#%make_install
PREFIX=%{buildroot}%{_prefix} make install

%clean

%files
%defattr(-,root,root)
%doc README.md
%{_bindir}/marathon-launcher
%{_bindir}/marathon-installer.sh
%{_datadir}/applications/marathon-launcher.desktop
%{_datadir}/icons/hicolor/128x128/apps/marathon_128.png
%{_datadir}/icons/marathon_128.png


%changelog
* Wed May 04 2022 Elagost <adamj@mailbox.org>
- Update to get it a lot cleaner and actually working

* Thu Jul 09 2020 Elagost <adamj@mailbox.org>
- Initial release
