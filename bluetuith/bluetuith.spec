Name:           bluetuith
Version:        0.0.7
Release:        1%{?dist}
Summary:        TUI-based bluetooth connection manager

License:        MIT
URL:            https://github.com/darkhz/bluetuith
Source0:        https://github.com/darkhz/bluetuith/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  bluez-libs-devel dbus-devel golang git
Requires:       bluez dbus

%global __brp_mangle_shebangs %{nil}
%global debug_package %{nil}

%description
bluetuith is a TUI-based bluetooth connection manager, which can interact with bluetooth adapters and devices. It aims to be a replacement to most bluetooth managers, like blueman.


%prep
%autosetup


%build
go build

%install
install -Dm755 bluetuith %{buildroot}/%{_bindir}/bluetuith


%files
%{_bindir}/bluetuith
%license LICENSE
%doc README.md



%changelog
* Fri Jul 15 2022 Adam Thiede <adamj@mailbox.org>
- update to 0.0.7

* Fri Jul 15 2022 Adam Thiede <adamj@mailbox.org>
- initial
