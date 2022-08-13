Name:           tic80
Version:        1.0.2164
Release:        1%{?dist}
Summary:        Tiny Fantasy Computer

License:        MIT
URL:            tic80.com
Source0:        https://github.com/nesbox/TIC-80/releases/download/v%{version}/tic80-v1.0-linux.zip

BuildRequires:  make unzip

Requires:       SDL2

%description
TIC-80 is a free and open source fantasy computer for making, playing and sharing tiny games.

%prep
%setup -c -n tic80

install -Dm755 tic80 %{buildroot}/usr/bin/tic80

%files
%{_bindir}/tic80



%changelog
* Sat Aug 13 2022 Adam Thiede <adamj@mailbox.org>
- initial
