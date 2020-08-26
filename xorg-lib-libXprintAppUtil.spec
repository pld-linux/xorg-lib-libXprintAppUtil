Summary:	XprintAppUtil library
Summary(pl.UTF-8):	Biblioteka XprintAppUtil
Name:		xorg-lib-libXprintAppUtil
Version:	1.0.1
Release:	8
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXprintAppUtil-%{version}.tar.bz2
# Source0-md5:	d2de510570aa6714681109b2ba178365
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXprintUtil-devel
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XprintAppUtil library.

%description -l pl.UTF-8
Biblioteka XprintAppUtil.

%package devel
Summary:	Header files for libXprintAppUtil library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXprintAppUtil
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXp-devel
Requires:	xorg-lib-libXprintUtil-devel
Requires:	xorg-proto-xproto-devel

%description devel
XprintAppUtil library.

This package contains the header files needed to develop programs that
use libXprintAppUtil.

%description devel -l pl.UTF-8
Biblioteka XprintAppUtil.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXprintAppUtil.

%package static
Summary:	Static libXprintAppUtil library
Summary(pl.UTF-8):	Biblioteka statyczna libXprintAppUtil
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
XprintAppUtil library.

This package contains the static libXprintAppUtil library.

%description static -l pl.UTF-8
Biblioteka XprintAppUtil.

Pakiet zawiera statyczną bibliotekę libXprintAppUtil.

%prep
%setup -q -n libXprintAppUtil-%{version}

%build
%{__libtoolize}
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXprintAppUtil.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXprintAppUtil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXprintAppUtil.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXprintAppUtil.so
%dir %{_includedir}/X11/XprintAppUtil
%{_includedir}/X11/XprintAppUtil/*.h
%{_pkgconfigdir}/xprintapputil.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXprintAppUtil.a
