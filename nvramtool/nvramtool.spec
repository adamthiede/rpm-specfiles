Summary: coreboot nvramtool
Name: nvramtool
Version: 4.16
Release: 1%{?dist}
License: GPLv3
URL: https://review.coreboot.org/coreboot
Source: https://coreboot.org/releases/coreboot-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: libusb-devel 
BuildRequires: pciutils-devel

#%global debug_package %{nil}

%description
nvramtool manipulates nvram from userspace.

%prep

cd coreboot-%{version}/util/nvramtool
DESTDIR=%{buildroot} PREFIX=%{_prefix} make install

%files
/usr/local/sbin/%{name}
/usr/local/share/man/man8/%{name}.8

%changelog
* Sat May 14 2022 Adam Thiede <adamj@mailbox.org> 4.16
- genesis
