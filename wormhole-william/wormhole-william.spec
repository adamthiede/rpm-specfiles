Summary: magic-wormhole but in go
Name: wormhole-william
Version: 1.0.6
Release: 1%{?dist}
License: MIT
URL: https://github.com/psanford/wormhole-william
Source: https://github.com/psanford/wormhole-william/archive/v%{version}.tar.gz

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
End-to-end encrypted file transfer. A magic wormhole CLI and API in Go.

%prep
%setup -q

%build
go build

%install
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_bindir}
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/wormhole-william
%doc README.md
%license LICENSE

%changelog
* Sun Mar 20 2022 Adam Thiede <adamj@mailbox.org> 1.0.6
- Updated version

