Summary: a commandline interface for libsignal-service-java 
Name: signal-cli 
Version: 0.10.8
Release: 1%{?dist}
License: GPL
URL: https://github.com/AsamK/signal-cli
Source: https://github.com/AsamK/signal-cli/archive/v%{version}.tar.gz

BuildRequires: java-11-openjdk-devel
Requires: java-11-openjdk

%global debug_package %{nil}

%description

%prep
%setup -q

%build
PREFIX=%{buildroot}%{_prefix} ./gradlew build

%install
PREFIX=%{buildroot}%{_prefix} ./gradlew installDist
install -D build/install/signal-cli/bin/signal-cli %{buildroot}%{_bindir}/signal-cli
mkdir -p %{buildroot}%{_libdir}
cp build/install/signal-cli/lib/* %{buildroot}%{_libdir}/

%files
%{_bindir}/signal-cli
%{_libdir}/*
%doc README.md
%license LICENSE

%changelog
* Sun Oct 25 2020 Elagost <me@elagost.com>
- Created spec file
