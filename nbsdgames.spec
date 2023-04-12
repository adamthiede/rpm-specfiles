Name:           nbsdgames
Version:        5
Release:        1%{?dist}
Summary:        A package of 18 text-based modern games

License:        CC0
URL:            https://github.com/abakh/nbsdgames
Source0:        https://github.com/abakh/nbsdgames/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  git make gcc ncurses-devel
Requires:       ncurses

%description
A package of 18 text-based modern games

%prep
%autosetup


%build
%make_build

%install
export GAMES_DIR=%{buildroot}/usr/games
mkdir -p %{buildroot}/usr/games
%make_install
rm -rf %{buildroot}/usr/lib/debug/usr/games/*

%files
%license LICENSE
%doc README.md
/usr/games/*



%changelog
* Tue Apr 11 2023 Adam Thiede <adamj@mailbox.org>
- 
