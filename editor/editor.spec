%global uuid    org.gnome.GNOME-Text-Editor

Name:           gnome-text-editor
Version:        3.39.92
Release:        1%{?dist}
Summary:        A simple text editor

License:        GPLv3+
URL:            https://gitlab.gnome.org/GNOME/gnome-text-editor
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  libhandy-devel
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gst-editing-services-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)

Requires:       hicolor-icon-theme
Requires:       gtk3
Requires:       gtk4

%description
A simple text editor

%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*
%{_metainfodir}/*.xml


%changelog
* Mon Jul 05 2021 Adam Thiede <me@adamthiede.com> - 3.39.92-1
- Initial 
