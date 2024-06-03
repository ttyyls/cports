pkgname = "python-pint"
pkgver = "0.23"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    "--benchmark-skip",
    "--deselect=pint/testsuite/test_quantity.py",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
checkdepends = [
    "python-pytest",
    "python-pytest-benchmark",
    "python-pytest-subtests",
]
pkgdesc = "Physical quantities module"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://github.com/hgrecco/pint"
source = f"$(PYPI_SITE)/P/Pint/Pint-{pkgver}.tar.gz"
sha256 = "e1509b91606dbc52527c600a4ef74ffac12fff70688aff20e9072409346ec9b4"


def post_install(self):
    self.install_license("LICENSE")
