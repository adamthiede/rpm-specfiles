Summary: TUI mastodon client in go
Name: tut
Version: 1.0.15
Release: 1%{?dist}
License: MIT
URL: https://github.com/RasmusLindroth/tut
Source: https://github.com/RasmusLindroth/tut/archive/%{version}.tar.gz

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
TUI Mastodon client written it Go

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
* Tue Jun 06 2022 Adam Thiede <adamj@mailbox.org> 1.0.13
- 1.0.13

* Tue Jun 06 2022 Adam Thiede <adamj@mailbox.org> 1.0.11
- 1.0.11
- Initial 
