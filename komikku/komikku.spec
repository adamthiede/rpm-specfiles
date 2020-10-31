Summary: Online/Offline Manga Reader for GNOME
Name: Komikku
Version: v0.21.1
Release: 1%{?dist}
License: GPL
URL: https://gitlab.com/valos/Komikku
Source: https://gitlab.com/valos/Komikku-/archive/%{version}/Komikku-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  gtk3-devel
BuildRequires:  libhandy1-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  python3
Requires: gtk3
Requires: desktop-file-utils

%global debug_package %{nil}

%description
An online/offline manga reader for GNOME,
developed with the aim of being used with the Librem 5 phone.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_bindir}/komikku
%{_datadir}/icons/hicolor/scalable/apps/info.febvre.Komikku.svg
%{_datadir}/icons/hicolor/symbolic/apps/info.febvre.Komikku-symbolic.svg
%{_datadir}/applications/info.febvre.Komikku.desktop
%{_datadir}/glib-2.0/schemas/info.febvre.Komikku.gschema.xml
%{_datadir}/locale/*/LC_MESSAGES/komikku.mo
%{_prefix}/lib/python*/site-packages/komikku/*
%{_prefix}/lib/python*/site-packages/komikku/servers/*
%{_datadir}/komikku/info.febvre.Komikku.gresource
%{_datadir}/metainfo/info.febvre.Komikku.appdata.xml


%changelog
* Fri Oct 30 2020 Elagost <me@elagost.com>
- Created spec file
