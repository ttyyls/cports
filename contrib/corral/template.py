pkgname = "corral"
pkgver = "0.8.1"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["ponyc"]
makedepends = ["pony-std"]
pkgdesc = "Pony dependency management tool"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-2-Clause"
url = "https://github.com/ponylang/corral"
source = f"https://github.com/ponylang/corral/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a6c95833ec4bd0fcdc2ba5dd3f5ab509c0a500a086f6be8df22f28c752148dc1"


def post_install(self):
    self.install_license("LICENSE")
