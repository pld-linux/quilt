Summary:	Scripts for working with series of patches
Summary(pl.UTF-8):	Skrypty do pracy z zestawem łatek
Name:		quilt
Version:	0.48
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://savannah.nongnu.org/download/quilt/%{name}-%{version}.tar.gz
# Source0-md5:	f77adda60039ffa753f3c584a286f12b
URL:		http://savannah.nongnu.org/projects/quilt/
BuildRequires:	gettext-devel
BuildRequires:	perl-tools-pod
Suggests:	diffstat
Suggests:	diffutils
Suggests:	find
Suggests:	patch
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
%doc AUTHORS TODO quilt.changes doc/{quilt.pdf,README{,.EMACS,.MAIL}}
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/quilt.quiltrc
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*
%attr(755,root,root) %{_datadir}/%{name}
%{_mandir}/man1/*

%files -n bash-completion-quilt
%defattr(644,root,root,755)
/etc/bash_completion.d/%{name}
