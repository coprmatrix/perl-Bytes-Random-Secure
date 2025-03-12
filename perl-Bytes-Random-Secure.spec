#
# spec file for package perl-Bytes-Random-Secure (Version 0.29)
#
# Copyright (c) 125 SUSE LLC
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

%define cpan_name Bytes-Random-Secure
Name:           perl-Bytes-Random-Secure
Version:        0.29
Release:        0%{?autorelease}
License:   Artistic-1.0 or GPL-1.0-or-later
Summary:        Perl extension to generate cryptographically-secure random bytes
Url:            https://metacpan.org/release/%{cpan_name}
Source0:         https://cpan.metacpan.org/authors/id/D/DA/DAVIDO/%{cpan_name}-%{version}.tar.gz
Source1:     cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl-macros-suse
BuildRequires:  perl-generators
BuildRequires:  perl(Crypt::Random::Seed)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.56
BuildRequires:  perl(Math::Random::ISAAC)
BuildRequires:  perl(Scalar::Util) >= 1.21
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  make
Requires:       perl(Crypt::Random::Seed)
Requires:       perl(Math::Random::ISAAC)
Requires:       perl(Scalar::Util) >= 1.21
%{?perl_requires}

%description
Bytes::Random::Secure provides two interfaces for obtaining crypto-quality
random bytes. The simple interface is built around plain functions. For
greater control over the Random Number Generator's seeding, there is an
Object Oriented interface that provides much more flexibility.

The "functions" interface provides functions that can be used any time you
need a string of a specific number of random bytes. The random bytes are
available as simple strings, or as hex-digits, Quoted Printable, or MIME
Base64. There are equivalent methods available from the OO interface, plus
a few others.

This module can be a drop-in replacement for Bytes::Random, with the
primary enhancement of using a cryptographic-quality random number
generator to create the random data. The 'random_bytes' function emulates
the user interface of Bytes::Random's function by the same name. But with
Bytes::Random::Secure the random number generator comes from
Math::Random::ISAAC, and is suitable for cryptographic purposes. The harder
problem to solve is how to seed the generator. This module uses
Crypt::Random::Seed to generate the initial seeds for Math::Random::ISAAC.

In addition to providing 'random_bytes()', this module also provides
several functions not found in Bytes::Random: 'random_string_from',
'random_bytes_base64()', 'random_bytes_hex', and 'random_bytes_qp'.

And finally, for those who need finer control over how Crypt::Random::Seed
generates its seed, there is an object oriented interface with a
constructor that facilitates configuring the seeding process, while
providing methods that do everything the "functions" interface can do
(truth be told, the functions interface is just a thin wrapper around the
OO version, with some sane defaults selected). The OO interface also
provides an 'irand' method, not available through the functions interface.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1


%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
echo fine

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist




%files -f %{name}.files
%doc Changes examples README


%changelog
