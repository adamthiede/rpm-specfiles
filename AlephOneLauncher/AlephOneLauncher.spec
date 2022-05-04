%define name alephone-marathon-launcher
%define version 1.2
%define release 1

Summary: Launcher for AlephOne
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Amusements/Games
URL: https://gitlab.com/elagost/alephone-marathon-launcher/
Source: %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# not relocatable because the data file packages depend upon the location
# of the data files in this package

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

%prep
%setup -q

%build
make

%install
rm -rf ${RPM_BUILD_ROOT}
DESTDIR=${RPM_BUILD_ROOT} make packaging

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL.Unix README docs/MML.html docs/Lua.html
%{_bindir}/marathon-launcher
%{_bindir}/marathon-installer.sh
%{_datadir}/applications/marathon-launcher.desktop
%{_datadir}/icons/hicolor/128x128/apps/marathon_128.png


%changelog
* Thu Jul 09 2020 Elagost <me@elagost.com>
- Initial release
