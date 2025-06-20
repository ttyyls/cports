pkgname = "khal"
pkgver = "0.13.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools_scm",
]
depends = [
    "python-click",
    "python-click-log",
    "python-configobj",
    "python-dateutil",
    "python-icalendar",
    "python-pytz",
    "python-pyxdg",
    "python-tzlocal",
    "python-urwid",
]
checkdepends = [
    "python-aiohttp",
    "python-freezegun",
    "python-hypothesis",
    "python-pytest",
    "python-vdirsyncer",
    *depends,
]
pkgdesc = "Standards based CLI calendar program"
license = "MIT"
url = "https://lostpackets.de/khal"
source = f"$(PYPI_SITE)/k/khal/khal-{pkgver}.tar.gz"
sha256 = "68fea8cd704e387e81b669c90322a8dafb4374f5876b07170c9c6e23415a3ee0"


def post_install(self):
    self.install_license("COPYING")
