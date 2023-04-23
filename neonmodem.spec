Summary: TUI for Discourse, Lemmy, Lobsters, and Hacker News
Name: neonmodem 
Version: 1.0.2
Release: 1%{?dist}
License: GPLv3
URL: https://github.com/mrusme/neonmodem
Source: https://github.com/mrusme/neonmodem/archive/refs/tags/v%{version}.tar.gz

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
TUI BBS-style command line client that supports Discourse, Lemmy, Lobsters and Hacker News

%prep
%setup -q

%build
make

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/neonmodem
%doc README.md
%license LICENSE

%changelog
* Tue Apr 12 2023 Adam Thiede <adamj@mailbox.org> 1.0.2
- Created spec file
