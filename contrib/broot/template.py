pkgname = "broot"
pkgver = "1.42.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "oniguruma-devel",
    "rust-std",
    "zlib-ng-compat-devel",
]
pkgdesc = "Filesystem visualization and traversal tool"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://dystroy.org/broot"
source = f"https://github.com/Canop/broot/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f8a206d44b55287f47cdb63e2f19c9022d55d49f9399e5461f7797ccbe0264ba"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/page", cat=1, name="broot")
