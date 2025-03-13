pkgname = "python-feedparser"
pkgver = "6.0.11"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
pkgdesc = "Feed parser library for rss/atom"
license = "BSD-2-Clause"
url = "https://feedparser.readthedocs.io"
source = f"$(PYPI_SITE)/f/feedparser/feedparser-{pkgver}.tar.gz"
sha256 = "c9d0407b64c6f2a065d0ebb292c2b35c01050cc0dc33757461aaabdc4c4184d5"


def post_install(self):
    self.install_license("LICENSE")
