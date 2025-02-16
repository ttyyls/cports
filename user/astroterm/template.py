pkgname = "astroterm"
pkgver = "1.0.7"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Terminal planetarium"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/da-luce/astroterm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3b8b1597afb31d1cb8ad54030b5766652b4d3f42f0a3d510bbc3191c0c6a4aa5"


def post_install(self):
    self.install_license("LICENSE")
