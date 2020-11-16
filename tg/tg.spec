Name:           tg
Version:        0.6.0
Release:        1%{?dist}
Summary:        Telegram terminal client.
License:        Unlicense
Group:          Networking
URL:            https://github.com/paul-nameless/tg
Source:         https://github.com/paul-nameless/tg/archive/v%{version}.tar.gz
BuildRequires:  gtk3-devel, gcc, python, python3-pip

%global debug_package %{nil}

%description
Telegram terminal client.

%prep
%setup -q

%build
PREFIX=%{_prefix} pip install python-telegram -t %{buildroot}%{_datadir}

%install
PREFIX=%{_prefix} pip install . -t %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_bindir}
cp %{buildroot}%{_datadir}/bin/tg %{buildroot}%{_bindir}/

%files
%{_datadir}/tg/*
%{_datadir}/bin/tg
%{_bindir}/tg
%{_datadir}/telegram/*
%{_datadir}/tg-0.6.0.dist-info/*
%{_datadir}/python_telegram-0.12.0-py3.9.egg-info/*

%changelog
* Mon Nov 16 2020 Elagost <me@elagost.com>
- Created spec file
