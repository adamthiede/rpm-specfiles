Summary: monero cli wallet
Name: monero
Version: 0.17.3.2
Release: 1%{?dist}
License: GPLv2
URL: https://github.com/monero-project/monero
Source: https://github.com/monero-project/monero/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc gcc-c++ cmake pkgconf boost-devel openssl-devel zeromq-devel openpgm-devel unbound-devel libsodium-devel libunwind-devel xz-devel readline-devel ldns-devel expat-devel gtest-devel ccache doxygen graphviz qt5-linguist hidapi-devel libusbx-devel protobuf-devel protobuf-compiler systemd-devel

%description
nvramtool manipulates nvram from userspace.

%prep
%setup -q

%build
%make_build %{?_smp_mflags} PREFIX=%{_prefix}
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_bindir}
%make_install PREFIX=%{_prefix}

%files
%{_sbindir}/%{name}

%changelog
* Tue Jun 14 2022 Adam Thiede <adamj@mailbox.org> 0.17.3.2
- initial spec file

