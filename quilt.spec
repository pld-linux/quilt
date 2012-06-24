Summary:	Scripts for working with series of patches
Summary(pl):	Skrypty do pracy z zestawem �atek
Name:		quilt
Version:	0.43
Release:	0.1
Epoch:		0
License:	GPL v2+
Group:		Applications/Text
Source0:	http://savannah.nongnu.org/download/quilt/%{name}-%{version}.tar.gz
# Source0-md5:	a0bed88a3dbc0d2f25659bf9077c2515
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

%description -l pl
Te skrypty pozwalaj� na zarz�dzanie zestawem �atek poprzez �ledzenie
zmian czynionych przez ka�d� �atk�. �aty mog� by� nak�adane,
wycofywane, od�wie�ane itp.

Skrypty te s� w du�ej mierze oparte na skryptach do �at Andrew
Mortona, kt�re mo�na znale�� pod adresem
<http://www.zip.com.au/~akpm/linux/patches/>.

%package -n bash-completion-quilt
Summary:	bash completion for quilt
Summary(pl):	Dope�nienia basha dla quilt
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion

%description -n bash-completion-quilt
Bash completion for quilt.

%description -n bash-completion-quilt -l pl
Dope�nienia basha dla quilt.

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
%{_datadir}/%{name}
%{_mandir}/man1/*

%files -n bash-completion-quilt
%defattr(644,root,root,755)
/etc/bash_completion.d/%{name}
