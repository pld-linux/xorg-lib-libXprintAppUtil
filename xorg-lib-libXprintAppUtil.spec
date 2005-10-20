Summary:	XprintAppUtil library
Summary(pl):	Biblioteka XprintAppUtil
Name:		xorg-lib-libXprintAppUtil
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/lib/libXprintAppUtil-%{version}.tar.bz2
# Source0-md5:	6b043a10e31d6ed0381d572d3334fdc5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXprintUtil-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%dir %{_includedir}/X11/XprintAppUtil
%{_includedir}/X11/XprintAppUtil/*.h
%{_pkgconfigdir}/xprintapputil.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXprintAppUtil.a
