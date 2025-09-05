pkgname = "liboqs"
pkgver = "0.14.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["openssl3-devel"]
pkgdesc = "Quantum-resistant cryptography C library"
license = "MIT"
url = "https://openquantumsafe.org"
source = f"https://github.com/open-quantum-safe/liboqs/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5b0df6138763b3fc4e385d58dbb2ee7c7c508a64a413d76a917529e3a9a207ea"
options = ["empty"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("liboqs-devel")
def _(self):
    return self.default_devel()
