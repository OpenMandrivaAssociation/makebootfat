%define name makebootfat
%define version 1.4
%define release %mkrel 6

Summary: A command line utility able to create bootable USB disks
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://puzzle.dl.sourceforge.net/sourceforge/advancemame/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware 
Url: http://advancemame.sourceforge.net/boot-download.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
makebootfat is a command line utility able to create 
bootable USB disks for Linux and Windows 
using the FAT filesystem and syslinux.

%prep
%setup -q
%configure

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/makebootfat
%{_mandir}/man1/makebootfat*



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-6mdv2011.0
+ Revision: 620291
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.4-5mdv2010.0
+ Revision: 429931
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 1.4-4mdv2009.0
+ Revision: 251784
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.4-2mdv2008.1
+ Revision: 140944
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import makebootfat


* Thu Jun 22 2006 Erwan Velu <erwan@seanodes.com> 1.4-2
- Fixing url

* Fri Jun 24 2005 Erwan Velu <erwan@seanodes.com> 1.4-1mdk
- 1.4
* Fri Feb 24 2005 Erwan Velu <erwan@seanodes.com> 1.2-1mdk
- Initial release
