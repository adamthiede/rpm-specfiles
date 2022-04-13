Summary: a cross-platform, terminal-based audio engine
Name: musikube
Version: 0.97.0
Release: 1%{?dist}
License: BSD
URL: https://github.com/clangen/musikcube
Source: %{url}/archive/%{version}.tar.gz

BuildRequires: make gcc-c++ cmake boost-devel libogg-devel libvorbis-devel ffmpeg-devel ncurses-devel zlib-devel alsa-lib-devel pulseaudio-libs-devel libcurl-devel libmicrohttpd-devel lame-devel libev-devel taglib-devel openssl-devel libopenmpt-devel

Requires: ncurses-base ffmpeg

%description
a cross-platform, terminal-based audio engine, library, player and server written in c++.

%prep
%setup -q
cmake -G "Unix Makefiles" .

%make_build %{?_smp_mflags} PREFIX=%{_prefix}
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_bindir}
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/musikube
%{_datadir}/musikube/*
%doc README.md
%license LICENSE.txt

%changelog
* Wed Nov 10 2021 Adam Thiede <adamj@mailbox.org> 0.96.7
- Initial Version
