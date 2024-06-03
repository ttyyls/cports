pkgname = "python-vulture"
pkgver = "2.11"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest", "python-pint"]
pkgdesc = "Find dead python code"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jendrikseipp/vulture"
source = f"$(PYPI_SITE)/v/vulture/vulture-{pkgver}.tar.gz"
sha256 = "f0fbb60bce6511aad87ee0736c502456737490a82d919a44e6d92262cb35f1c2"


def post_install(self):
    self.install_license("LICENSE.txt")
