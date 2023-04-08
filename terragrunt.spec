Summary: terragrunt
Name: terragrunt
Version: 0.45.0
Release: 1%{?dist}
License: MIT
URL: https://github.com/gruntwork-io/terragrunt
Source: https://github.com/gruntwork-io/terragrunt/archive/v%{version}.tar.gz

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
#%make_build PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_bindir}
go clean -modcache
go mod tidy
go build -v -o terragrunt -ldflags "-X main.VERSION=v%{version}"
cp terragrunt %{buildroot}%{_bindir}

%files
%{_bindir}/terragrunt
%doc README.md
%license LICENSE

%changelog
* Fri 24 Mar 2022 Adam Thiede <adamj@mailbox.org> 0.45.0
- v0.45.0
