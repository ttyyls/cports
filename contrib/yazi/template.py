pkgname = "yazi"
pkgver = "0.3.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "oniguruma-devel",
    "rust-std",
]
pkgdesc = "Modal terminal file manager"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://yazi-rs.github.io"
source = f"https://github.com/sxyazi/yazi/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b1292be2d071a1a95fd7732baee8c22dd20f08c1facf560399e61e520dbee1e1"


def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/yazi")
    self.install_license("LICENSE")
    self.install_license("LICENSE-ICONS")
