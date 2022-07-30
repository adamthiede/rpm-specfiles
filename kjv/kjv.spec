Name:           kjv
Version:        master
Release:        1%{?dist}
Summary:        read the Bible from your terminal.

License:        Unlicense
URL:            https://github.com/LukeSmithxyz/kjv
Source0:        https://github.com/LukeSmithxyz/kjv/archive/refs/heads/master.tar.gz

BuildRequires:  make
Requires:       bash less sed

%global __brp_mangle_shebangs %{nil}

%description
Read the Word of God from your terminal
Forked from https://github.com/bontibon/kjv.git but with the Apocrypha added.

%prep
%autosetup

%install
%make_install PREFIX='/usr/'

%files
%{_bindir}/kjv
%license LICENSE
%doc README.md



%changelog
* Sat Jul 30 2022 Adam Thiede <adamj@mailbox.org>
- 
