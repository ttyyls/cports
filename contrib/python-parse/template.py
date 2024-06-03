pkgname = "python-parse"
pkgver = "1.20.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Parse strings according to python's format() syntax"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/r1chardj0n3s/parse"
source = f"$(PYPI_SITE)/p/parse/parse-{pkgver}.tar.gz"
sha256 = "09002ca350ad42e76629995f71f7b518670bcf93548bdde3684fd55d2be51975"


def post_install(self):
    self.install_license("LICENSE")
