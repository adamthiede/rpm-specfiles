Summary: go-ipfs
Name: ipfs client in go
Version: 0.11.0
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
%make_build PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_bindir}
go build
cp go-ipfs %{buildroot}%{_bindir}

%files
%{_bindir}/go-ipfs
%doc README.md
%license LICENSE

%changelog
* Thu Jan 20 2022 Adam Thiede <adamj@mailbox.org> 0.11.0
- v0.11.0
- initial specfile

