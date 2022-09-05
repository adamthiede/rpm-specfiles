Name:           invidtui
Version:        0.2.6
Release:        1%{?dist}
Summary:        TUI-based invidious client

License:        MIT
URL:            https://github.com/darkhz/invidtui
Source0:        https://github.com/darkhz/invidtui/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang git
Requires:       mpv ffmpeg yt-dlp

%global __brp_mangle_shebangs %{nil}
%global debug_package %{nil}

%description
invidtui is an invidious client, which fetches data from invidious instances and displays a user interface in the terminal(TUI), and allows for selecting and playing Youtube audio and video.

%prep
%autosetup


%build
go build

%install
install -Dm755 invidtui %{buildroot}/%{_bindir}/invidtui


%files
%{_bindir}/invidtui
%license LICENSE
%doc README.md



%changelog
* Tue Aug 30 2022 Adam Thiede <adamj@mailbox.org>
- update to 0.1.0

* Fri Jul 15 2022 Adam Thiede <adamj@mailbox.org>
- update to 0.0.7

* Fri Jul 15 2022 Adam Thiede <adamj@mailbox.org>
- initial
