pkgname = "typos"
pkgver = "1.29.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Source code spell checker"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT OR Apache-2.0"
url = "https://github.com/crate-ci/typos"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6427c063b5ee5003cb7878d3c655df204574d6a3f8ea8fd618cdab67177c27d9"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/typos")
    self.install_license("LICENSE-MIT")
