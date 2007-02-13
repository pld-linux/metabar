Summary:	Konqueror's Sidebar
Summary(pl.UTF-8):	Panel nawigacyjny dla Konquerora
Name:		metabar
Version:	0.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/metabar/%{name}-%{version}.tar.gz
# Source0-md5:	4f43f62b831e343e8598e9d130c21699
# http://metabar.sourceforge.net/ in future
URL:		http://sourceforge.net/projects/metabar/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdebase-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	unsermake >= 040805
Requires:	konqueror
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A sidebar plugin for KDE's Konqueror which shows information and
actions for selected files and directories.

%description -l pl.UTF-8
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
%attr(755,root,root) %{_libdir}/kde3/konqsidebar_metabar.so
%{_libdir}/kde3/konqsidebar_metabar.la
%{_datadir}/apps/konqsidebartng/add/*.desktop
%{_datadir}/apps/konqsidebartng/entries/*.desktop
