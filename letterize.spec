Name:		letterize
Version:	1.3
Release:	%mkrel 1
Summary:	Generate pronounceable mnemonics from phone numbers
URL:		http://www.catb.org/~esr/letterize/
Source0:	%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Text tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Generate all possible alphabetic mnemonics for a phone
number, then filter them for phonetic plausibility in
English.

%prep
%setup -q

%build

cc $RPM_OPT_FLAGS letterize.c -o letterize

## make letterize.1

%install
rm -rf %buildroot 
mkdir -p %buildroot/usr/bin
mkdir -p %buildroot/usr/share/man/man1/
cp %{name}  %buildroot/usr/bin
cp %{name}.1 %buildroot/usr/share/man/man1/

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README COPYING
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

