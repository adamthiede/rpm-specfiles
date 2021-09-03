Summary: A Telegram client optimized for the GNOME desktop
Name: telegrand
Version: main
Release: 1%{?dist}
License: GPL-3.0
URL: https://github.com/melix99/telegrand
Source: https://github.com/melix99/telegrand/archive/%{version}.tar.gz

BuildRequires: gcc
BuildRequires: rust
BuildRequires: make
BuildRequires: cargo
BuildRequires: gtk3-devel
BuildRequires: gtk4-devel
BuildRequires: openssl-devel
BuildRequires: desktop-file-utils

Requires: gtk3
Requires: gtk4
Requires: desktop-file-utils

%global debug_package %{nil}

%description
A Telegram client optimized for the GNOME desktop

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
#%make_install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%files
%{_bindir}/telegrand
%doc README.md
%license LICENSE
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Thu Sep 2 2021 Elagost <mail@elagost.com>
- Created spec file
