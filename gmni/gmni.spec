Summary: A Gemini Client
Name: gmni
Version: master
Release: 1%{?dist}
License: GPL
URL: https://git.sr.ht/~sircmpwn/gmni
Source: https://git.sr.ht/~sircmpwn/gmni/archive/%{version}.tar.gz

BuildRequires: make
BuildRequires: git
BuildRequires: gcc
BuildRequires: openssl-devel

Requires: ncurses-base

%global debug_package %{nil}

%description

%prep
%setup -q
%configure

%build
%make_build DESTDIR=%{buildroot}%{_prefix} %{?_smp_mflags} PREFIX=%{buildroot}%{_prefix}

%install
%make_install DESTDIR=%{buildroot}%{_prefix} PREFIX=%{buildroot}%{_prefix}

%files
%{_bindir}/gmni
%{_bindir}/gmnlm
%doc README.md
%license COPYING

%changelog
* Mon Nov 30 2020 Elagost <me@elagost.com>
- Created spec file
