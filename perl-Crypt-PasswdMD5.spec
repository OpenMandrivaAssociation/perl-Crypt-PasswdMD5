%define	modname	 Crypt-PasswdMD5
%define modver 1.40

Summary:	Perl extension for crypt()-compatible interfaces to the MD5-based crypt()
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.cpan.org:21/pub/CPAN/modules/by-module/Crypt/Crypt-PasswdMD5-%{modver}.tgz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This  code  provides  various  crypt()-compatible  interfaces  to  the
MD5-based crypt() function found in  various *nixes. It's based on the
implementation  found  on FreeBSD  2.2.[56]-RELEASE

%prep
%setup -q -n %{modname}-%{modver}
perl -pi -e 's,(SSL_DIR.*)/lib\b,\1/%{_lib},g' Makefile.PL

%build
CFLAGS="%{optflags}" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Crypt/PasswdMD5.pm
%{_mandir}/man3/*


