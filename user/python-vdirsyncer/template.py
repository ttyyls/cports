pkgname = "python-vdirsyncer"
pkgver = "0.19.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = [
    "python-aiohttp",
    "python-click",
    "python-click-log",
    "python-multidict",
    "python-requests",
    "python-urllib3",
]
checkdepends = [
    # "pytest-pytest-asyncio",
    # "python-aioresponses",
    "python-hypothesis",
    "python-pytest",
    "python-pytest-httpserver",
    "python-trustme",
    *depends,
]
pkgdesc = "Synchronize calendars and contacts"
license = "BSD-3-Clause"
url = "https://vdirsyncer.pimutils.org"
source = f"$(PYPI_SITE)/v/vdirsyncer/vdirsyncer-{pkgver}.tar.gz"
sha256 = "e437851feb985dec3544654f8f9cf6dd109b0b03f7e19956086603092ffeb28f"


def post_install(self):
    self.install_license("LICENSE")
