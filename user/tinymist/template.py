pkgname = "tinymist"
pkgver = "0.12.22"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--features=cli", "--bin", "tinymist", "--bin", "typlite"]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel"]
depends = ["typst"]
pkgdesc = "Language server for Typst"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://myriad-dreamin.github.io/tinymist"
source = f"https://github.com/Myriad-Dreamin/tinymist/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e423ecbc57bedec806d7d7c7b63d51c5d03ae68a626b55c04d11ffba2d0d298c"
# takes forever
options = ["!check"]

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_build(self):
    for shell in ["bash", "fish", "zsh", "nushell"]:
        with open(self.cwd / f"tinymist.{shell}", "w") as f:
            self.do(
                f"./target/{self.profile().triplet}/release/tinymist",
                "completion",
                shell,
                stdout=f,
            )


def install(self):
    for shell in ["bash", "fish", "zsh", "nushell"]:
        self.install_completion(f"tinymist.{shell}", shell)
    self.install_bin(f"target/{self.profile().triplet}/release/tinymist")
    self.install_bin(f"target/{self.profile().triplet}/release/typlite")
