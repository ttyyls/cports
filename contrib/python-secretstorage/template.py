pkgname = "python-secretstorage"
pkgver = "3.3.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-cryptography",
    "python-jeepney",
]
checkdepends = depends + [
    "dbus",
    "gnome-keyring",
    "python-pytest",
]
pkgdesc = "Python bindings to freedesktop secret service api"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://secretstorage.readthedocs.io/en/latest"
source = f"$(PYPI_SITE)/S/SecretStorage/SecretStorage-{pkgver}.tar.gz"
sha256 = "2403533ef369eca6d2ba81718576c5e0f564d5cca1b58f73a8b23e7d4eeebd77"


def post_install(self):
    self.install_license("LCENSE")
