Summary: a Gemini browser for your terminal
Name: amfora
Version: 1.8.0
Release: 1%{?dist}
License: GPLv3
URL: https://github.com/makeworld-the-better-one/amfora
Source: https://github.com/makeworld-the-better-one/amfora/archive/v%{version}.tar.gz

BuildRequires: make
BuildRequires: git
BuildRequires: gcc
BuildRequires: golang

Requires: ncurses-base

%description
Amfora aims to be the best looking Gemini client with the most features...
all in the terminal.

%prep
%setup -q

%build
%make_build %{?_smp_mflags} BUILDER="official-rpm" PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications/
%make_install PREFIX=%{buildroot}%{_prefix}

%files
%{_bindir}/amfora
%{_datadir}/applications/amfora.desktop
%doc README.md
%license LICENSE

%changelog
* Mon Oct 4 2021 Adam Thiede <adamj@mailbox.org> 1.8.0
- Copy spec to "amfora_fedora.spec" to comply with Fedora-specific packaging rules

* Sun Oct 3 2021 Adam Thiede <adamj@mailbox.org> 1.8.0
- Updated version and cleaned spec file for upload

* Sun Nov 29 2020 Adam Thiede <adamj@mailbox.org> 1.6.0
- Created spec file
