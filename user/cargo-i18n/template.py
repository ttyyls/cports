pkgname = "cargo-i18n"
pkgver = "3.1.2"
pkgrel = 0
build_wrksrc = "crates/cli"
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Internalization utility for rust"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/longbridgeapp/rust-i18n"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "75b1a34951df070cc7ad83be0adaf0b950b55962d7c347990d73c40bc9b488ec"
# no tests defined
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cargo-i18n")
    self.install_license("LICENSE")
