Name:           pass-tomb
Version:        1.3
Release:        1%{?dist}
Summary:        store passwords in a tomb

License:        GPLv3
URL:            https://github.com/roddhjav/pass-tomb
Source0:        https://github.com/roddhjav/pass-tomb/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  make bash
Requires:       pass tomb

%description
A pass extension that helps you keep the whole tree of passwords encrypted inside a Tomb.

%prep
%autosetup


%install
%make_install

%files
%license LICENSE
%doc README.md
%{_prefix}/lib/password-store/extensions/*
%{_mandir}/man1/*
%{_datadir}



%changelog
* Tue Apr 11 2023 Adam Thiede <adamj@mailbox.org>
- 
