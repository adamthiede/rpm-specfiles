Summary: terraform
Name: terraform
Version: 1.4.6
Release: 1%{?dist}
License: GPLv3
URL: https://github.com/hashicorp/terraform
Source: https://github.com/hashicorp/terraform/archive/v%{version}.tar.gz

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
Automate your infrastructure

%prep
%setup -q

%build
#sed -i -e 's,go 1.17,go 1.16,' go.mod
#sed -i -e 's,go-tfe v0.19.1-.*$,go-tfe v0.22.0,' go.mod
#sed -i -e '/sigs.k8s.io\/json/d' go.mod
#go mod download github.com/hashicorp/go-tfe
%make_build PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_bindir}
go build
cp terraform %{buildroot}%{_bindir}

%files
%{_bindir}/terraform
%doc README.md
%license LICENSE

%changelog
* Sat Apr 08 2023 Adam Thiede <adamj@mailbox.org> 1.2.6
- v1.4.4
