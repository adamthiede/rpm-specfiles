Summary: A GNOME Matrix Client
Name: fractal
Version: 4.4.0
Release: 1%{?dist}
License: GPL
URL: https://gitlab.gnome.org/GNOME/fractal
Source: https://gitlab.gnome.org/GNOME/fractal/-/archive/%{version}/fractal-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gmp-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  rust
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gst-editing-services-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(libhandy-0.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)

Requires: gtk3
Requires: desktop-file-utils

%global debug_package %{nil}

%description
Fractal is a Matrix messaging app for GNOME written in Rust.
Its interface is optimized for collaboration in large groups,
such as free software projects.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/fractal
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Fractal.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Fractal-symbolic.svg
%{_datadir}/applications/org.gnome.Fractal.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Fractal.gschema.xml
%{_datadir}/locale/*/LC_MESSAGES/fractal.mo
%{_datadir}/metainfo/org.gnome.Fractal.metainfo.xml

%changelog
* Wed Oct 28 2020 Elagost <me@elagost.com>
- Created spec file
