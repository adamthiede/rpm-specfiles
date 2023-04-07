Summary: terraform-docs
Name: terraform-docs
Version: 0.16.0
Release: 1%{?dist}
License: MIT
URL: https://github.com/terraform-docs/terraform-docs
Source: https://github.com/terraform-docs/terraform-docs/archive/v%{version}.tar.gz

BuildRequires: make
BuildRequires: git
BuildRequires: gcc
# suse package: go
# fedora/rhel package: golang
%if 0%{?suse_version}
BuildRequires: go
%endif
%if 0%{?fedora}
BuildRequires: golang
%endif
%if 0%{?rhel}
BuildRequires: golang
%endif

Requires: ncurses-base

%global debug_package %{nil}

%description
Automate your infrastructure

%prep
%setup -q

%build
#sed -i -e 's,go 1.17,go 1.16,' go.mod
#sed -i -e 's,go-tfe v0.19.1-.*$,go-tfe v0.22.0,' go.mod
#sed -i -e '/sigs.k8s.io\/json/d' go.mod
#go mod download github.com/hashicorp/go-tfe
%make_build PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_bindir}
go build
cp terraform-docs %{buildroot}%{_bindir}

%files
%{_bindir}/terraform-docs
%doc README.md
%license LICENSE

%changelog
* Sun Aug 07 2022 Adam Thiede <adamj@mailbox.org> 1.2.6
- v1.2.6
* Thu May 26 2022 Adam Thiede <adamj@mailbox.org> 1.2.1
- v1.2.1
* Fri May 20 2022 Adam Thiede <adamj@mailbox.org> 1.2.0
- v1.2.0
* Fri Apr 22 2022 Adam Thiede <adamj@mailbox.org> 1.1.9
- v1.1.9
* Sun Apr 3 2022 Adam Thiede <adamj@mailbox.org> 1.1.8
- v1.1.8
* Wed Jan 19 2022 Adam Thiede <adamj@mailbox.org> 1.1.4
- v1.1.4
* Sat Jan 15 2022 Adam Thiede <adamj@mailbox.org> 1.1.3
- v1.1.3
* Sat Nov 6 2021 Adam Thiede <adamj@mailbox.org> 1.0.10
- Initial 
