Name:           sway-session-custom
Version:        1.0.0
Release:        1%{?dist}
Summary:        custom sway desktop file for silverblue

License:        GPLv3
URL:            https://github.com/swaywm/sway/issues/7519

#BuildRequires:  
Requires:       sway

%description
Adds WLR_DRM_NO_ATOMIC=1 to sway config file.

%install
mkdir -p %{buildroot}/%{_datadir}/wayland-sessions/

echo '[Desktop Entry]
Name=Sway Custom
Comment=An i3-compatible Wayland compositor
Exec=env WLR_DRM_NO_ATOMIC=1 sway
Type=Application' > %{buildroot}/%{_datadir}/wayland-sessions/sway-custom.desktop

%files
%{_datadir}/wayland-sessions/sway-custom.desktop

%changelog
* Thu Apr 27 2023 Adam Thiede <me@adamthiede.com>
- initial file
