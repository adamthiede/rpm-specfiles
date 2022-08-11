Name:           autotiling
Version:        1.6
Release:        1%{?dist}
Summary:        Script for sway and i3 to automatically switch the horizontal/vertical window split orientation

License:        GPL
URL:            https://github.com/nwg-piotr/autotiling
Source0:        https://github.com/nwg-piotr/autotiling/archive/v%{version}.tar.gz

BuildRequires:  python3 python3-pip python3-i3ipc
Requires:       python3 python3-i3ipc

%description
Script for sway and i3 to automatically switch the horizontal/vertical window split orientation

%prep
%autosetup

python3 setup.py build

python3 setup.py install --prefix=%{buildroot}/usr


%files
%{_bindir}/autotiling
%{_usr}/lib/python3.10/site-packages/autotiling-%{version}-py3.10.egg
%license LICENSE
%doc README.md

%changelog
* Thu Aug 11 2022 Adam Thiede <adamj@mailbox.org>
- initial spec
