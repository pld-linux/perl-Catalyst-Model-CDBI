#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Model-CDBI
Summary:	Catalyst::Model::CDBI - Class::DBI model class for Catalyst
Summary(pl.UTF-8):	Catalyst::Model::CDBI - klasa modelu Class::DBI dla Catalysta
Name:		perl-Catalyst-Model-CDBI
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c9b3d6c90541a0440257823a2f715a99
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 4.00
BuildRequires:	perl-Class-DBI-Loader >= 0.20
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the "Class::DBI" model class for Catalyst. It's built on top
of "Class::DBI::Loader"

%description -l pl.UTF-8
To jest klasa modelu Class::DBI dla Catalysta. Jest zbudowana w
oparciu o Class::DBI::Loader.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Model/*
%{perl_vendorlib}/Catalyst/Helper/Model/*
%{_mandir}/man3/*
