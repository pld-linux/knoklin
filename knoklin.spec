Summary:	DCT3 flasher for Linux
Summary(pl.UTF-8):	Flasher DCT3 pod Linuksa
Name:		knoklin
Version:	1.0.0
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://zope.achterklap.nl:8080/nokia/sub_250software/sub_knoklin/%{name}-%{version}.tar.gz
# Source0-md5:	5319596bd01ba144e2a8ef10711c8ca9
URL:		http://zope.achterklap.nl:8080/nokia/sub_250software/sub_knoklin/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Knok for Linux is a DCT3 flasher for Linux. It is a port of the source
of KNOK.

%description -l pl.UTF-8
Knok dla Linuksa jest flasherem DCT3 pod Linuksa. Jest on oparty na
źródle KNOK-a.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/cmd $RPM_BUILD_ROOT%{_bindir}
install src/sendcode $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog readme.txt TODO
%attr(755,root,root) %{_bindir}/*
