Summary: A port of OpenBSD's doas to Linux
Name: doas
Version: 6.3p5
Release: 1%{?dist}
License: BSD
URL: https://github.com/slicer69/doas
Source: https://github.com/slicer69/doas/archive/%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: bison
BuildRequires: flex
BuildRequires: pam-devel
BuildRequires: byacc

%global debug_package %{nil}

%description
A port of OpenBSD's doas which runs on FreeBSD, Linux, NetBSD, illumos and macOS.

%prep
%setup -q

%build
make %{?_smp_mflags} PREFIX=%{_prefix} MANDIR=%{buildroot}/%{_datadir}/man

%install
%make_install PREFIX=%{_prefix} DESTDIR=%{buildroot} MANDIR=%{buildroot}/%{_datadir}/man

%post
if [[ -f /etc/pam.d/sudo && ! -f /etc/pam.d/doas ]];then
    cp /etc/pam.d/sudo /etc/pam.d/doas
fi

%files
%{_bindir}/doas
%{_bindir}/vidoas
%{_datadir}/man/man1/doas.1.gz
%{_datadir}/man/man5/doas.conf.5.gz
%{_datadir}/man/man8/vidoas.8.gz
%doc README.md
%license LICENSE

%changelog
* Thu Jan 28 2021 Adam Thiede <me@adamthiede.com>
- Created spec file
