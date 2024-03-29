pkgname = "swappy"
pkgver = "1.5.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = [
    "cairo-devel",
    "gettext-devel",
    "gtk+3-devel",
    "pango-devel",
]
pkgdesc = "Snapshot editing tool"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jtheoof/swappy"
source = f"https://github.com/jtheoof/swappy/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "266fac289d4b903d80d44746044bafe8a8b663c6032be696c651ad390bcb1850"
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
