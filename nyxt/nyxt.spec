Summary: Nyxt is a keyboard-oriented, infinitely extensible web browser designed for power users.
Name: nyxt
Version: 2.0.0
Release: 1%{?dist}
License: BSD
URL: https://github.com/atlas-engineer/nyxt
Source: https://github.com/atlas-engineer/nyxt/archive/refs/tags/%{version}.tar.gz

BuildRequires: make

Requires: gtk3

%global debug_package %{nil}

%description
Nyxt is a keyboard-oriented, infinitely extensible web browser designed for power users.


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
* Thu May 20 2021 Elagost <me@elagost.com>
- Created spec file
