Name:           plotinus
Version:        0.2.0
Release:        1%{?dist}
Summary:        GTK Command Palette
License:        GPL-3.0-or-later
URL:            https://github.com/p-e-w/plotinus
Source:         https://github.com/p-e-w/plotinus/archive/%{version}.tar.gz
BuildRequires:  gtk3-devel vala cmake
BuildRequires:  gtk3

%global debug_package %{nil}

%description
Command Palette for  GTK3 applications

%prep
%setup -q

%build
mkdir build
cd build
%cmake build ..
make %{?_smp_mflags} PREFIX=%{_prefix}
pwd
sleep 3

%install
cd build
make install PREFIX=%{_prefix}
pwd
sleep 3

%files
%{_bindir}/%{name}
%dir %{_prefix}/lib/%{name}

%changelog
* Sat Oct 17 2020 Elagost <me@elagost.com>
- Created spec file
