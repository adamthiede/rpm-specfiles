Name:           mdnf-alias
Version:        1.0
Release:        2%{?dist}
Summary:        microdnf aliases

License:        GPLv3
URL:            https://adamthiede.com

#BuildRequires:  
Requires:       microdnf

%description
microdnf shell script to add alias for 'up' and 'in', etc

%install
mkdir -p %{buildroot}/%{_bindir}
echo '#!/bin/bash
case $1 in
	"in")
		shift 1
		microdnf install $@
		;;
	"rm")
		shift 1
		microdnf remove $@
		;;
	"up")
		shift 1
		microdnf upgrade $@
		;;
	"se")
		shift 1
		microdnf search $@
		;;
	*)
		microdnf $@
		;;
esac
' > %{buildroot}/%{_bindir}/mdnf
chmod 755 %{buildroot}/%{_bindir}/mdnf

%files
%{_bindir}/mdnf

%changelog
* Sun Apr 23 2023 Adam Thiede <me@adamthiede.com>
- initial file
