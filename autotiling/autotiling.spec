Name:           autotiling
Version:        1.6
Release:        2%{?dist}
Summary:        Script for sway and i3 to automatically switch the horizontal/vertical window split orientation

License:        GPL
URL:            https://github.com/nwg-piotr/autotiling
Source0:        https://github.com/nwg-piotr/autotiling/archive/v%{version}.tar.gz

BuildRequires:  python3-devel python3-setuptools python-setuptools-wheel python3-pip python3-i3ipc python3-wheel
Requires:       python3 python3-i3ipc

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
%{_usr}/lib/python3.10/site-packages/autotiling/*
%{_usr}/lib/python3.10/site-packages/autotiling-%{version}.dist-info/*

%changelog
* Thu Aug 11 2022 Adam Thiede <adamj@mailbox.org>
- initial spec
