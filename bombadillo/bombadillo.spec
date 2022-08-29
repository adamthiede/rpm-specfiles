Summary: a non-web browser
Name: bombadillo
Version: 2.4.0
Release: 1%{?dist}
License: GPLv3
URL: https://tildegit.org/sloum/bombadillo
Source: https://tildegit.org/sloum/bombadillo/archive/%{version}.tar.gz

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
%define _build_id_links none

%description
Bombadillo is a non-web browser for the terminal.
Bombadillo supports gopher, gemini, finger, local (a user's file system)


%prep
%setup -q -n bombadillo

%build
%make_build %{?_smp_mflags} PREFIX=%{_prefix}

#%install
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications/
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/bombadillo
%{_datadir}/applications/bombadillo.desktop
%{_mandir}/man1/bombadillo.1.gz
%{_datadir}/pixmaps/bombadillo-icon.png
%doc README.md
%license LICENSE

%changelog
* Sun Aug 28 2022 Adam Thiede <adamj@mailbox.org> 2.4.0
- initial version

