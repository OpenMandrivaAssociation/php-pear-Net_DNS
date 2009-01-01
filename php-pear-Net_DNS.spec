%define		_class		Net
%define		_subclass	DNS
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - resolver library to communicate with a DNS server
Name:		php-pear-%{_pearname}
Version:	1.0.0
%define		_suf b3
Release:	%mkrel 9
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_suf}.tar.bz2
URL:		http://pear.php.net/package/Net_DNS/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A resolver library used to communicate with a name server to perform
DNS queries, zone transfers, dynamic DNS updates, etc. Creates an
object hierarchy from a DNS server's response, which allows you to
view all of the information given by the DNS server. It bypasses the
system's resolver library and communicates directly with the server.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/RR

install %{_pearname}-%{version}%{_suf}/*.php	%{buildroot}%{_datadir}/pear/%{_class}
install %{_pearname}-%{version}%{_suf}/%{_subclass}/*.php	%{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install %{_pearname}-%{version}%{_suf}/%{_subclass}/RR/*.php	%{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/RR

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}
%{_datadir}/pear/packages/%{_pearname}.xml


