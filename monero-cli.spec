
%define MajorVersion 0.18

Name:           monero-cli
Version:        %{MajorVersion}.2.0
Release:        1%{?dist}
Summary:        Monero CLI wallet

License:        BSD
URL:            https://github.com/monero-project/monero
Source0:        https://github.com/monero-project/monero/archive/refs/heads/release-v%{MajorVersion}.tar.gz

BuildRequires:  gcc gcc-c++ cmake pkgconf boost-devel openssl-devel zeromq-devel openpgm-devel unbound-devel libsodium-devel libunwind-devel xz-devel readline-devel expat-devel gtest-devel ccache doxygen graphviz qt5-linguist hidapi-devel libusbx-devel protobuf-devel protobuf-compiler systemd-devel git
Requires:       glibc

%description
Monero CLI wallet

%prep
%setup -n monero-release-v%{MajorVersion}

%build
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md

%changelog
* Sun Apr 09 2023 Adam Thiede <adamj@mailbox.org>
- initial
