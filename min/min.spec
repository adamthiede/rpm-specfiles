Summary: a Gemini browser for your terminal
Name: min
Version: 0.0.42
Release: 1%{?dist}
License: MIT
URL: https://github.com/a-h/min
Source: https://github.com/a-h/min/archive/v%{version}.tar.gz

BuildRequires: go
BuildRequires: git
BuildRequires: make

Requires: ncurses-base

%global debug_package %{nil}

%description
A Gemini browser for your terminal.

%prep
%setup -q

%build
#make %{?_smp_mflags} PREFIX=%{_prefix}
go build

%install
mkdir -p %{buildroot}/%{_bindir}
install -D target/release/min %{buildroot}/%{_bindir}/min
#%make_install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%files
%{_bindir}/min
%doc README.md

%changelog
* Sun Nov 29 2020 Elagost <me@elagost.com>
- Created spec file
