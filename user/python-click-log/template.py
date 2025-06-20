pkgname = "python-click-log"
pkgver = "0.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-click"]
checkdepends = [*depends, "python-pytest"]
pkgdesc = "Logging integration for Click"
license = "MIT"
url = "https://github.com/click-contrib/click-log"
source = f"$(PYPI_SITE)/c/click-log/click-log-{pkgver}.tar.gz"
sha256 = "3970f8570ac54491237bcdb3d8ab5e3eef6c057df29f8c3d1151a51a9c23b975"


def post_install(self):
    self.install_license("LICENSE")
