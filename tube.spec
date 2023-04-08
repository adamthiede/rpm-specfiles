Summary: Youtube CLI
Name: tube
Version: 115
Release: 1%{?dist}
License: MIT
URL: https://www.datagubbe.se/yt
Source: https://www.datagubbe.se/yt/tube%{version}.tgz

BuildRequires: bash

Requires: bash
Requires: python3

%global __brp_mangle_shebangs %{nil}

%description
tube is a Python script for extracting video metadata from an arbitrary Youtube
URL and then launch a player of choice to watch the video, or pipe the output
from yt-dlp to said player.

%prep
%setup -n tube-dist

%install
install -Dm755 tube %{buildroot}%{_bindir}/tube
install -Dm755 tubeshell %{buildroot}%{_bindir}/tubeshell

%files
%{_bindir}/tube
%{_bindir}/tubeshell
%doc README

%changelog
* Fri Jun 10 2022 Adam Thiede <me@adamthiede.com>
- Created spec file
