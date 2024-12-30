pkgname = "python-atomicwrites"
pkgver = "1.4.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Atomic file writes"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/untitaker/python-atomicwrites"
source = f"$(PYPI_SITE)/a/atomicwrites/atomicwrites-{pkgver}.tar.gz"
sha256 = "81b2c9071a49367a7f770170e5eec8cb66567cfbbc8c73d20ce5ca4a8d71cf11"


def post_install(self):
    self.install_license("LICENSE")
