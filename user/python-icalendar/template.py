pkgname = "python-icalendar"
pkgver = "6.3.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = ["python-dateutil"]
checkdepends = [
    "python-hypothesis",
    "python-pytest",
    "python-pytz",
    *depends,
]
pkgdesc = ""
license = "BSD-2-Clause"
url = "https://github.com/collective/icalendar"
source = f"$(PYPI_SITE)/i/icalendar/icalendar-{pkgver}.tar.gz"
sha256 = "a697ce7b678072941e519f2745704fc29d78ef92a2dc53d9108ba6a04aeba466"


def post_install(self):
    self.install_license("LICENSE.rst")
