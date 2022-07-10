Summary: IRC client
Name: catgirl
Version: 2.1 
Release: 1%{?dist}
License: GPLv3
URL: https://git.causal.agency/catgirl
Source: https://git.causal.agency/catgirl/snapshot/catgirl-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: libretls-devel

Requires: ncurses-base

%global debug_package %{nil}

%description
TLS-only terminal IRC client

%prep
%setup -q

./configure

%build

%install
%make_install PREFIX=/usr/ MANDIR=/usr/share/man

%files
%{_bindir}/%{name}
%{_docdir}/man/man1/%{name}.1.gz
%doc README.7
%license LICENSE

%changelog
* Sun Jul 10 2022 Adam Thiede <adamj@mailbox.org> 2.1
- 2.1
- Initial 
