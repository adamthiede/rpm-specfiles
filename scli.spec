Summary: a TUI interface for signal-cli
Name: scli
Version: 0.7.1
Release: 1%{?dist}
License: GPL
URL: https://github.com/isamert/scli
Source: %{url}/archive/v%{version}.tar.gz

BuildRequires: make
Requires: signal-cli python3-urwid python3-urwid-readline

%global debug_package %{nil}
%global __brp_mangle_shebangs %{nil}

%description

%prep
%setup -q

install -D scli %{buildroot}%{_bindir}/scli

%files
%{_bindir}/scli
%doc README.md
%license LICENSE

%changelog
* Sun Oct 25 2020 Elagost <me@elagost.com>
- Created spec file
