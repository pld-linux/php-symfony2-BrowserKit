%define		package	BrowserKit
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 BrowserKit Component
Name:		php-symfony2-BrowserKit
Version:	2.7.3
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	ebd07028a29e6686711ba5a8eb5aa249
URL:		http://symfony.com/components/BrowserKit
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-pear >= 4:1.3.10
Requires:	php-symfony2-DomCrawler >= 2.0.5
Suggests:	php-symfony2-Process
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BrowserKit simulates the behavior of a web browser.

The component only provide an abstract client and does not provide any
"default" backend for the HTTP layer.

%prep
%setup -q -n %{package}-%{version}

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
cp -a *.php $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/BrowserKit
%{php_pear_dir}/Symfony/Component/BrowserKit/*.php
