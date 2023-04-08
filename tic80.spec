Name:           tic80
Version:        1.0.2164
Release:        1%{?dist}
Summary:        Tiny Fantasy Computer

License:        MIT
URL:            tic80.com
Source0:        https://github.com/nesbox/TIC-80/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ make ruby rubygem-tk rubygem-tk-doc rubygem-rake rubygem-test-unit cmake libglvnd-devel libglvnd-gles freeglut-devel clang libXext-devel SDL_sound pipewire-devel pipewire-jack-audio-connection-kit-devel pulseaudio-libs-devel

Requires:       SDL2

%description
TIC-80 is a free and open source fantasy computer for making, playing and sharing tiny games.

%prep
%setup -n TIC-80-%{version}


%build
#cd build && cmake .. -DCMAKE_CXX_COMPILER=clang++ -DSDL_ALSA=On && make -j$(nproc)
cd build
cmake .. -DBUILD_PRO=On -DSDL_ALSA=On
make -j$(nproc)

%install
%make_install


%files
%license LICENSE
%doc README.md



%changelog
* Sat Aug 13 2022 Adam Thiede <adamj@mailbox.org>
- initial
