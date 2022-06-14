Summary: TUI mastodon client in go
Name: tut
Version: 1.0.11
Release: 1%{?dist}
License: MIT
URL: https://github.com/RasmusLindroth/tut
Source: https://github.com/RasmusLindroth/tut/archive/v%{version}.tar.gz

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
* Thu May 26 2022 Adam Thiede <adamj@mailbox.org> 1.2.1
- v1.2.1
* Fri May 20 2022 Adam Thiede <adamj@mailbox.org> 1.2.0
- v1.2.0
* Fri Apr 22 2022 Adam Thiede <adamj@mailbox.org> 1.1.9
- v1.1.9
* Sun Apr 3 2022 Adam Thiede <adamj@mailbox.org> 1.1.8
- v1.1.8
* Wed Jan 19 2022 Adam Thiede <adamj@mailbox.org> 1.1.4
- v1.1.4
* Sat Jan 15 2022 Adam Thiede <adamj@mailbox.org> 1.1.3
- v1.1.3
* Sat Nov 6 2021 Adam Thiede <adamj@mailbox.org> 1.0.10
- Initial 
