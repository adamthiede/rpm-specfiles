Name:           rbw
Version:        1.7.1
Release:        1%{?dist}
Summary:        rust bitwarden cli client

License:        MIT
URL:            https://github.com/doy/rbw
Source0:        https://github.com/doy/rbw/archive/refs/tags/%{version}.tar.gz

BuildRequires:  rust cargo
Requires:       pinentry

# I don't need this.
%global debug_package %{nil}

%description
rust bitwarden cli client

%prep
%autosetup

%build
cargo build --release --locked
cargo run --release --locked --bin rbw -- gen-completions bash >bash-completions

%install
install -Dm 755 target/release/rbw -t "%{buildroot}/%{_bindir}/"
install -Dm 755 target/release/rbw-agent -t "%{buildroot}/%{_bindir}/"
install -Dm 644 bash-completions "%{buildroot}/%{_datadir}/bash-completion/completions/rbw"

%files
%license LICENSE
%doc README.md
%{_datadir}/bash-completion/completions/rbw
%{_bindir}/rbw
%{_bindir}/rbw-agent

%changelog
* Sun Apr 30 2023 Adam Thiede <me@adamthiede.com>
- 
