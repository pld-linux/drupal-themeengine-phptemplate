%define		engine phptemplate
Summary:	Drupal PHPTemplate theme engine
Summary(pl):	Silnik motywów Drupala PHPTemplate
Name:		drupal-themeengine-%{engine}
Version:	4.6.0
Release:	0.2
Epoch:		0
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{engine}-%{version}.tar.gz
# Source0-md5:	54604c9ce9e3a760126152badb0f401d
URL:		http://drupal.org/project/phptemplate
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enginedir			%{_datadir}/drupal/themes/engines

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

%description -l pl
Ten silnik motywów umo¿liwia u¿ywanie plików szablonów napisanych w
czystym PHP. Te pliki szablonów nie wymagaj± przetwarzania przez
silnik motywów i jako takie wykonuj± siê du¿o szybciej ni¿ wiêkszo¶æ
innych silników motywów. Inn± du¿± zalet± u¿ywania PHP jako jêzyka
szablonów jest elastyczno¶æ, jako ¿e zaawansowany u¿ytkownik mo¿e
dostaæ siê do ka¿dej informacji/funkcjonalno¶ci dostêpnej w API
Drupala i nie jest ograniczony do tego, na co pozwala mu silnik/jêzyk
szablonów.

Kilka najwiêkszych serwisów opartych na Drupalu, takich jak Drupal.org
czy Spreadfirefox.com u¿ywa motywów opartych na PHPTemplate.

"Domy¶lnym" szablonem dla tego silnika jest box_grey Adriana Simmonsa.

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
