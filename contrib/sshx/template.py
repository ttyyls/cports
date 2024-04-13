pkgname = "sshx"
pkgver = "0.2.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf", "protobuf"]
makedepends = ["rust-std", "protobuf-devel", "zstd-devel"]
pkgdesc = "Terminal sharing over the web"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/ekzhang/sshx"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "343a98cc8f18079e1f779b100ab8af12b506fa77ee6d63f07697e261920dfd79"


def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/sshx")
    self.install_license("LICENSE")
