Summary: a Gemini Project client written in Rust with NCurses
Name: asuka
Version: 0.8.1
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
#make %{?_smp_mflags} PREFIX=%{_prefix}
cargo build --release

%install
mkdir -p %{buildroot}/%{_bindir}
install -D target/release/asuka %{buildroot}/%{_bindir}/asuka
#%make_install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%files
%{_bindir}/asuka
%doc README.md
%license LICENSE

%changelog
* Sun Oct 25 2020 Elagost <me@elagost.com>
- Created spec file
