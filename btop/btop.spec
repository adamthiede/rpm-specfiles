Summary: Resource Monitor (based on bashtop/bpytop)
Name: btop
Version: 1.2.7
Release: 1%{?dist}
License: GPL
URL: https://github.com/aristocratos/btop/
Source: %{url}/archive/v%{version}.tar.gz

BuildRequires: make
BuildRequires: git
BuildRequires: gcc-c++

Requires: ncurses-base

%global debug_package %{nil}

%description
Resource monitor that shows usage and stats for processor, memory, disks, network and processes.
C++ version and continuation of bashtop and bpytop.

%prep
%setup -q

%make_build %{?_smp_mflags} PREFIX=%{_prefix}
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_bindir}
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/btop
%{_datadir}/btop/*
%{_datadir}/applications/btop.desktop
%{_datadir}/icons/hicolor/*
%doc README.md
%license LICENSE

%changelog
* Sat Jun 11 2022 Adam Tyiede <adamj@mailbox.org> 1.2.7
- Update btop to version 1.2.7
- add more files

* Sat Nov 27 2021 Adam Tyiede <adamj@mailbox.org> 1.1.2
- Update btop to version 1.1.2

* Mon Nov 08 2021 Adam Thiede <adamj@mailbox.org> 1.0.23
- Update btop version to 1.0.23

* Mon Oct 04 2021 Adam Thiede <adamj@mailbox.org> 1.0.13
- Update btop version to 1.0.13

* Fri Oct 01 2021 Adam Thiede <adamj@mailbox.org> 1.0.12
- Created spec file
