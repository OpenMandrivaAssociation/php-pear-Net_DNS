%define		_class		Net
%define		_subclass	DNS
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.7
Release:	5
Summary:	Resolver library to communicate with a DNS server
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Net_DNS/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
A resolver library used to communicate with a name server to perform
DNS queries, zone transfers, dynamic DNS updates, etc. Creates an
object hierarchy from a DNS server's response, which allows you to
view all of the information given by the DNS server. It bypasses the
system's resolver library and communicates directly with the server.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-3mdv2012.0
+ Revision: 742137
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-2
+ Revision: 679409
- mass rebuild

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.7-1mdv2011.0
+ Revision: 594498
- update to new version 1.0.7

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.5-1mdv2011.0
+ Revision: 569598
- update to new version 1.0.5

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-2mdv2010.1
+ Revision: 468694
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sat Sep 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-1mdv2010.0
+ Revision: 449309
- new version
- use pear installer
- use fedora %%post/%%postun

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.0-10mdv2010.0
+ Revision: 441443
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-9mdv2009.1
+ Revision: 322374
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-8mdv2009.0
+ Revision: 236976
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-7mdv2007.0
+ Revision: 82239
- Import php-pear-Net_DNS

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdk
- initial Mandriva package (PLD import)

