Summary: A graphical client for plain-text protocols
Name: castor
Version: 0.8.16
Release: 1%{?dist}
License: MIT
URL: https://git.sr.ht/~julienxx/castor
Source: https://git.sr.ht/~julienxx/castor/archive/%{version}.tar.gz

BuildRequires: gcc
BuildRequires: rust
BuildRequires: make
BuildRequires: cargo
BuildRequires: gtk3-devel
BuildRequires: openssl-devel
BuildRequires: desktop-file-utils

Requires: gtk3
Requires: desktop-file-utils

%global debug_package %{nil}

%description
A graphical client for plain-text protocols written in Rust with GTK.
It currently supports the Gemini, Gopher and Finger protocols.

%prep
%setup -q

%build
make %{?_smp_mflags} PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/{16x16,32x32,64x64,128x128}/apps
sed -i -e 's/update-desktop-database//g' Makefile
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/castor
%doc README.md
%license LICENSE
%{_datadir}/icons/hicolor/scalable/apps/org.typed-hole.castor.svg
%{_datadir}/icons/hicolor/*/apps/org.typed-hole.castor.png
%{_datadir}/applications/Castor.desktop

%changelog
* Sun Oct 25 2020 Elagost <me@elagost.com>
- Created spec file
