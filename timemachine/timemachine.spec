Summary: rsync backup solution
Name: linux-timemachine
Version: 1.3.2
Release: 1%{?dist}
License: MIT
URL: https://github.com/cytopia/linux-timemachine
Source: https://github.com/cytopia/linux-timemachine/archive/v%{version}.tar.gz

BuildRequires: make
Requires: rsync bash

%global debug_package %{nil}

%description
Rsync-based OSX-like time machine for Linux, MacOS and BSD for atomic and resumable local and remote backups

%prep
%setup -q

%install
sed -i Makefile -e 's,/usr/local/,/usr/,g'
make install

%files
%{_bindir}/timemachine
%doc README.md
%license LICENSE

%changelog
* Sat Mar 04 2023 Adam Thiede <adamj@mailbox.org> 1.3.2
- Initial 
