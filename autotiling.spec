Name:           autotiling
Version:        1.8
Release:        1%{?dist}
Summary:        Script for sway and i3 to automatically switch the horizontal/vertical window split orientation

License:        GPL
URL:            https://github.com/nwg-piotr/autotiling
Source0:        https://github.com/nwg-piotr/autotiling/archive/v%{version}.tar.gz

BuildRequires:  python3-devel python3-setuptools python-setuptools-wheel python3-pip python3-i3ipc python3-wheel
Requires:       python3 python3-i3ipc

%global debug_package %{nil}

%description
Script for sway and i3 to automatically switch the horizontal/vertical window split orientation

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install


%files
%doc README.md
%license LICENSE
%{_bindir}/autotiling
%{_usr}/lib/python3.11/site-packages/autotiling/*
%{_usr}/lib/python3.11/site-packages/autotiling-%{version}.dist-info/*

%changelog
* Thu Jan 18 2023 Adam Thiede <me@adamthiede.com>
- v1.8

* Thu Aug 11 2022 Adam Thiede <me@adamthiede.com>
- initial spec
