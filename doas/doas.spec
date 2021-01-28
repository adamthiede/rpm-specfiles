Summary: A port of OpenBSD's doas to Linux
Name: doas
Version: 6.3p4
Release: 1%{?dist}
License: BSD
URL: https://github.com/slicer69/doas
Source: https://github.com/slicer69/doas/archive/%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: bison
BuildRequires: flex
BuildRequires: pam-devel

%global debug_package %{nil}

%description
A port of OpenBSD's doas which runs on FreeBSD, Linux, NetBSD, illumos and macOS.

%prep
%setup -q

%build
make %{?_smp_mflags} PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%files
%{_bindir}/doas
%doc README.md
%license LICENSE

%changelog
* Thu Jan 28 2021 Adam Thiede <me@adamthiede.com>
- Created spec file
