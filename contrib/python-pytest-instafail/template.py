pkgname = "python-pytest-instafail"
pkgver = "0.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Pytest plugin to show failures instantly"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://github.com/pytest-dev/pytest-instafail"
source = f"$(PYPI_SITE)/p/pytest-instafail/pytest-instafail-{pkgver}.tar.gz"
sha256 = "33a606f7e0c8e646dc3bfee0d5e3a4b7b78ef7c36168cfa1f3d93af7ca706c9e"


def post_install(self):
    self.install_license("LICENSE")
