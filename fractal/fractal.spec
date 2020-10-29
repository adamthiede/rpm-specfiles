Summary: A GNOME Matrix Client
Name: fractal
Version: 4.4.0
Release: 1%{?dist}
License: GPL
URL: https://gitlab.gnome.org/GNOME/fractal
Source: https://gitlab.gnome.org/GNOME/fractal/-/archive/%{version}/fractal-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: meson
BuildRequires: rust
BuildRequires: make
BuildRequires: cargo
BuildRequires: gtk3-devel
BuildRequires: vala
BuildRequires: gspell-devel
BuildRequires: libhandy-devel
BuildRequires: gstreamer1-devel
BuildRequires: rust-gstreamer-audio-devel
BuildRequires: rust-gstreamer-player-devel
BuildRequires: gstreamer-devel
BuildRequires: gst-editing-services-devel
BuildRequires: gtksourceview4-devel
BuildRequires: openssl-devel
BuildRequires: desktop-file-utils
BuildRequires: gobject-introspection-devel

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
meson . _build --prefix=%{buildroot}%{_prefix}
PREFIX=%{buildroot}%{_prefix} ninja -C _build

%install
PREFIX=%{buildroot}%{_prefix} ninja -C _build install 

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
