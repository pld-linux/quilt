Summary:	Scripts for working with series of patches
Summary(pl):	Skrypty do pracy z zestawem ³atek
Name:		quilt
Version:	0.42
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications/Text
Source0:	http://savannah.nongnu.org/download/quilt/%{name}-%{version}.tar.gz
# Source0-md5:	c07d43f24f4a473cab4519732647086b
URL:		http://savannah.nongnu.org/projects/quilt
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The scripts allow to manage a series of patches by keeping
track of the changes each patch makes. Patches can be
applied, un-applied, refreshed, etc.

The scripts are heavily based on Andrew Morton's patch scripts
found at http://www.zip.com.au/~akpm/linux/patches/.

%package -n bash-completion-quilt
Summary:        bash completion for quilt
Summary(pl):    Dope³nienia basha dla quilt
Group:          Applications/Shells
Requires:       bash-completion
Requires:       %{name} = %{version}-%{release}

%description -n bash-completion-quilt
Bash completion for quilt.

%description -n bash-completion-quilt -l pl
Dope³nienia basha dla quilt.

%prep
%setup -q

%build
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=/usr \
	BUILD_ROOT=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO quilt.changes doc/{quilt.pdf,README.MAIL,sample.quiltrc}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/quilt.quiltrc
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*

%files -n bash-completion-quilt
%defattr(644,root,root,755)
/etc/bash_completion.d/%{name}
