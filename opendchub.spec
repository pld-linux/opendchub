#
# Note:
# - works very unstable at axp (other not tested)
#
Summary:	Direct Connect Hub
Summary(pl):	Serwer Direct Connect
Name:		opendchub
Version:	0.7.15
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/opendchub/%{name}-%{version}.tar.gz
# Source0-md5:	8f9ab5bb7f85730f4b1ce7cceb6aef96
Source1:	%{name}.init
Patch0:		%{name}-bufoverflow.patch
Patch1:		%{name}-no_nsl.patch
URL:		http://opendchub.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libcap-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(postun,pre):	/usr/sbin/usermod
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
Provides:	group(clamav)
Provides:	user(clamav)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Opendchub is a hub of direct connect file sharing network.

%description -l pl
Opendchub jest hubem sieci direct connect s³u¿±cej do wymiany plików.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-switch_user

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/opendchub
install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 190 opendchub
%useradd -u 190 -d /etc/opendchub -s /bin/false -c "Open DC Hub" -g opendchub opendchub

%post
/sbin/chkconfig --add opendchub
%service opendchub restart "Open DC Hub"

%preun
if [ "$1" = "0" ]; then
        %service opendchub stop
        /sbin/chkconfig --del opendchub
fi

%postun
if [ "$1" = "0" ]; then
        %userremove opendchub
        %groupremove opendchub
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README Documentation/* Samplescripts
%attr(755,root,root) %{_bindir}/*
%attr(754,root,root) /etc/rc.d/init.d/opendchub
%dir %attr(750,opendchub,opendchub) %{_sysconfdir}/opendchub
