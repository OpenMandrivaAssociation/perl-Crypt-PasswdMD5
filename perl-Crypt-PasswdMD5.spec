%define	upstream_name	 Crypt-PasswdMD5
%define	upstream_version 1.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Perl extension for crypt()-compatible interfaces to the MD5-based crypt()
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This  code  provides  various  crypt()-compatible  interfaces  to  the
MD5-based crypt() function found in  various *nixes. It's based on the
implementation  found  on FreeBSD  2.2.[56]-RELEASE

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
perl -pi -e 's,(SSL_DIR.*)/lib\b,\1/%{_lib},g' Makefile.PL

%build
CFLAGS="$RPM_OPT_FLAGS" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Crypt/PasswdMD5.pm
%{_mandir}/*/*
