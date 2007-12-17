%define	module	Crypt-PasswdMD5
%define	name	perl-%{module}
%define	version	1.3
%define	release	%mkrel 3

Summary:	Perl extension for crypt()-compatible interfaces to the MD5-based crypt()
Name:		%{name}
Version:	%version
Release:	%release
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Crypt/%{module}-%{version}.tar.bz2
URL:		ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Crypt/%{module}-%{version}.readme
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This  code  provides  various  crypt()-compatible  interfaces  to  the
MD5-based crypt() function found in  various *nixes. It's based on the
implementation  found  on FreeBSD  2.2.[56]-RELEASE

%prep
%setup -q -n %{module}-%{version}
perl -pi -e 's,(SSL_DIR.*)/lib\b,\1/%{_lib},g' Makefile.PL

%build
CFLAGS="$RPM_OPT_FLAGS" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Crypt/PasswdMD5.pm
%{_mandir}/*/*

