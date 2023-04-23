Summary: a Gemini Project client written in Rust with NCurses
Name: asuka
Version: 0.8.5
Release: 1%{?dist}
License: MIT
URL: https://git.sr.ht/~julienxx/asuka
Source: https://git.sr.ht/~julienxx/asuka/archive/%{version}.tar.gz

BuildRequires: rust
BuildRequires: make
BuildRequires: cargo
BuildRequires: openssl-devel
BuildRequires: ncurses-devel

Requires: ncurses-base

%global debug_package %{nil}

%description
asuka is a Gemini Project client written in Rust with NCurses.

%prep
%setup -q

%build
cargo build --release

%install
mkdir -p %{buildroot}/%{_bindir}
install -D target/release/asuka %{buildroot}/%{_bindir}/asuka

%files
%{_bindir}/asuka
%doc README.md
%license LICENSE

%changelog
* Sun Sep 25 2022 Adam Thiede <me@adamthiede.com>
- 0.8.5

* Sun Oct 3 2021 Adam Thiede <me@adamthiede.com>
- Created spec file
