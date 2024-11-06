pkgname = "acme-client"
pkgver = "1.3.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "bison", "pkgconf"]
makedepends = ["openssl-devel"]
pkgdesc = "Client for issuing certificates from ACME-complaint servers"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-only"
url = "https://git.wolfsden.cz/acme-client-portable"
source = f"{url}/snapshot/acme-client-portable-{pkgver}.tar.gz"
sha256 = "3a38f2911b01e83779f8b274485a2ed44028eafa8fea05ee2e612e134b79cba9"
# tests fail
options = ["!check"]
