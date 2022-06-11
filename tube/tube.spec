Summary: Youtube CLI
Name: tube
Version: 114
Release: 1%{?dist}
License: MIT
URL: https://www.datagubbe.se/yt
Source: https://www.datagubbe.se/yt/tube%{version}.tgz

BuildRequires: python

Requires: bash
Requires: python

#%global debug_package %{nil}

%description
tube is a Python script for extracting video metadata from an arbitrary Youtube
URL and then launch a player of choice to watch the video, or pipe the output
from yt-dlp to said player.

%prep
%setup -q

%install
install -Dm755 tube %{buildroot}%{_bindir}/tube
install -Dm755 tubeshell %{buildroot}%{_bindir}/tubeshell
install -Dm644 LICENSE %{buildroot}%{_datadir}/licenses/tube/LICENSE

%files
%{_bindir}/tube
%{_bindir}/tubeshell
%doc README.md
%license LICENSE

%changelog
* Fri Jun 10 2022 Adam Thiede <me@adamthiede.com>
- Created spec file
