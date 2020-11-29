Summary: a Gemini browser for your terminal
Name: amfora
Version: 1.6.0
Release: 1%{?dist}
License: GPL
URL: https://github.com/makeworld-the-better-one/amfora
Source: https://github.com/makeworld-the-better-one/amfora/archive/v%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: golang

Requires: ncurses-base

%global debug_package %{nil}

%description
Amfora aims to be the best looking Gemini client with the most features... all in the terminal.

%prep
%setup -q

%build
%make_build %{?_smp_mflags} PREFIX=%{_prefix}

%install
%make_install PREFIX=%{buildroot}%{_prefix}

%files
%{_bindir}/amfora
%{_datadir}/applications/amfora.desktop
%doc README.md
%license LICENSE

%changelog
* Sun Nov 29 2020 Elagost <me@elagost.com>
- Created spec file
