%define _disable_rebuild_configure 1
%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	BUDGIE Screensaver
Name:		budgie-screensaver
Version:	5.1.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Budgie
Url:		https://github.com/BuddiesOfBudgie/
Source0:	https://github.com/BuddiesOfBudgie/budgie-screensaver/releases/download/v%{version}/budgie-screensaver-v%{version}.tar.xz

BuildRequires:  meson
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pam-devel
BuildRequires:	xmlto
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libgnomekbdui)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xxf86misc)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xtst)
BuildRequires:  glibc-static-devel

Requires:	xsltproc
Requires:	dbus-x11
Suggests:	mandriva-theme-screensaver

%description
gnome-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.
It is designed to support:

* the ability to lock down configuration settings
* translation into other languages
* user switching

%prep
%autosetup -p1

%build
%meson

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc README.md AUTHORS
%{_sysconfdir}/pam.d/budgie-screensaver
%{_datadir}/applications/budgie-screensaver.desktop
%{_bindir}/*
%{_libexecdir}/budgie-screensaver-dialog
%{_mandir}/man1/budgie-screensaver-command.1.*
%{_mandir}/man1/budgie-screensaver.1.*
