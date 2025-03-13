pkgname = "python-offpunk"
pkgver = "2.6"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = [
    "python-beautifulsoup4",
    "python-chardet",
    "python-cryptography",
    "python-feedparser",
    "python-readability-lxml",
    "python-lxml-html-clean",
    "python-setproctitle",
]
pkgdesc = "CLI offline-first smolnet browser/feed reader"
license = "AGPL-3.0-or-later"
url = "https://git.sr.ht/~lioploum/offpunk"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "58a6931dc15dcb43f4443a9b8feb7bcabc72a87d8c3cad758985b11a7928ea13"


def post_install(self):
    self.install_license("LICENSE")
