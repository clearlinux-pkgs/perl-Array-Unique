#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Array-Unique
Version  : 0.08
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/S/SZ/SZABGAB/Array-Unique-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SZ/SZABGAB/Array-Unique-0.08.tar.gz
Summary  : Tie-able array that allows only unique values
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Array-Unique-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Array::Unique - Tie-able array that allows only unique values
SYNOPSIS
use Array::Unique;
tie @a, 'Array::Unique';

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
%setup -q -n Array-Unique-0.08
cd %{_builddir}/Array-Unique-0.08

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Array::Unique.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Array/Unique.pm
