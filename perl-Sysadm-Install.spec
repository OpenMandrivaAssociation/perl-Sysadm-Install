%define upstream_name Sysadm-Install
%define upstream_version 0.44

Summary:	Typical installation tasks for system administrators
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Sysadm-Install/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSCHILLI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(Config)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Expect)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Temp) >= 0.16
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Status)
BuildRequires:	perl(Log::Log4perl) >= 1.00
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Term::ReadKey)
# For test suite
BuildRequires:	perl(Test::More)
# Runtime deps not automatically picked up by RPM
Requires:	perl(Archive::Tar)
Requires:	perl(Config)
Requires:	perl(Encode)
Requires:	perl(Expect)
Requires:	perl(HTTP::Request)
Requires:	perl(HTTP::Status)
Requires:	perl(LWP::UserAgent)

BuildArch:	noarch

%description
"Sysadm::Install" executes shell-like commands performing typical
installation tasks: Copying files, extracting tarballs, calling "make".
It has a "fail once and die" policy, meticulously checking the result of
every operation and calling "die()" immediately if anything fails,
with optional logging of everything.

"Sysadm::Install" also supports a *dry_run* mode, in which it logs
everything, but suppresses any write actions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test 

%install
%makeinstall_std

%files
%doc Changes README 
%{_bindir}/one-liner
%{perl_vendorlib}/*
%{_mandir}/man3/*
