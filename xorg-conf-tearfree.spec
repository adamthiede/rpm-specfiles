Name:           xorg-conf-tearfree
Version:        1.0.1
Release:        1%{?dist}
Summary:        Config files for no screen tearing on xorg

License:        GPLv3
URL:            https://linuxreviews.org/HOWTO_fix_screen_tearing

#BuildRequires:  
Requires:       xorg-x11-server-Xorg

%description
Xorg config files for AMD and Intel GPUs to enable tearfree

%install
mkdir -p %{buildroot}/etc/X11/xorg.conf.d

echo 'Section "Device"
   Identifier  "Intel Graphics"
   Driver      "intel"
   Option      "TearFree"  "true"
EndSection' > %{buildroot}/etc/X11/xorg.conf.d/20-intel-gpu-tearfree.conf

echo 'Section "Device"
   Identifier  "AMD Graphics"
   Driver      "amdgpu"
   Option      "TearFree"  "true"
EndSection' > %{buildroot}/etc/X11/xorg.conf.d/20-amd-gpu-tearfree.quirks 

echo 'Section "Device"
   Identifier  "AMD Graphics"
   Driver      "radeon"
   Option      "TearFree"  "true"
EndSection' > %{buildroot}/etc/X11/xorg.conf.d/20-radeon-gpu-tearfree.quirks 

%files
/etc/X11/xorg.conf.d/*

%changelog
* Sun Apr 23 2023 Adam Thiede <me@adamthiede.com>
- initial file
