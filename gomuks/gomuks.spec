Summary: A terminal based Matrix client written in Go
Name: gomuks
Version: master
Release: 2%{?dist}
License: AGPLv3
URL: https://github.com/tuli/gomuks
Source: https://github.com/tulir/gomuks/archive/master.tar.gz

BuildRequires: make
BuildRequires: git
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libolm-devel
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
%setup -q

%build
#sed -i go.mod -e 's/^go 1.17/go 1.16/'
go mod tidy
go build

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/gomuks
#%{_docdir}/%{name}/README.md
%doc README.md
%license LICENSE

%changelog
* Thu Mar 10 2022 Elagost <me@elagost.com> - 0.2.5-1
- Initial package
