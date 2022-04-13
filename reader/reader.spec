Summary: better readability of web pages on the CLI.
Name: readability
Version: 0.1.3
Release: 1%{?dist}
License: GPLv3
URL: https://github.com/mrusme/reader
Source: %{url}/archive/v%{version}.tar.gz

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
reader is for your command line what the "readability" view is for modern browsers: A lightweight tool offering better readability of web pages on the CLI.

%prep
%setup -q

%build
go mod tidy
go build

%install
install -Dm755 %{name} %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}
%doc README.md
%license LICENSE

%changelog
* Tue Apr 13 2022 Adam Thiede <adamj@mailbox.org> 0.1.3
- genesis
