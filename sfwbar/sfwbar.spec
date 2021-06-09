Name:           sfwbar
Version:        0.9.8
Release:        1%{?dist}
Summary:        Sway Floating Window Bar
License:        GPL-3.0
URL:            https://github.com/LBCrion/sfwbar
Source0:        https://github.com/LBCrion/sfwbar/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  meson
BuildRequires:  gtk3-devel 
BuildRequires:  libucl-devel
BuildRequires:  gtk-layer-shell-devel

%description
SFWBar (Sway Floating Window Bar) is a flexible taskbar application for Sway wayland compositor, designed with a stacking layout in mind.

%build
meson build
ninja -C build

%install
DESTDIR=%{buildroot}%{_prefix} %{?_smp_mflags} PREFIX=%{buildroot}%{_prefix} ninja -C build install

%files
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/*
%license LICENSE


%changelog
* Tue June 08 2021 Adam Thiede <me@adamthiede.com> 0.9.8-1
- Initial specfile
