#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Array-Unique
Version  : 0.09
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/S/SZ/SZABGAB/Array-Unique-0.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SZ/SZABGAB/Array-Unique-0.09.tar.gz
Summary  : 'Tie-able array that allows only unique values'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Array-Unique-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Array::Unique - Tie-able array that allows only unique values
SYNOPSIS
use Array::Unique;
tie @a, 'Array::Unique';

Now use @a as a regular array.

%package dev
Summary: dev components for the perl-Array-Unique package.
Group: Development
Provides: perl-Array-Unique-devel = %{version}-%{release}
Requires: perl-Array-Unique = %{version}-%{release}

%description dev
dev components for the perl-Array-Unique package.


%package perl
Summary: perl components for the perl-Array-Unique package.
Group: Default
Requires: perl-Array-Unique = %{version}-%{release}

%description perl
perl components for the perl-Array-Unique package.


%prep
%setup -q -n Array-Unique-0.09
cd %{_builddir}/Array-Unique-0.09
pushd ..
cp -a Array-Unique-0.09 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Array::Unique.3
/usr/share/man/man3/Array::Unique::Hash.3
/usr/share/man/man3/Array::Unique::IxHash.3
/usr/share/man/man3/Array::Unique::Quick.3
/usr/share/man/man3/Array::Unique::Std.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
