pkgname = "perl-file-mimeinfo"
pkgver = "0.35"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = [
    "perl",
    "perl-file-basedir",
    "perl-file-desktopentry",
    "perl-encode-locale",
]
depends = [*makedepends]
pkgdesc = "Parses streams to create MIME entities"
maintainer = "ttyyls <contact@behri.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/dist/File-MimeInfo"
source = f"$(CPAN_SITE)/File/File-MimeInfo-{pkgver}.tar.gz"
sha256 = "9717cb6cc4998640100d5405a1594330d38a6ba37fb1dce482f59816c981fcc1"
