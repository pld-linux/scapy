# TODO:
# - package and add Suggests:
# * Vpython (http://www.vpython.org/)

Summary:	Interactive packet manipulation program
Summary(pl.UTF-8):	Interaktywny program do manipulacji pakietami
Name:		scapy
Version:	2.2.0
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	http://www.secdev.org/projects/scapy/files/%{name}-%{version}.tar.gz
# Source0-md5:	406990bd8da1f4958b354b4b6fc4b3eb
URL:		http://www.secdev.org/projects/scapy/
BuildRequires:	rpm-pythonprov
BuildRequires:	sphinx-pdg
Requires:	python-libdnet
Requires:	python-pylibpcap
Suggests:	python-Crypto
Suggests:	python-Gnuplot
Suggests:	python-pygraphviz
Suggests:	python-pyx
Suggests:	sox
Suggests:	texlive
Suggests:	texlive-fonts-type1-bluesky
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scapy is a powerful interactive packet manipulation program. It is
able to forge or decode packets of a wide number of protocols, send
them on the wire, capture them, match requests and replies, and much
more. It can easily handle most classical tasks like scanning,
tracerouting, probing, unit tests, attacks or network discovery (it
can replace hping, 85% of nmap, arpspoof, arp-sk, arping, tcpdump,
tethereal, p0f, etc.). It also performs very well at a lot of other
specific tasks that most other tools can't handle, like sending
invalid frames, injecting your own 802.11 frames, combining technics
(VLAN hopping+ARP cache poisoning, VoIP decoding on WEP encrypted
channel, ...), etc.

%description -l pl.UTF-8
Scapy jest interaktywnym programem służacym do manipulacji pakietami o
olbrzymich możliwościach. Potrafi tworzyć i dekodować pakiety sporej
ilości protokołów, przesyłać je, przechwytywac je, dopasowywać żądania
i odpowiedzi i wiele więcej. Z łatwością obsługuje typowe zadania
takie jak skanowanie, śledzenie trasy, sondowanie, testy jednostkowe,
ataki czy też wykrywanie (usług w) sieci (może zastapić hping, 85%
nmapa, arpspoof, arp-sk, arping, tcpdump, tethereal, p0f itp.). Radzi
sobie rownież z innymi specyficznymi zadaniami, którym inne narzedzia
nie są w stanie podołać - wysyłanie nieprawidlowych ramek,
wstrzykiwanie własnych ramek 802.11, łączenie technik (przeskakiwanie
VLANów+zatruwanie ARP cache, dekodowanie VoIP na kanale zabezpieczonym
WEP, ...) itp.

%prep
%setup -q

%build
%{__python} setup.py build
cd doc/scapy
%{__make} html

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/scapy/_build/html/*
#%doc doc/scapy/_build/html/_static/*
#%doc doc/scapy/_build/html/_images/*
#%doc doc/scapy/_build/html/_sources/*.txt
%attr(755,root,root) %{_bindir}/*%{name}
%{py_sitescriptdir}/*.egg-info
%dir %{py_sitescriptdir}/%{name}
%dir %{py_sitescriptdir}/%{name}/arch
%dir %{py_sitescriptdir}/%{name}/arch/windows
%dir %{py_sitescriptdir}/%{name}/asn1
%dir %{py_sitescriptdir}/%{name}/crypto
%dir %{py_sitescriptdir}/%{name}/layers
%dir %{py_sitescriptdir}/%{name}/modules
%dir %{py_sitescriptdir}/%{name}/tools
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/%{name}/arch/*.py[co]
%{py_sitescriptdir}/%{name}/arch/windows/*.py[co]
%{py_sitescriptdir}/%{name}/asn1/*.py[co]
%{py_sitescriptdir}/%{name}/crypto/*.py[co]
%{py_sitescriptdir}/%{name}/layers/*.py[co]
%{py_sitescriptdir}/%{name}/modules/*.py[co]
%{py_sitescriptdir}/%{name}/tools/*.py[co]
%{_mandir}/man1/%{name}.1*
