Summary:  GTK and Python based, system performance and usage monitoring tool
Name: system-monitoring-center
Version: 1.8.0
Release: 1%{?dist}
License: GPL
URL: https://github.com/hakandundar34coding/%{name}
Source: %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: gtk3-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: gtk3
Requires: python
Requires: python3-cairo
Requires: python3-gobject
Requires: python3-beautifulsoup4
Requires: dmidecode
Requires: util-linux
Requires: iproute2

%description
GTK and Python based, system performance and usage monitoring tool

%prep
%setup -q

%build
python3 ./setup.py build

%install
#DESTDIR=%{buildroot}/ make install
python3 ./setup.py install --root="%{buildroot}" --optimize=1 --skip-build

%files
%{_bindir}/system-monitoring-center
%license LICENSE
%doc README.md

%changelog
* Thu Apr 21 2022 Adam Thiede <adamj@mailbox.org>
- Created spec file

