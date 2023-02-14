Summary: azure kubernetes login plugin
Name: go-aws-azure-login
Version: 0.3
Release: 1%{?dist}
License: MIT
URL: https://github.com/luneo7/go-aws-azure-login
Source: https://github.com/luneo7/go-aws-azure-login/archive/v%{version}.tar.gz

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
go-aws-azure-login for azure

%prep
%setup -q

#%build
#go mod download github.com/hashicorp/go-tfe
#%make_build PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_bindir}
go build
cp %{name} %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}
%doc README.md
%license LICENSE

%changelog
* Tue Feb 14 2023 Adam Thiede <adamj@mailbox.org> 0.3
- Initial RPM
