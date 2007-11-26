%define name makebootfat
%define version 1.4
%define release %mkrel 2

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

