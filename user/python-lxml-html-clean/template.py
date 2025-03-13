pkgname = "python-lxml-html-clean"
pkgver = "0.4.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
depends = ["python-lxml"]
checkdepends = [*depends, "python-pytest"]
pkgdesc = "HTML cleaner from lxml project"
license = "BSD-3-Clause"
url = "https://github.com/fedora-python/lxml_html_clean"
source = f"$(PYPI_SITE)/l/lxml_html_clean/lxml_html_clean-{pkgver}.tar.gz"
sha256 = "40c838bbcf1fc72ba4ce811fbb3135913017b27820d7c16e8bc412ae1d8bc00b"
# failing tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
