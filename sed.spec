#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7FD9FCCB000BEEEE (meyering@fb.com)
#
Name     : sed
Version  : 4.8
Release  : 30
URL      : https://mirrors.kernel.org/gnu/sed/sed-4.8.tar.xz
Source0  : https://mirrors.kernel.org/gnu/sed/sed-4.8.tar.xz
Source1  : https://mirrors.kernel.org/gnu/sed/sed-4.8.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: sed-bin = %{version}-%{release}
Requires: sed-info = %{version}-%{release}
Requires: sed-license = %{version}-%{release}
Requires: sed-locales = %{version}-%{release}
Requires: sed-man = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : glibc-locale
BuildRequires : libc6-locale
BuildRequires : valgrind

%description
This is the GNU implementation of sed, the Unix stream editor.
GNU Sed website: https://www.gnu.org/software/sed/

%package bin
Summary: bin components for the sed package.
Group: Binaries
Requires: sed-license = %{version}-%{release}

%description bin
bin components for the sed package.


%package info
Summary: info components for the sed package.
Group: Default

%description info
info components for the sed package.


%package license
Summary: license components for the sed package.
Group: Default

%description license
license components for the sed package.


%package locales
Summary: locales components for the sed package.
Group: Default

%description locales
locales components for the sed package.


%package man
Summary: man components for the sed package.
Group: Default

%description man
man components for the sed package.


%prep
%setup -q -n sed-4.8
cd %{_builddir}/sed-4.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619063143
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1619063143
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sed
cp %{_builddir}/sed-4.8/COPYING %{buildroot}/usr/share/package-licenses/sed/0dd432edfab90223f22e49c02e2124f87d6f0a56
%make_install
%find_lang sed

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sed

%files info
%defattr(0644,root,root,0755)
/usr/share/info/sed.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sed/0dd432edfab90223f22e49c02e2124f87d6f0a56

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/sed.1

%files locales -f sed.lang
%defattr(-,root,root,-)

