Summary: A terminal based Matrix client written in Go
Name: gomuks
Version: 0.2.5
Release: 1%{?dist}
License: AGPLv3 and MPLv2.0
URL: https://github.com/elagost/gomuks
Source: https://github.com/elagost/gomuks/archive/v%{version}.tar.gz

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
A terminal Matrix client written in Go using mautrix and mauview

%prep

%build
go build

%install
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_bindir}
install -Dm755 gomuks "%{buildroot}%{_bindir}/gomuks"
install -Dm644 README.md "%{buildroot}%{_docdir}%{name}/README.md"

%files
%{_bindir}/gomuks
%{_docdir}%{name}/README.md
%doc README.md
%license LICENSE

%changelog
* Thu Mar 10 2022 Elagost <me@elagost.com> - 0.2.5-1
- Initial package
