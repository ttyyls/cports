pkgname = "python-more-itertools"
pkgver = "10.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "More routines for operating on iterables, beyond itertools"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/more-itertools/more-itertools"
source = f"$(PYPI_SITE)/m/more-itertools/more-itertools-{pkgver}.tar.gz"
sha256 = "8fccb480c43d3e99a00087634c06dd02b0d50fbf088b380de5a41a015ec239e1"


def post_install(self):
    self.install_license("LICENSE")
