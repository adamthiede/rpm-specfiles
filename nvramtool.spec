Summary: coreboot nvramtool
Name: nvramtool
Version: 4.19
Release: 1%{?dist}
License: GPLv2
URL: https://review.coreboot.org/coreboot
Source: https://coreboot.org/releases/coreboot-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc

%description
nvramtool manipulates nvram from userspace.

%prep
tar -C %{_builddir} -xf %{_sourcedir}/coreboot-%{version}.tar.xz
mv %{_builddir}/coreboot-%{version} %{_builddir}/nvramtool-%{version}
cd %{_builddir}/nvramtool-%{version}/util/nvramtool
DESTDIR=%{buildroot} PREFIX=%{_prefix} make
install -Dm755 nvramtool %{buildroot}/%{_sbindir}/nvramtool

%files
%{_sbindir}/%{name}

%changelog
* Wed Oct 26 2022  Adam Thiede <adamj@mailbox.org> 4.18
- version change

* Fri Jun 24 2022  Adam Thiede <adamj@mailbox.org> 4.17
- version change

* Sat May 14 2022 Adam Thiede <adamj@mailbox.org> 4.16
- initial spec file
