Summary:	Konqueror's Sidebar
Name:		metabar
Version:	0.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/metabar/%{name}-%{version}.tar.gz
# Source0-md5:  cf69531eb967caac6ea42ba47513d364
#w pszysz³osci http://metabar.sourceforge.net
URL:		http://sourceforge.net/projects/metabar
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A sidebar plugin for KDE's Konqueror which shows information and
actions for selected files and directories.

%description -l pl
Wtyczka do panelu nawigacyjnego konquerora

%prep
%setup -q -n %{name}

%{__sed} -i -e 's,\$(TOPSUBDIRS),doc po src,'  Makefile.am
%{__sed} -i -e 's,\$(KDE_INCLUDES),-I$(kde_includes)/,' src/Makefile.am

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
       --enable-libsuffix=64 \
%endif
       --%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
       --with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
       DESTDIR=$RPM_BUILD_ROOT \
       kde_htmldir=%{_kdedocdir} \
       kde_libs_htmldir=%{_kdedocdir} \
       kdelnkdir=%{_desktopdir} \

%find_lang sidebar --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f sidebar.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/*
%{_datadir}/apps/*
