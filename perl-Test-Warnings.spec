%{?scl:%scl_package perl-Test-Warnings}

# Run optional test
%if ! (0%{?rhel}) && ! (0%{?scl:1})
%bcond_without perl_Test_Warnings_enables_optional_test
%else
%bcond_with perl_Test_Warnings_enables_optional_test
%endif

Name:		%{?scl_prefix}perl-Test-Warnings
Version:	0.028
Release:	2%{?dist}
Summary:	Test for warnings and the lack of them
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Test-Warnings
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Warnings-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	%{?scl_prefix}perl-generators
BuildRequires:	%{?scl_prefix}perl-interpreter
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
# Module
BuildRequires:	%{?scl_prefix}perl(Carp)
BuildRequires:	%{?scl_prefix}perl(Exporter)
BuildRequires:	%{?scl_prefix}perl(Test::Builder)
BuildRequires:	%{?scl_prefix}perl(parent)
BuildRequires:	%{?scl_prefix}perl(strict)
BuildRequires:	%{?scl_prefix}perl(warnings)
# Test Suite
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:	%{?scl_prefix}perl(File::Spec)
BuildRequires:	%{?scl_prefix}perl(if)
BuildRequires:	%{?scl_prefix}perl(lib)
BuildRequires:	%{?scl_prefix}perl(Test::More) >= 0.94
BuildRequires:	%{?scl_prefix}perl(Test::Tester) >= 0.108
%if %{with perl_Test_Warnings_enables_optional_test}
# Optional Tests
BuildRequires:	%{?scl_prefix}perl(CPAN::Meta) >= 2.120900
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:	%{?scl_prefix}perl(CPAN::Meta::Check) >= 0.011
%endif
BuildRequires:	%{?scl_prefix}perl(CPAN::Meta::Prereqs)
BuildRequires:	%{?scl_prefix}perl(CPAN::Meta::Requirements)
BuildRequires:	%{?scl_prefix}perl(PadWalker)
%endif
# Runtime
Requires:	%{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:	%{?scl_prefix}perl(Carp)

%description
If you've ever tried to use Test::NoWarnings to confirm there are no warnings
generated by your tests, combined with the convenience of done_testing to not
have to declare a test count, you'll have discovered that these two features do
not play well together, as the test count will be calculated before the
warnings test is run, resulting in a TAP error (see examples/test_nowarnings.pl
in this distribution for a demonstration).

This module is intended to be used as a drop-in replacement for
Test::NoWarnings: it also adds an extra test, but runs this test before
done_testing calculates the test count, rather than after. It does this by
hooking into done_testing as well as via an END block. You can declare a plan,
or not, and things will still Just Work.

It is actually equivalent to:

    use Test::NoWarnings 1.04 ':early';

as warnings are still printed normally as they occur. You are safe, and
enthusiastically encouraged, to perform a global search-replace of the above
with use Test::Warnings; whether or not your tests have a plan.

%prep
%setup -q -n Test-Warnings-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENCE
%doc Changes CONTRIBUTING README examples/
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Warnings.3*

%changelog
* Fri Jan 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.028-2
- SCL

* Sun Dec 22 2019 Paul Howarth <paul@city-fan.org> - 0.028-1
- Update to 0.028
  - Allow for warnings->import being called after importing the "warnings" sub

* Sat Sep 28 2019 Paul Howarth <paul@city-fan.org> - 0.027-1
- Update to 0.027
  - New :fail_on_warning feature, for more easily seeing where the surprising
    warning appeared during testing
- Use author-independent source URL
- Simplify find command using -delete

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.026-11
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.026-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.026-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.026-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.026-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Paul Howarth <paul@city-fan.org> - 0.026-1
- Update to 0.026
  - Fixed use of modules loaded by t/zzz-check-breaks.t
  - Fix stderr suppression on perl 5.6

* Mon Jan 25 2016 Paul Howarth <paul@city-fan.org> - 0.025-1
- Update to 0.025
  - Prereqs lowered from required to suggested:
    - CPAN::Meta::Check
    - CPAN::Meta::Requirements
  - Tests are now quieter to avoid causing confusion, by suppressing the
    printing of stderr in tests

* Sun Dec 27 2015 Paul Howarth <paul@city-fan.org> - 0.024-1
- Update to 0.024
  - Remove diagnostics accidentally left in new test

* Tue Dec 22 2015 Paul Howarth <paul@city-fan.org> - 0.023-1
- Update to 0.023
  - Properly handle propagating warnings to previously declared handlers that
    are not coderefs (i.e. a sub name, or the magic DEFAULT and IGNORE)

* Mon Dec 21 2015 Paul Howarth <paul@city-fan.org> - 0.022-1
- Update to 0.022
  - Propagate all warnings to any previously-declared __WARN__ handlers
    (unlike with __DIE__, merely calling warn() is not sufficient)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.021-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.021-2
- Perl 5.22 rebuild

* Mon Mar 23 2015 Paul Howarth <paul@city-fan.org> - 0.021-1
- Update to 0.021
  - Add a x_breaks entry for conflicting versions of File::pushd that
    inadvertently call our exported warnings() rather than invoking
    warnings.pm, and documented this undesired interaction

* Wed Jan  7 2015 Paul Howarth <paul@city-fan.org> - 0.020-1
- Update to 0.020
  - Re-release to fix problematic $VERSION declaration (CPAN RT#101239)

* Fri Dec 19 2014 Paul Howarth <paul@city-fan.org> - 0.019-1
- Update to 0.019
  - Fix test to allow for special characters (e.g. MSWin32 file separators) in
    filenames (PR#7)

* Thu Dec 18 2014 Paul Howarth <paul@city-fan.org> - 0.018-1
- Update to 0.018
  - Fix test to not depend on message formatting changes in newer Carp

* Wed Dec 17 2014 Paul Howarth <paul@city-fan.org> - 0.017-1
- Update to 0.017
  - Handle other warning handlers passing us partial warning messages by
    re-adding the source file and line number
- Use %%license

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.016-2
- Perl 5.20 rebuild

* Sun Jun 22 2014 Paul Howarth <paul@city-fan.org> - 0.016-1
- Update to 0.16
  - Fix prereq problem with last release - now no longer testing the example
    scripts for user installs

* Fri Jun 20 2014 Paul Howarth <paul@city-fan.org> - 0.015-1
- Update to 0.15
  - Adjusted packaging and tests to become perl-5.6 friendly, including only
    using core or dual-lifed prerequisites
- Switch to ExtUtils::MakeMaker flow

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar  3 2014 Paul Howarth <paul@city-fan.org> - 0.014-1
- Update to 0.014
  - Fix test that fails when FOO or BAR environment variables are set
    (CPAN RT#93447)

* Mon Dec 16 2013 Paul Howarth <paul@city-fan.org> - 0.013-1
- Update to 0.013
  - Update configure_requires checking in Makefile.PL

* Mon Oct 14 2013 Paul Howarth <paul@city-fan.org> - 0.012-1
- Update to 0.012
  - Re-release to fix t/00-report-prereqs.t use of CPAN::Meta::Requirements

* Sun Oct 13 2013 Paul Howarth <paul@city-fan.org> - 0.011-1
- Update to 0.011
  - Unnecessary tests removed
  - CONTRIBUTING file added
- Drop buildreqs only needed for removed tests
- BR: optional test requirement perl(CPAN::Meta::Requirements)

* Wed Sep 25 2013 Paul Howarth <paul@city-fan.org> - 0.010-1
- Update to 0.010
  - Re-release with fixed compile test
- Update dependencies
- Package examples

* Wed Sep 11 2013 Paul Howarth <paul@city-fan.org> - 0.009-1
- Update to 0.009
  - Fixed error in synopsis (we do not export anything by default)
  - A caveat added to the documentation regarding embedding warning checks
    inside another sub
  - ':no_end_test' now also covers side effects of done_testing, as well as
    END blocks, making it possible to use the warning(s) subs without having an
    end warning test while using done_testing (necessary when combining with
    the 'if' pragma)
  - END tests will not be added by a subequent use of Test::Warnings if a
    previous one passed ':no_end_test'
- Update dependencies

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.008-2
- Perl 5.18 rebuild

* Mon Jul 15 2013 Paul Howarth <paul@city-fan.org> - 0.008-1
- Update to 0.008
  - Compile test updated, to hopefully fix mswin32 parsing issues

* Wed Jul 10 2013 Paul Howarth <paul@city-fan.org> - 0.007-1
- Update to 0.007
  - Fix subtest tests to work on Test::More before 0.95_01 (CPAN RT#86802)
- BR: perl(Capture::Tiny)
- Bump perl(Module::Build::Tiny) version requirement to 0.024
- Bump perl(Test::CheckDeps) version requirement to 0.006
- Drop perl(Test::More) version requirement to 0.94

* Tue Jul  9 2013 Paul Howarth <paul@city-fan.org> - 0.006-2
- Sanitize for Fedora submission

* Tue Jul  9 2013 Paul Howarth <paul@city-fan.org> - 0.006-1
- Initial RPM version
