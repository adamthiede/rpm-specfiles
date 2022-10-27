Summary: better readability of web pages on the CLI.
Name: reader
Version: 0.3.0
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
#sed -i -e 's,go 1.17,go 1.16,' go.mod
go mod tidy
go build

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc README.md
%license LICENSE

%changelog
* Wed Apr 13 2022 Adam Thiede <adamj@mailbox.org> 0.3.0

* Wed Apr 13 2022 Adam Thiede <adamj@mailbox.org> 0.1.3
- genesis
