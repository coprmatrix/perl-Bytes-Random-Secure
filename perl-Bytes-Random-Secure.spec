#
# spec file for package perl-Bytes-Random-Secure
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-Bytes-Random-Secure
Version:        0.29
Release:        0
%define cpan_name Bytes-Random-Secure
Summary:        Perl extension to generate cryptographically-secure
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            http://search.cpan.org/dist/Bytes-Random-Secure/
Source0:        http://www.cpan.org/authors/id/D/DA/DAVIDO/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::Random::Seed)
BuildRequires:  perl(Math::Random::ISAAC)
BuildRequires:  perl(Scalar::Util) >= 1.21
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Crypt::Random::Seed)
Requires:       perl(Math::Random::ISAAC)
Requires:       perl(Scalar::Util) >= 1.21
%{perl_requires}

%description
the Bytes::Random::Secure manpage provides two interfaces for obtaining
crypto-quality random bytes. The simple interface is built around plain
functions. For greater control over the Random Number Generator's seeding,
there is an Object Oriented interface that provides much more flexibility.

The "functions" interface provides functions that can be used any time you
need a string of a specific number of random bytes. The random bytes are
available as simple strings, or as hex-digits, Quoted Printable, or MIME
Base64. There are equivalent methods available from the OO interface, plus
a few others.

This module can be a drop-in replacement for the Bytes::Random manpage,
with the primary enhancement of using a cryptographic-quality random number
generator to create the random data. The 'random_bytes' function emulates
the user interface of the Bytes::Random manpage's function by the same
name. But with Bytes::Random::Secure the random number generator comes from
the Math::Random::ISAAC manpage, and is suitable for cryptographic
purposes. The harder problem to solve is how to seed the generator. This
module uses the Crypt::Random::Seed manpage to generate the initial seeds
for Math::Random::ISAAC.

In addition to providing 'random_bytes()', this module also provides
several functions not found in the Bytes::Random manpage:
'random_string_from', 'random_bytes_base64()', 'random_bytes_hex', and
'random_bytes_qp'.

And finally, for those who need finer control over how the
Crypt::Random::Seed manpage generates its seed, there is an object oriented
interface with a constructor that facilitates configuring the seeding
process, while providing methods that do everything the "functions"
interface can do (truth be told, the functions interface is just a thin
wrapper around the OO version, with some sane defaults selected). The OO
interface also provides an 'irand' method, not available through the
functions interface.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples README

%changelog
