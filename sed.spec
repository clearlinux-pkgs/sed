#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7FD9FCCB000BEEEE (meyering@fb.com)
#
Name     : sed
Version  : 4.4
Release  : 20
URL      : http://ftp.gnu.org/gnu/sed/sed-4.4.tar.xz
Source0  : http://ftp.gnu.org/gnu/sed/sed-4.4.tar.xz
Source99 : http://ftp.gnu.org/gnu/sed/sed-4.4.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0 GPL-3.0+
Requires: sed-bin
Requires: sed-doc
Requires: sed-locales
BuildRequires : acl-dev
BuildRequires : libc6-locale
BuildRequires : valgrind

%description
This is the GNU implementation of sed, the Unix stream editor.
GNU Sed website: https://www.gnu.org/software/sed/

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
%setup -q -n sed-4.4

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487184393
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export FCFLAGS="$CFLAGS -Os -ffunction-sections "
export FFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1487184393
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

