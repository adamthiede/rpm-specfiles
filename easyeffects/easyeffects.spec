Summary: Audio effects for PipeWire applications.
Name: easyeffects
Version: 5.0.4
Release: 1%{?dist}
License: GPL
URL: https://github.com/wwmm/easyeffects
Source: https://github.com/wwmm/easyeffects/archive/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: g++
BuildRequires: cmake
BuildRequires: meson
BuildRequires: itstool
BuildRequires: boost-devel
BuildRequires: libbs2b-devel
BuildRequires: lilv-devel
BuildRequires: rnnoise-devel
BuildRequires: gtkmm30-devel
BuildRequires: pipewire-devel
BuildRequires: libebur128-devel
BuildRequires: gstreamer1-devel
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: zita-convolver-devel
BuildRequires: gstreamer1-plugins-bad-free-devel

Requires: gtk3
Requires: gtk4
Requires: pipewire

%global debug_package %{nil}

%description
Limiter, compressor, convolver, equalizer and auto volume and many other plugins for PipeWire applications

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
%{_bindir}/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/*
%doc README.md
%license LICENSE.md

%changelog
* Sat Sep 25 2021 Adam Thiede <adamj@mailbox.org>
- Created spec file
