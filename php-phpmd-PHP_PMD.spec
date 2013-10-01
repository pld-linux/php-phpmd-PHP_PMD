%define		status		stable
%define		pearname	PHP_PMD
%include	/usr/lib/rpm/macros.php
Summary:	PHP Mess Detector
Name:		php-phpmd-PHP_PMD
Version:	1.5.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpmd.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	9b3ffd8cca7882d62d37bea4c773b9a2
URL:		http://pear.phpmd.org/package/PHP_PMD/
BuildRequires:	php-channel(pear.phpmd.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(dom)
Requires:	php(pcre)
Requires:	php(simplexml)
Requires:	php(spl)
Requires:	php-channel(pear.phpmd.org)
Requires:	php-pdepend-PHP_Depend >= 1.1.1
Requires:	php-pear
Obsoletes:	php-phpmd-PHP-PMD
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PHP Mess Detector aims to be a simplified PHP port of the well
known Java Tool PMD. This project uses PHP_Depend to measure several
software metrics from given source code, then it compares the
calculated values with customizeable thresholds and reports all
suspect software artifacts

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
%pear_package_install
install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/PHP_PMD/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/phpmd
%{php_pear_dir}/PHP/PMD.php
%{php_pear_dir}/PHP/PMD
%{php_pear_dir}/data/PHP_PMD
