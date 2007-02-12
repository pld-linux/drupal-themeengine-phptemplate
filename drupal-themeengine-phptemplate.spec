%define		engine phptemplate
Summary:	Drupal PHPTemplate theme engine
Summary(pl.UTF-8):   Silnik motywów Drupala PHPTemplate
Name:		drupal-themeengine-%{engine}
Version:	4.6.0
Release:	0.3
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{engine}-%{version}.tar.gz
# Source0-md5:	54604c9ce9e3a760126152badb0f401d
URL:		http://drupal.org/project/phptemplate
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_enginedir	%{_drupaldir}/themes/engines

%description
A theme engine that allows you to use template files written in pure
PHP. These template files do not need to be processed by the theme
engine, and as such execute a lot faster than most other template
engines. Another major advantage to using PHP as your template
language, is flexibility, as the advanced user can access any
information / functionality available in the Drupal API, and is not
restricted to what the template engine / language allows him to do.

Several of the largest Drupal sites, such as Drupal.org and
Spreadfirefox.com use PHPTemplate based themes.

The 'default' template for this engine is box_grey by Adrian Simmons.

%description -l pl.UTF-8
Ten silnik motywów umożliwia używanie plików szablonów napisanych w
czystym PHP. Te pliki szablonów nie wymagają przetwarzania przez
silnik motywów i jako takie wykonują się dużo szybciej niż większość
innych silników motywów. Inną dużą zaletą używania PHP jako języka
szablonów jest elastyczność, jako że zaawansowany użytkownik może
dostać się do każdej informacji/funkcjonalności dostępnej w API
Drupala i nie jest ograniczony do tego, na co pozwala mu silnik/język
szablonów.

Kilka największych serwisów opartych na Drupalu, takich jak Drupal.org
czy Spreadfirefox.com używa motywów opartych na PHPTemplate.

"Domyślnym" szablonem dla tego silnika jest box_grey Adriana Simmonsa.

%prep
%setup -q -n %{engine}
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_enginedir}/%{engine}

install *.engine *.php $RPM_BUILD_ROOT%{_enginedir}/%{engine}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_enginedir}/%{engine}
