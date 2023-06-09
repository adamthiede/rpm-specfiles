Summary: ipfs client in go
Name: go-ipfs
Version: 0.12.2
Release: 1%{?dist}
License: GPLv3
URL: https://github.com/ipfs/go-ipfs
Source: https://github.com/ipfs/go-ipfs/archive/v%{version}.tar.gz

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
IPFS client in go

%prep
%setup -q

%build
make build

%install
install -Dm755 cmd/ipfs/ipfs %{buildroot}/%{_bindir}/ipfs

%files
%{_bindir}/ipfs
%doc README.md
%license LICENSE

%changelog
* Wed Apr 13 2022 Adam Thiede <adamj@mailbox.org> 0.12.2
- v0.12.2

* Thu Jan 20 2022 Adam Thiede <adamj@mailbox.org> 0.11.0
- v0.11.0
- initial specfile

