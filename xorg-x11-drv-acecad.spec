%global tarball xf86-input-acecad
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/input

Summary:   Xorg X11 acecad input driver
Name:      xorg-x11-drv-acecad
Version:   1.5.0
Release:   8%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Patch01:   0001-Stop-crash-on-ABI-12-startup.patch
Patch02:   0001-Always-set-the-type-name.patch
Patch03:   0001-Dont-call-xf86DeleteInput-on-PreInit-failure.patch
Patch04:   0001-Don-t-free-anything-in-PreInit-provide-an-UnInit-ins.patch

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.3.0.0-6
BuildRequires: xorg-x11-util-macros >= 1.3.0

Requires:  Xorg %(xserver-sdk-abi-requires ansic)
Requires:  Xorg %(xserver-sdk-abi-requires xinput)

%description 
X.Org X11 acecad input driver.

%prep
%setup -q -n %{tarball}-%{version}
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch04 -p1

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/acecad_drv.so
%{_mandir}/man4/acecad.4*

%changelog
* Wed Nov 11 2015 Adam Jackson <ajax@redhat.com> 1.5.0-8
- Rebuild for server 1.17

* Wed Apr 23 2014 Adam Jackson <ajax@redhat.com> 1.5.0-7
- Rebuild for server 1.15

* Wed Aug 22 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1.5.0-6
- Rebuild for server 1.13

* Wed Aug 22 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1.5.0-5
- Rebuild for server 1.13

* Wed Aug 01 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1.5.0-4
- Rebuild for server 1.13 (#835212)

* Tue Jul 19 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.5.0-3
- Fix crashes on PreInit failure

* Fri Jul 08 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.5.0-2
- 0001-Always-set-the-type-name.patch: set the type name to something other
  than "UNKNOWN"

* Mon Jun 27 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.5.0-1
- acecad 1.5.0 (#713777)
- 0001-Stop-crash-on-ABI-12-startup.patch

* Wed Jan 06 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.4.0-2
- Use global instead of define per Packaging Guidelines

* Fri Sep 11 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.4.0-1
- acecad 1.4.0
- acecad-1.3.0-abi.patch: Drop.
- Require xorg-x11-util-macros 1.3.0

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.3.0-2
- acecad-1.3.0-abi.patch: cope with XINPUT ABI 7.

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 1.3.0-1.1
- ABI bump

* Tue Feb 24 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.3.0-1
- acecad 1.3.0

* Fri Feb 22 2008 Adam Jackson <ajax@redhat.com> 1.2.2-1
- acecad 1.2.2

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.0-6
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 1.1.0-5
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.1.0-4
- Update BuildRequires and Requires.

* Tue Feb 20 2007 Adam Jackson <ajax@redhat.com> 1.1.0-3
- ExclusiveArch -> ExcludeArch
- Disown directories

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Fri May 26 2006 Mike A. Harris <mharris@redhat.com> 1.1.0-2
- Update sdk dependency to 1.1.0-2 to pick up indirect dependency on
  proto-devel.

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-1
- Bump to 1.1.0 from 7.1RC1.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0.5-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.0.5-1
- Updated xorg-x11-drv-acecad to version 1.0.0.5 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.4-1
- Updated xorg-x11-drv-acecad to version 1.0.0.4 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.2-1
- Updated xorg-x11-drv-acecad to version 1.0.0.2 from X11R7 RC2

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.1-1
- Updated xorg-x11-drv-acecad to version 1.0.0.1 from X11R7 RC1
- Fix *.la file removal.

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-0
- Initial spec file for acecad input driver generated automatically
  by my xorg-driverspecgen script.
