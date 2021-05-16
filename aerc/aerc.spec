Name:           aerc
Version:        0.5.2
Release:        1%{?dist}
Summary:        A pretty good email client

License:        MIT
URL:            https://aerc-mail.org/
Source0:        https://git.sr.ht/~sircmpwn/aerc/archive/%{version}.tar.gz

BuildRequires:  make
BuildRequires:  scdoc
BuildRequires:  golang

%description
aerc is an email client that runs in your terminal. It's highly efficient and extensible, perfect for the discerning hacker.

%build
%make_build DESTDIR=%{buildroot}%{_prefix} %{?_smp_mflags} PREFIX=%{buildroot}%{_prefix}

%install
%make_install DESTDIR=%{buildroot}%{_prefix} %{?_smp_mflags} PREFIX=%{buildroot}%{_prefix}

%files
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/*
%license LICENSE


%changelog
* Sun May 16 2021 Adam Thiede <me@adamthiede.com> 0.5.2-1
- Initial specfile
