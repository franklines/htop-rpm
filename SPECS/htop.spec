Name:    htop
Version: 2.2.0
Release: 2%{?dist}
Summary: htop process viewer tool for Unix.

License: GPLv2
URL: https://github.com/hishamhm/%{name}
Source0: %{name}-%{version}.tar.gz

BuildRequires: ncurses-devel 

%description
This is htop, an interactive process viewer for Unix systems. It is a text-mode application (for console or X terminals) and requires ncurses. 

%prep
%setup -q

%build
./configure --prefix=/opt/%{name}
make 

%install
rm -rf ${RPM_BUILD_ROOT}
%make_install
ln -s /opt/%{name}/bin/%{name} /usr/local/bin/%{name}

%files
%doc README COPYING
/opt/%{name}

%changelog
* Sat Jan 25 2020 2.2.0
 - Solaris/Illumos/OpenIndiana support (thanks to Guy M. Broome)
 - -t/--tree flag for starting in tree-view mode (thanks to Daniel Flanagan)
 - macOS: detects High Sierra version to avoid OS bug (thanks to Pierre Malhaire)
 - OpenBSD: read battery data (thanks to @nerd972)
 - Various automake and build improvements (thanks to Kang-Che Sung)
 - Check for pkg-config when building with --enable-delayacct (thanks to @florian2833z for the report)
 - Avoid some bashisms in configure script (thanks to Jesin)
 - Use CFLAGS from ncurses*-config if present (thanks to Michael Klein)
 - Header generator supports non-UTF-8 environments (thanks to @volkov-am)
 - Linux: changed detection of kernel threads
 - Collapse current subtree pressing Backspace
 - BUGFIX: fix behavior of SYSCR column (thanks to Marc Kleine-Budde)
 - BUGFIX: obtain exit code of lsof correctly (thanks to @wangqr)
 - BUGFIX: fix crash with particular keycodes (thanks to Wellington Torrejais da Silva for the report)
 - BUGFIX: fix issue with small terminals (thanks to Daniel Elf for the report)
 - BUGFIX: fix terminal color issues (thanks to Kang-Che Sung for the report)
 - BUGFIX: preserve LDFLAGS when building (thanks to Lance Frederickson for the report)
 - BUGFIX: fixed overflow for systems with >= 100 signals 
