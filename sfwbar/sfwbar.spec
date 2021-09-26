Name:           sfwbar
Version:        0.9.10.1
Release:        1%{?dist}
Summary:        Sway Floating Window Bar
License:        GPL-3.0
URL:            https://github.com/LBCrion/sfwbar
Source0:        https://github.com/LBCrion/sfwbar/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  gtk3-devel 
BuildRequires:  libucl-devel
BuildRequires:  fedora-rpm-macros
BuildRequires:  gtk-layer-shell-devel

%global debug_package %{nil}

%description
SFWBar (Sway Floating Window Bar) is a flexible taskbar application for Sway wayland compositor, designed with a stacking layout in mind.

%prep
%setup -q

PREFIX=%{_prefix} meson build
PREFIX=%{_prefix} ninja -C build
PREFIX=%{_prefix} DESTDIR=%{buildroot} ninja -C build install
mv %{buildroot}/usr/local/* %{buildroot}/usr/

%files
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/sfwbar/*
%{_datadir}/sfwbar/*/*
%{_datadir}/sfwbar/*/*/*
%license LICENSE


%changelog
* Tue Jun 08 2021 Adam Thiede <me@adamthiede.com> 0.9.8-1
- Initial specfile
