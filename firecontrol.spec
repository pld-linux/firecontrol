Summary:	Debug 1394 devices
Summary(pl.UTF-8):	Diagnostyka urządzeń 1394
Name:		firecontrol
Version:	0.2
Release:	4
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/firecontrol/%{name}-%{version}.tar.gz
# Source0-md5:	e0f272ee4a72f214af3b06bfb81527ef
URL:		http://firecontrol.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libraw1394-devel >= 0.10.0
BuildRequires:	readline-devel
Provides:	1394commander
Obsoletes:	1394commander
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
firecontrol is a simple console oriented tool based on libraw1394 to
issue asynchronous read, write and lock commands to some nodes on the
bus as well as to force bus resets. The main advantage of this tool
over other available tools (like gscanbus) is (besides not requiring a
graphical interface), that it reports the exact acknowledge and
response codes and therefore is very useful for debugging purposes.

%description -l pl.UTF-8
firecontrol to proste narzędzie konsolowe oparte na libraw1394 do
wydawania poleceń asynchronicznego odczytu, zapisu i blokowania
pewnych węzłów na szynie, a także wymuszania resetu szyny. Główną
zaletą tego narzędzia nad innymi (jak gscanbus) jest (oprócz nie
wymagania graficznego interfejsu) to, że podaje szczegółowe informacje
i kody odpowiedzi, dzięki czemu jest bardzo przydatne do celów
diagnostycznych.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/firecontrol
