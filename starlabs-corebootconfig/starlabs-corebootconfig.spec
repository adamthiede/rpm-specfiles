Summary: A simple GUI to change settings in coreboot's CBFS, via the nvramtool utility.
Name: coreboot-configurator
Version: 8
Release: 1%{?dist}
License: GPLv3
URL: https://github.com/StarLabsLtd/coreboot-configurator
Source: %{url}/archive/%{version}.tar.gz

BuildRequires: make
BuildRequires: cmake
BuildRequires: git
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: yaml-cpp-devel
# yes, really
#BuildRequires: inkscape
Requires: qt5-qtbase-gui

#%global debug_package %{nil}

%description
A simple GUI to change settings in coreboot's CBFS, via the nvramtool utility.

%prep
%setup -q

%build
meson build

%install
%ninja_install -C build
#ninja -C build install

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/polkit-1/actions/org.coreboot.nvramtool.policy
%{_datadir}/polkit-1/actions/org.coreboot.reboot.policy
%doc README.md
%license LICENSE

%changelog
* Sat May 14 2022 Adam Thiede <adamj@mailbox.org> 8
- genesis
