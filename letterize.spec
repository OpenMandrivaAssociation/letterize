Name: letterize
Version: 1.2
Release: %mkrel 8
Summary: Generate pronounceable mnemonics from phone numbers
URL: http://www.catb.org/~esr/letterize/
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Text tools
BuildRoot: %{_tmppath}/%{name}-root

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
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"/usr/bin
mkdir -p "$RPM_BUILD_ROOT"/usr/share/man/man1/
cp letterize "$RPM_BUILD_ROOT"/usr/bin
cp letterize.1 "$RPM_BUILD_ROOT"/usr/share/man/man1/

%clean
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README COPYING
%{_mandir}/man1/letterize.1*
%{_bindir}/letterize

