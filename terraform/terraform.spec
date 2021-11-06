Summary: terraform
Name: terraform
Version: 1.0.10
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
* Sat Nov 6 2021 Adam Thiede <adamj@mailbox.org> 1.0.10
- Initial 
