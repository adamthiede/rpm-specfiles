Summary: A GNOME Matrix Client
Name: fractal
Version: 4.4.0
Release: 1%{?dist}
License: GPL
URL: https://gitlab.gnome.org/GNOME/fractal
Source: https://gitlab.gnome.org/GNOME/fractal/-/archive/%{version}/fractal-%{version}.tar.gz

#BuildRequires: gcc
#BuildRequires: cmake
#BuildRequires: meson
#BuildRequires: rust
#BuildRequires: make
#BuildRequires: cargo
#BuildRequires: gtk3-devel
#BuildRequires: vala
#BuildRequires: gspell-devel
#BuildRequires: libhandy-devel
#BuildRequires: gstreamer1-devel
#BuildRequires: rust-gstreamer-audio-devel
#BuildRequires: rust-gstreamer-player-devel
#BuildRequires: gstreamer-devel
#BuildRequires: gst-editing-services-devel
#BuildRequires: gtksourceview4-devel
#BuildRequires: openssl-devel
#BuildRequires: desktop-file-utils
#BuildRequires: gobject-introspection-devel

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
#BuildRequires:  pkgconfig(gstreamer-player-1.0)
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
#meson . _build --prefix=%{buildroot}%{_prefix}
#PREFIX=%{buildroot}%{_prefix} ninja -C _build
%meson
%meson_build

%install
#PREFIX=%{buildroot}%{_prefix} ninja -C _build install 
%meson_install
%find_lang %{name}

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/fractal
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Fractal.svg
%{_datadir}/icons/hicolor/icon-theme.cache
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Fractal-symbolic.svg
%{_datadir}/applications/org.gnome.Fractal.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Fractal.gschema.xml
%{_datadir}/glib-2.0/schemas/gschemas.compiled
%{_datadir}/locale/*/LC_MESSAGES/fractal.mo
%{_datadir}/metainfo/org.gnome.Fractal.metainfo.xml

%changelog
* Wed Oct 28 2020 Elagost <me@elagost.com>
- Created spec file
