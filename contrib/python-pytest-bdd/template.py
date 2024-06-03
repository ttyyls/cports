pkgname = "python-pytest-bdd"
pkgver = "7.1.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = [
    "python-mako",
    "python-packaging",
    "python-parse",
    "python-parse-type",
    "python-pytest",
    "python-typing_extensions",
]
checkdepends = ["p"]
pkgdesc = "BDD plugin for pytest"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-bdd"
source = f"$(PYPI_SITE)/p/pytest-bdd/pytest_bdd-{pkgver}.tar.gz"
sha256 = "b992536360f49441ac25b687f092d02815582b60b2acb3f62fce16b7b6e7273d"
# pypi tarball has no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
