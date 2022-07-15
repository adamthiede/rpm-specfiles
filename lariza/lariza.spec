Summary: Simple WebKit2GTK+ Browser 
Name: lariza
Version: v22.04
Release: 1%{?dist}
License: MIT
URL: https://www.uninformativ.de/git/lariza/
Source: https://www.uninformativ.de/git/lariza/archives/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: gtk3-devel
BuildRequires: webkit2gtk3-devel

Requires: gtk3
Requires: webkit2gtk3

%global debug_package %{nil}

%description
Simple WebKit2GTK+ Browser

%prep
%setup -q

%build
sed -i Makefile -e 's,prefix = /usr/local,prefix = /usr/,'

%install
%make_install

%files
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/web_extensions/we_adblock.so
%{_datadir}/%{name}/user-scripts/hints.js
%{_datadir}/man/man1/*
%doc README
%license LICENSE

%changelog
* Sun Jul 10 2022 Adam Thiede <adamj@mailbox.org> v22.04
- Initial 
