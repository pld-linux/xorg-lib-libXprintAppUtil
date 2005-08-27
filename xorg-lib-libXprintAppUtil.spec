Summary:	XprintAppUtil library
Summary(pl):	Biblioteka XprintAppUtil
Name:		xorg-lib-libXprintAppUtil
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXprintAppUtil-%{version}.tar.bz2
# Source0-md5:	1944c200ed6a7bd668ed6d200731a963
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXprintUtil-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/libXprintAppUtil-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XprintAppUtil library.

%description -l pl
Biblioteka XprintAppUtil.

%package devel
Summary:	Header files libXprintAppUtil development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXprintAppUtil
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXprintUtil-devel

%description devel
XprintAppUtil library.

This package contains the header files needed to develop programs that
use these libXprintAppUtil.

%description devel -l pl
Biblioteka XprintAppUtil.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXprintAppUtil.

%package static
Summary:	Static libXprintAppUtil library
Summary(pl):	Biblioteka statyczna libXprintAppUtil
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
XprintAppUtil library.

This package contains the static libXprintAppUtil library.

%description static -l pl
Biblioteka XprintAppUtil.

Pakiet zawiera statyczn± bibliotekê libXprintAppUtil.

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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libXprintAppUtil.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXprintAppUtil.so
%{_libdir}/libXprintAppUtil.la
%{_includedir}/X11/XprintAppUtil/*.h
%{_pkgconfigdir}/xprintapputil.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXprintAppUtil.a
