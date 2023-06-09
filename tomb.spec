Name:           tomb
Version:        2.9
Release:        1%{?dist}
Summary:        the Crypto Undertaker 

License:        GPLv3
URL:            https://github.com/dyne/Tomb/
Source0:        https://github.com/dyne/Tomb/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  make
Requires:       sudo cryptsetup pinentry gnupg zsh

%description
A minimalistic commandline tool to manage encrypted volumes aka The Crypto Undertaker

%prep
%setup -n Tomb-%{version}

%install
%make_install PREFIX=/usr 

%files
%{_bindir}/tomb
%{_mandir}/man1/tomb.1.gz
%license COPYING
%doc README.md

%changelog
* Wed May 03 2023 Adam Thiede <me@adamthiede.com>
- 
