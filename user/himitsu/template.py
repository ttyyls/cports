pkgname = "himitsu"
pkgver = "0.8"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["hare", "scdoc"]
makedepends = ["hare-std"]
pkgdesc = "Secret storage system"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-only"
url = "https://himitsustore.org"
source = f"https://git.sr.ht/~sircmpwn/himitsu/archive/{pkgver}.tar.gz"
sha256 = "fc670b24984de5d32df2e8ac34284fdbdaf83352c63c7910b334bfe941ea06ab"

if self.profile().cross:
    make_build_args += [f"HAREFLAGS='-a{self.profile().arch}'"]


def init_build(self):
    self.make_jobs = 1
