#
# Note:
# - works very unstable at axp (other not tested)
#
Summary:	Direct Connect Hub
Summary(pl):	Serwer Direct Connect
Name:		opendchub
Version:	0.7.14
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	6121347154820e2b307a5aecafa86ce8
URL:		http://opendchub.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-devel
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Opendchub is a hub of direct connect file sharing network.

%description -l pl
Opendchub jest hubem sieci direct connect s³u¿±cej do wymiany plików. 

%prep
%setup -q

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
%doc AUTHORS ChangeLog NEWS README Documentation/* Samplescripts
%attr(755,root,root) %{_bindir}/*
