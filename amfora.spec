Summary: a Gemini browser for your terminal
Name: amfora
Version: 1.9.2
Release: 1%{?dist}
License: GPLv3
URL: https://github.com/makew0rld/amfora
Source: https://github.com/makew0rld/amfora/archive/v%{version}.tar.gz

BuildRequires: make
BuildRequires: git
BuildRequires: gcc
# suse package: go
# fedora/rhel package: golang
%if 0%{?suse_version}
BuildRequires: go
%endif
%if 0%{?fedora}
BuildRequires: golang
%endif
%if 0%{?rhel}
BuildRequires: golang
%endif

Requires: ncurses-base

%global debug_package %{nil}

%description
Amfora aims to be the best looking Gemini client with the most features...
all in the terminal.

%prep
%setup -q

%build
%make_build %{?_smp_mflags} BUILDER="official-rpm" PREFIX=%{_prefix}

#%install
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications/
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/amfora
%{_datadir}/applications/amfora.desktop
%doc README.md
%license LICENSE

%changelog
* Sun Mar 20 2022 Adam Thiede <me@adamthiede.com> 1.9.2
- Updated version

* Sun Oct 3 2021 Adam Thiede <me@adamthiede.com> 1.8.0
- Updated version and cleaned spec file for upload

* Sun Nov 29 2020 Adam Thiede <me@adamthiede.com> 1.6.0
- Created spec file
