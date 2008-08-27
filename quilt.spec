Summary:	Scripts for working with series of patches
Summary(pl.UTF-8):	Skrypty do pracy z zestawem łatek
Name:		quilt
Version:	0.47
Release:	0.1
Epoch:		0
License:	GPL v2+
Group:		Applications/Text
Source0:	http://savannah.nongnu.org/download/quilt/%{name}-%{version}.tar.gz
# Source0-md5:	d33d2442bd34387260b1c1db3e623af0
URL:		http://savannah.nongnu.org/projects/quilt/
BuildRequires:	gettext-devel
BuildRequires:	perl-tools-pod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The scripts allow to manage a series of patches by keeping track of
the changes each patch makes. Patches can be applied, un-applied,
refreshed, etc.

The scripts are heavily based on Andrew Morton's patch scripts found
at <http://www.zip.com.au/~akpm/linux/patches/>.

%description -l pl.UTF-8
Te skrypty pozwalają na zarządzanie zestawem łatek poprzez śledzenie
zmian czynionych przez każdą łatkę. Łaty mogą być nakładane,
wycofywane, odświeżane itp.

Skrypty te są w dużej mierze oparte na skryptach do łat Andrew
Mortona, które można znaleźć pod adresem
<http://www.zip.com.au/~akpm/linux/patches/>.

%package -n bash-completion-quilt
Summary:	bash completion for quilt
Summary(pl.UTF-8):	Dopełnienia basha dla quilt
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion

%description -n bash-completion-quilt
Bash completion for quilt.

%description -n bash-completion-quilt -l pl.UTF-8
Dopełnienia basha dla quilt.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BUILD_ROOT=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO quilt.changes doc/{quilt.pdf,README,README.MAIL}
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/quilt.quiltrc
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/scripts
%attr(755,root,root) %{_datadir}/%{name}/add
%attr(755,root,root) %{_datadir}/%{name}/push
%attr(755,root,root) %{_datadir}/quilt/annotate
%attr(755,root,root) %{_datadir}/quilt/applied
%attr(755,root,root) %{_datadir}/quilt/delete
%attr(755,root,root) %{_datadir}/quilt/diff
%attr(755,root,root) %{_datadir}/quilt/edit
%attr(755,root,root) %{_datadir}/quilt/files
%attr(755,root,root) %{_datadir}/quilt/fold
%attr(755,root,root) %{_datadir}/quilt/fork
%attr(755,root,root) %{_datadir}/quilt/graph
%attr(755,root,root) %{_datadir}/quilt/grep
%attr(755,root,root) %{_datadir}/quilt/header
%attr(755,root,root) %{_datadir}/quilt/import
%attr(755,root,root) %{_datadir}/quilt/mail
%attr(755,root,root) %{_datadir}/quilt/new
%attr(755,root,root) %{_datadir}/quilt/next
%attr(755,root,root) %{_datadir}/quilt/patches
%attr(755,root,root) %{_datadir}/quilt/pop
%attr(755,root,root) %{_datadir}/quilt/previous
%attr(755,root,root) %{_datadir}/quilt/refresh
%attr(755,root,root) %{_datadir}/quilt/rename
%attr(755,root,root) %{_datadir}/quilt/revert
%attr(755,root,root) %{_datadir}/quilt/series
%attr(755,root,root) %{_datadir}/quilt/setup
%attr(755,root,root) %{_datadir}/quilt/snapshot
%attr(755,root,root) %{_datadir}/quilt/top
%attr(755,root,root) %{_datadir}/quilt/unapplied
%attr(755,root,root) %{_datadir}/quilt/upgrade
%{_mandir}/man1/*

%files -n bash-completion-quilt
%defattr(644,root,root,755)
/etc/bash_completion.d/%{name}
