pkgname = "udiskie"
pkgver = "2.5.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python",
    "python-build",
    "python-setuptools",
    "python-wheel",
]
makedepends = [
    "python-keyutils",
    "python-pyyaml",
    "python-gobject",
]
checkdepends = ["python-pytest"]
pkgdesc = "Automounter for removable media"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/coldfix/udiskie"
source = (
    f"https://github.com/coldfix/udiskie/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "6971adaa00dcd6b799b8a0b62c47103e0ad9a3f1880112c51ccc662316d2b306"


def post_install(self):
    self.install_license("MIT")
