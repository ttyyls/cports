pkgname = "flirt"
pkgver = "0.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "File interaction tool for the command line"
license = "BSD-3-Clause"
url = "https://git.sr.ht/~hadronized/flirt"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "58879c33a6b14a7c33335dcc3d93b78eee022251841bd59f020e9f26920c89d6"


def post_install(self):
    self.install_license("LICENSE")
