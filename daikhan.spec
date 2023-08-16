Name:           daikhan
Version:        0
Release:        1
Summary:        A media player for the modern desktop
License:        AGPL-3.0
URL:            https://gitlab.com/daikhan/daikhan
Source0:        https://gitlab.com/daikhan/daikhan/-/archive/main/daikhan-main.tar.bz2

BuildRequires:  meson
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(vapigen)

%description
A media player for the modern desktop.

Current Features (More Planned)

Play/pause, next/prev, volume control, seeking, etc.
Audio/video/subtitle track selection
Repeat (single file / whole queue)
Remember last playback position for each file
Remember audio/video/subtitle track selection for each file
Remember player state (restore session)
Move window by dragging from the video area
Drop files into the video area to play them
Replay previous queue simply by hitting play

%prep
%autosetup -n %{name}-main -p1

%build
%meson
%meson_build

%install
%meson_install

%files
