Summary: Quickly create and run optimised Windows, macOS and Linux desktop virtual machines.
Name: quickemu
Version: 3.15
Release: 1%{?dist}
License: MIT
URL: https://github.com/quickemu-project/quickemu
Source: %{url}/archive/%{version}.tar.gz

BuildRequires: bash
BuildRequires: make

Requires: bash
Requires: coreutils
Requires: edk2-ovmf
Requires: genisoimage
Requires: grep
Requires: jq
Requires: procps-ng
Requires: python3
Requires: qemu
Requires: qemu-ui-gtk
Requires: qemu-ui-sdl
Requires: qemu-ui-spice-core
Requires: sed
Requires: spice-gtk3
Requires: spice-server
Requires: swtpm
Requires: unzip
Requires: usbutils
Requires: util-linux
Requires: wget
Requires: xdg-user-dirs
Requires: xrandr

%global __brp_mangle_shebangs %{nil}

%description
Quickly create and run optimised Windows, macOS and Linux desktop virtual machines.

%prep
%setup -q

%install
cd docs
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/quickemu
%{_bindir}/quickget
%{_bindir}/macrecovery
%{_datadir}/man/man1/*
%doc README.md
%license LICENSE

%changelog
* Sun Apr 25 2022 Adam Tyiede <adamj@mailbox.org> 3.15
- created spec file

