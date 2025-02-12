pkgname = "python-bottles"
pkgver = "0.13.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
pkgdesc = "WSGI micro web framework for python"
maintainer = "ttyyls <contac@behri.org>"
license = "MIT"
url = "https://bottlepy.org/docs/dev"
source = f"https://github.com/bottlepy/bottle/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "638e4fdd64ee55becd0a591ecf4aaddf27c319f5254b6bcb6959130c00c6e793"


def post_install(self):
    self.install_license("LICENSE")
