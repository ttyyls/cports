pkgname = "mise"
pkgver = "2024.10.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo",
    "pkgconf",
]
makedepends = [
    "libgit2-devel",
    "openssl-devel",
    "rust-std",
    "zstd-devel",
]
pkgdesc = "Dev tools, env vars, task runner"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://mise.jdx.dev"
source = f"https://github.com/jdx/mise/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bf9d99fb8416f33e3828baf770b4d71d8a548ed75c11178e1e1763cfd619c64f"
# check env is unsuitable for most
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/mise")
    self.install_license("LICENSE")
    self.install_man("man/man1/mise.1")
