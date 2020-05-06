%define		package	BrowserKit
%define		php_min_version 5.3.9
Summary:	Symfony2 BrowserKit Component
Name:		php-symfony2-BrowserKit
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	cfea82b837888e88471d95a950b648ed
URL:		http://symfony.com/components/BrowserKit
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
Requires:	php-symfony2-DomCrawler >= 2.0.5
Suggests:	php-symfony2-Process
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BrowserKit simulates the behavior of a web browser.

The component only provide an abstract client and does not provide any
"default" backend for the HTTP layer.

%prep
%setup -q -n browser-kit-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/BrowserKit
%{php_data_dir}/Symfony/Component/BrowserKit/*.php
