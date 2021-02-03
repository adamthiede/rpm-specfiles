Summary: a Gemini browser for your terminal
Name: amfora
Version: 1.7.2
Release: 1%{?dist}
License: GPL
URL: https://github.com/makeworld-the-better-one/amfora
Source: https://github.com/makeworld-the-better-one/amfora/archive/v%{version}.tar.gz

BuildRequires: make
BuildRequires: git
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
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications/
%make_install PREFIX=%{buildroot}%{_prefix}

%files
%{_bindir}/amfora
%{_datadir}/applications/amfora.desktop
%doc README.md
%license LICENSE

%changelog
* Sun Nov 29 2020 Elagost <me@elagost.com>
- Created spec file
