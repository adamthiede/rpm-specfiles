# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/gokcehan/lf
%global goipath         github.com/gokcehan/lf
Version:                r26
%global tag             r26

%gometa

%global common_description %{expand:
Terminal file manager.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Terminal file manager

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/lf %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sun Mar 13 2022 Elagost <me@elagost.com> - r26-1
- Initial package
