Name:           starlabs-touchpadquirks
Version:        1.19
Release:        1%{?dist}
Summary:        Star Labs laptop touchpad quirks

License:        MIT
URL:            https://github.com/StarLabsLtd/touchpad
Source0:        https://github.com/StarLabsLtd/touchpad/archive/refs/heads/%{version}.zip

#BuildRequires:  
Requires:       libinput xorg-x11-server-Xorg

%description
Quirks for Star Labs laptop touchpads

%prep
%setup -n touchpad-%{version}

%install
install -Dm644 etc/X11/xorg.conf.d/40-starlabs.conf %{buildroot}/etc/X11/xorg.conf.d/40-starlabs.conf
install -Dm644 usr/share/libinput/31-vendor-starlabs.quirks %{buildroot}/usr/share/libinput/31-vendor-starlabs.quirks 

%files
%doc README.md
/etc/X11/xorg.conf.d/40-starlabs.conf
/usr/share/libinput/31-vendor-starlabs.quirks 

%changelog
* Fri Apr 07 2023 Adam Thiede <adamj@mailbox.org>
- 
