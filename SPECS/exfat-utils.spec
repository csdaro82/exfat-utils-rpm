Name:		exfat-utils
Summary:	Utilities for exFAT file system
Version: 	1.2.4
Release:	1%{?dist}
Group:		System Environment/Base
License:	GPLv3+
URL:		https://github.com/relan/exfat
Source0:	https://github.com/relan/exfat/releases/download/v%{version}/exfat-utils-%{version}.tar.gz
#Source0:        https://dl.deskosproject.org/sources/exfat-utils/

%description
A set of utilities for creating, checking, dumping and labeling exFAT file system.

%prep
%setup -q


%build
%configure
%make_build


%install
%make_install INSTALL="install -p"


%files
%{_sbindir}/dumpexfat
%{_sbindir}/exfatfsck
%attr(755,root,root) %{_sbindir}/fsck.exfat
%{_sbindir}/mkexfatfs
%attr(755,root,root) %{_sbindir}/mkfs.exfat
%{_sbindir}/exfatlabel
%attr(644,root,root) %{_mandir}/man8/dumpexfat.8.gz
%attr(644,root,root) %{_mandir}/man8/exfatfsck.8.gz
%attr(644,root,root) %{_mandir}/man8/mkexfatfs.8.gz
%attr(644,root,root) %{_mandir}/man8/exfatlabel.8.gz

%changelog
* Mon Sep 26 2016 Darío Córdova <dcordova@deskosproject.org> - 1.2.4-1
- Initial package for DeskOS
