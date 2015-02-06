Name:		letterize
Version:	1.3
Release:	2
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



%changelog
* Sun Oct 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3-1mdv2011.0
+ Revision: 588083
- correct use of buildroot
- new version 1.3
- spec cleanup
- fix license
- fix source0

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.2-8mdv2010.0
+ Revision: 429711
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.2-7mdv2009.0
+ Revision: 248365
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.2-5mdv2008.1
+ Revision: 136535
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 17:58:13 (54972)
- rebuild

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 17:56:56 (54971)
Import letterize

* Mon May 01 2006 Olivier Thauvin <nanardon@mandriva.org> 1.2-4mdk
- Birthday Rebuild

* Sun Jan 30 2005 Sylvie Terjan <erinmargault@mandrake.org> 1.2-3mdk
- forgotten last changelog on birthday rebuild

* Sun Jan 30 2005 Sylvie Terjan <erinmargault@mandrake.org> 1.2-2mdk
* Tue Dec 30 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.2-1mdk
- introduce in contrib

* Mon Dec 29 2003 Eric S. Raymond <esr@snark.thyrsus.com> 1.2-1
- RPM packaging fixes for freshmeat release.

