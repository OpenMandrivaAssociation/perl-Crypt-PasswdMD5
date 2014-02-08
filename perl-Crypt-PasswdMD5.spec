%define	upstream_name	 Crypt-PasswdMD5
%define	upstream_version 1.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Perl extension for crypt()-compatible interfaces to the MD5-based crypt()
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This  code  provides  various  crypt()-compatible  interfaces  to  the
MD5-based crypt() function found in  various *nixes. It's based on the
implementation  found  on FreeBSD  2.2.[56]-RELEASE

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.300.0-4mdv2012.0
+ Revision: 765131
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.300.0-3
+ Revision: 763635
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.300.0-2
+ Revision: 667061
- mass rebuild

* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.300.0-1mdv2010.1
+ Revision: 505723
- rebuild using %%perl_convert_version

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.3-7mdv2010.0
+ Revision: 426442
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.3-6mdv2009.1
+ Revision: 351698
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.3-5mdv2009.0
+ Revision: 241195
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Sun Jul 09 2006 Stefan van der Eijk <stefan@mandriva.org> 1.3-3mdk
- rebuild

* Sat Jun 04 2005 Stefan van der Eijk <stefan@eijk.nu> 1.3-2mdk
- B'day rebuild
- %%mkrel

* Sun May 16 2004 Stefan van der Eijk <stefan@eijk.nu> 1.3-1mdk
- initial package

