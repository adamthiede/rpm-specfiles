Name:           aerc
Version:        0.8.2
Release:        1%{?dist}
Summary:        A pretty good email client

License:        MIT
URL:            https://aerc-mail.org/
Source0:        https://git.sr.ht/~rjarry/aerc/archive/%{version}.tar.gz

BuildRequires:  git
BuildRequires:  make
BuildRequires:  scdoc
BuildRequires:  golang

%global debug_package %{nil}

%description
aerc is an email client that runs in your terminal. It's highly efficient and extensible, perfect for the discerning hacker.

%prep
%setup -q

%build
echo "---MAKE START---"
%make_build
echo "---MAKE END---"
#%make_build DESTDIR=%{buildroot}%{_prefix} %{?_smp_mflags} PREFIX=%{buildroot}%{_prefix}

%install
echo "---INSTALL START---"
%make_install
#cd %{buildroot} && make install DESTDIR=%{buildroot}%{_prefix} %{?_smp_mflags} PREFIX=%{buildroot}%{_prefix}
echo "---INSTALL END---"


%files
%{_prefix}/local/share/aerc
%{_prefix}/local/bin/aerc
%license LICENSE


%changelog
* Sun Mar 20 2022 Adam Thiede <me@adamthiede.com> 0.8.2-1
- version update

* Sun May 16 2021 Adam Thiede <me@adamthiede.com> 0.5.2-1
- Initial specfile
