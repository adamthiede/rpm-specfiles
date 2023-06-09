%define name AlephOne
%define version 20220115
%define release 1

Summary: 3D first-person shooter game
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Amusements/Games
URL: https://github.com/Aleph-One-Marathon/alephone
Source: https://github.com/Aleph-One-Marathon/alephone/releases/download/release-%{version}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# not relocatable because the data file packages depend upon the location
# of the data files in this package

Requires: SDL >= 1.2.0 SDL_image >= 1.2.0 SDL_net 
BuildRequires: make autoconf automake boost-devel curl-devel expat-devel  gcc-c++ libpng-devel SDL2-devel SDL2_ttf-devel SDL2_image-devel SDL2_net-devel SDL2_mixer-devel speex-devel speexdsp-devel zziplib-devel libsndfile-devel libvorbis-devel

%global __brp_mangle_shebangs %{nil}

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

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%clean

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL.Unix README docs/MML.html docs/Lua.html
%{_bindir}/alephone
%{_datadir}/AlephOne/MML
%{_mandir}/man6/alephone.6.gz
%{_datadir}/mime/packages/alephone.xml
%{_datadir}/AlephOne/Plugins/Default_Theme/
%{_datadir}/icons/hicolor/*/mimetypes/*alephone*


%changelog
* Sat Jun 21 2008 Gregory Smith <wolfy@treellama.org>
- removed the dependence on AlephOne-core-data (users can use unimap zip files)
- removed deprecated cheats docs
- updated required libraries (there are many)

* Sun Nov 20 2005 Christian Bauer <www.cebix.net>
- modernized the spec file a bit

* Thu Oct  5 2000 Christian Bauer <Christian.Bauer@uni-mainz.de>
- Added docs and theme data files
- Package name and version are set by configure script

* Fri Sep 30 2000 Tom Moertel <tom-rpms-alephone@moertel.com>
- Added a requirement to the base package for AlephOne-core-data
- Split out the Marathon Infinity Demo data into its own package

* Thu Sep 29 2000 Tom Moertel <tom-rpms-alephone@moertel.com>
- Added patch for SDL 1.1.5 SDL_SetClipping incompatability.

* Sat Sep 23 2000 Tom Moertel <tom-rpms-alephone@moertel.com>
- Added Marathon Infinity Demo data to package.
