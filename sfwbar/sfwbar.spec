Name:           sfwbar
Version:        0.9.10.1
Release:        1%{?dist}
Summary:        Sway Floating Window Bar
License:        GPL-3.0
URL:            https://github.com/LBCrion/sfwbar
Source0:        https://github.com/LBCrion/sfwbar/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  make
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

%build
mkdir -p %{buildroot}/x86_64-redhat-linux-gnu
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications/

#DESTDIR=%{buildroot}%{_prefix} PREFIX=%{buildroot}%{_prefix} %meson_configure
#DESTDIR=%{buildroot}%{_prefix} PREFIX=%{buildroot}%{_prefix} %meson_build
#DESTDIR=%{buildroot}%{_prefix} PREFIX=%{buildroot}%{_prefix} %ninja_build
%meson_build
%ninja_build

%install
#DESTDIR=%{buildroot}%{_prefix}  PREFIX=%{buildroot}%{_prefix} %ninja_install
%ninja_install

%files
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/*
%license LICENSE


%changelog
* Tue Jun 08 2021 Adam Thiede <me@adamthiede.com> 0.9.8-1
- Initial specfile
