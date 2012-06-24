#
# Note:
# - works very unstable at axp (other not tested)
#
Summary:	Direct Connect Hub
Summary(pl):	Serwer Direct Connect
Name:		opendchub
Version:	0.7.14
Release:	3
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/opendchub/%{name}-%{version}.tar.gz
# Source0-md5:	6121347154820e2b307a5aecafa86ce8
Patch0:		%{name}-bufoverflow.patch
URL:		http://opendchub.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-devel
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Opendchub is a hub of direct connect file sharing network.

%description -l pl
Opendchub jest hubem sieci direct connect s�u��cej do wymiany plik�w.

%prep
%setup -q
%patch0 -p1

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
