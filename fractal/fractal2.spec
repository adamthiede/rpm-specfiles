%global uuid    org.gnome.Fractal

Name:           fractal
Version:        4.4.0
Release:        1%{?dist}
Summary:        Matrix messaging app for GNOME written in Rust

License:        GPLv3+
URL:            https://gitlab.gnome.org/GNOME/fractal
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gmp-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  rust
BuildRequires:  pkgconfig(atk)
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
BuildRequires:  pkgconfig(libhandy-0.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)

Requires:       hicolor-icon-theme

Conflicts:      fractal-master

%description
Fractal is a Matrix messaging app for GNOME written in Rust. Its interface is
optimized for collaboration in large groups, such as free software projects.


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
* Fri Aug 07 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 4.4.0-1
- Update to 4.4.0

* Sun Jan 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 4.2.2-1
- Update to 4.2.2

* Sat Sep 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 4.2.1-1
- Update to 4.2.1

* Sun Jul 28 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 4.2.0-1.20190727git65ed458
- Update 4.2.0

* Wed May 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 4.0.0-1.20190514git7925a33
- Initial package
