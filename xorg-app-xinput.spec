Summary:	xinput application - allows configuration and testing of XInput devices
Summary(pl.UTF-8):	Aplikacja xinput pozwalająca na konfigurację i testowanie urządzeń XInput
Name:		xorg-app-xinput
Version:	1.6.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/archive/individual/app/xinput-%{version}.tar.bz2
# Source0-md5:	6a889412eff2e3c1c6bb19146f6fe84c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel >= 1.6.0
BuildRequires:	xorg-proto-inputproto-devel >= 2.1.99.1
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXi >= 1.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility to configure and test XInput devices.

%description -l pl.UTF-8
Narzędzie do konfiguracji i testowania urządzeń XInput.

%prep
%setup -q -n xinput-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xinput
%{_mandir}/man1/xinput.1*
