Summary: a TUI display manager
Name: ly
Version: 0.5.3
Release: 1%{?dist}
License: WTFPL
URL: https://github.com/fairyglade/ly
Source: https://github.com/fairyglade/ly/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: ncurses-devel

Requires: ncurses-base

%global debug_package %{nil}

%description
a TUI display manager

%prep
%setup -q

%build

%install
%make_install PREFIX=/usr/

%files
%{_bindir}/%{name}
%{_datadir}/man/man1/%{name}.1.gz
%doc readme.md
%license license.md

%changelog
* Sun Jul 10 2022 Adam Thiede <adamj@mailbox.org> 0.5.3
- Initial 
