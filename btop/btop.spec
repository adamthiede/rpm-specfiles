Summary: Resource Monitor (based on bashtop/bpytop)
Name: btop
Version: 1.0.12
Release: 1%{?dist}
License: GPL
URL: https://github.com/aristocratos/btop/
Source: %{url}/archive/v%{version}.tar.gz

BuildRequires: make
BuildRequires: git
BuildRequires: g++

Requires: ncurses-base

%global debug_package %{nil}

%description
Resource monitor that shows usage and stats for processor, memory, disks, network and processes.
C++ version and continuation of bashtop and bpytop.

%prep
%setup -q

%build
%make_build %{?_smp_mflags} PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_bindir}
%make_install PREFIX=%{buildroot}%{_prefix}

%files
%{_bindir}/btop
%doc README.md
%license LICENSE

%changelog
* Fri Oct 01 2021 Adam Thiede <adamj@mailbox.org>
- Created spec file