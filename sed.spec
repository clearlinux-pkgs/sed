#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sed
Version  : 4.2.2
Release  : 13
URL      : http://ftp.gnu.org/gnu/sed/sed-4.2.2.tar.bz2
Source0  : http://ftp.gnu.org/gnu/sed/sed-4.2.2.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0+ GPL-3.0 GFDL-1.3
Requires: sed-bin
Requires: sed-doc
Requires: sed-locales
BuildRequires : acl-dev

%description
This is the GNU implementation of sed, the Unix stream editor.
See the NEWS file for a brief summary and the ChangeLog for
more detailed descriptions of changes.

%package bin
Summary: bin components for the sed package.
Group: Binaries

%description bin
bin components for the sed package.


%package doc
Summary: doc components for the sed package.
Group: Documentation

%description doc
doc components for the sed package.


%package locales
Summary: locales components for the sed package.
Group: Default

%description locales
locales components for the sed package.


%prep
%setup -q -n sed-4.2.2

%build
export CFLAGS="$CFLAGS -Os -ffunction-sections"
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections"
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang sed

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sed

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files locales -f sed.lang 
%defattr(-,root,root,-)

