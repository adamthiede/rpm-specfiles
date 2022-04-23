Summary: USENET-inspired, uncensorable, decentralized internet discussion system.}
Name: superhighway84 
Version: 0.1.1
Release: 1%{?dist}
License: GPLv3
URL: https://github.com/mrusme/superhighway84
Source: https://github.com/mrusme/superhighway84/archive/v%{version}.tar.gz

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
USENET-inspired, uncensorable, decentralized internet discussion system.}

%prep
%setup -q

%build
sed -i go.mod -e 's/^go 1.17/go 1.16/'
go mod tidy
go build

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/superhighway84
%doc README.md
%license LICENSE

%changelog
* Tue Apr 12 2022 Adam Thiede <adamj@mailbox.org> 0.1.1
- Created spec file
