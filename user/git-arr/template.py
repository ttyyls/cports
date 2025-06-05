pkgname = "git-arr"
pkgver = "0.31"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
pkgdesc = "Git repository browser using static html"
license = "MIT"
url = "https://blitiri.com.ar/p/git-arr"
source = f"{url}/files/0.31/git-arr-{pkgver}.tar.gz"
sha256 = "3942a75dc3e0d725c67676088a09f565451f5764dee29716ba78a41dbf673bed"


def post_install(self):
    self.install_license("LICENSE")
