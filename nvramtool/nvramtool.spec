Summary: coreboot nvramtool
Name: nvramtool
Version: 4.16
Release: 1%{?dist}
License: GPLv3
URL: https://review.coreboot.org/coreboot
Source: https://coreboot.org/releases/coreboot-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc
#BuildRequires: libusb-devel
#BuildRequires: pciutils-devel

%description
nvramtool manipulates nvram from userspace.

%prep

cd coreboot-%{version}/util/nvramtool
DESTDIR=%{buildroot} PREFIX=%{_prefix} make
install -Dm755 nvramtool %{buildroot}/%{_bindir}/nvramtool

%files
%{_bindir}/%{name}

%changelog
* Sat May 14 2022 Adam Thiede <adamj@mailbox.org> 4.16
- genesis
