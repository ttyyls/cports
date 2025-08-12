pkgname = "python-himitsu"
pkgver = "0.0.9"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = [
    "python-cryptography",
    "python-dbus",
    "python-gobject",
    "python-prctl",
]
checkdepends = ["python-pytest"]
pkgdesc = "Himitsu client library"
license = "MIT"
url = "https://git.sr.ht/~apreiml/py-himitsu"
source = f"$(PYPI_SITE)/p/py_himitsu/py_himitsu-{pkgver}.tar.gz"
sha256 = "45de3188fc56011f8121bba6f43bd59ebddf8d1e2e3a24e32f2479b725ec92ce"


def post_install(self):
    self.install_license("COPYING")
