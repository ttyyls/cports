pkgname = "himitsu"
pkgver = "0.9"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["hare", "scdoc"]
makedepends = ["hare"]
pkgdesc = "Secret storage system"
license = "GPL-3.0-only"
url = "https://himitsustore.org"
source = f"https://git.sr.ht/~sircmpwn/himitsu/archive/{pkgver}.tar.gz"
sha256 = "369e65b7a6fcfd90078a12abc25e25c1d161eb33f9eda01a6ed8d4ade74fbbcc"


def post_install(self):
    self.insatll_service("^/himitsu.user")
