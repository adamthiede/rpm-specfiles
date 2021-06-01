Name:           helix
Version:        0.0.6
Release:        1%{?dist}
Summary:        A pretty good email client

License:        MPL-2.0
URL:            https://helix-editor.com/
Source0:        https://github.com/helix-editor/helix/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  rust
BuildRequires:  cargo

%description
A kakoune / neovim inspired editor, written in Rust.

%build
%make_build

%install
%make_install DESTDIR=%{buildroot}%{_prefix} %{?_smp_mflags} PREFIX=%{buildroot}%{_prefix}

%files
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/*
%license LICENSE


%changelog
* Tue June 01 2021 Adam Thiede <me@adamthiede.com> 0.0.6-1
- Initial specfile
