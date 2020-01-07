#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-autovivification
Version  : 0.18
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/V/VP/VPIT/autovivification-0.18.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/V/VP/VPIT/autovivification-0.18.tar.gz
Summary  : 'Lexically disable autovivification.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-autovivification-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
autovivification - Lexically disable autovivification.
VERSION
Version 0.18

%package dev
Summary: dev components for the perl-autovivification package.
Group: Development
Provides: perl-autovivification-devel = %{version}-%{release}
Requires: perl-autovivification = %{version}-%{release}

%description dev
dev components for the perl-autovivification package.


%package perl
Summary: perl components for the perl-autovivification package.
Group: Default
Requires: perl-autovivification = %{version}-%{release}

%description perl
perl components for the perl-autovivification package.


%prep
%setup -q -n autovivification-0.18
cd %{_builddir}/autovivification-0.18

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
/usr/share/man/man3/autovivification.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/auto/autovivification/autovivification.so
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/autovivification.pm
