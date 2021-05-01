%define _disable_rebuild_configure 1
%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	BUDGIE Screensaver
Name:		budgie-screensaver
Version:	4.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Budgie
Url:		https://github.com/getsolus
Source0:	https://github.com/getsolus/budgie-screensaver/releases/download/v%{version}/budgie-screensaver-v%{version}.tar.xz

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
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xxf86misc)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xtst)

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
%setup -q -n %{name}-v%{version}
%autopatch -p1

%build
export CC=gcc
export CXX=g++
%configure \
	--disable-more-warnings

%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS
#{_sysconfdir}/pam.d/gnome-screensaver
#{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/*
#{_libexecdir}/gnome-screensaver-dialog
#{_mandir}/man1/gnome-screensaver*
