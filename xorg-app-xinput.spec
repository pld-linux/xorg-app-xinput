Summary:	xinput application - allows configuration and testing of XInput devices
Summary(pl.UTF-8):	Aplikacja xinput pozwalająca na konfigurację i testowanie urządzeń XInput
Name:		xorg-app-xinput
Version:	1.3.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/archive/individual/app/xinput-%{version}.tar.bz2
# Source0-md5:	977d657e8d7b59f7d82c98ebef444b28
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xinput
%{_mandir}/man1/xinput.1x*
