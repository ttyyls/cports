pkgname = "gleam"
pkgver = "1.7.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
checkdepends = ["git"]
pkgdesc = "Gleam programming language"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://gleam.run"
source = (
    f"https://github.com/gleam-lang/gleam/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "e1a2081705b50c3a335424d6052e0aeb9dd85bca5daf6ab28a7ada7a0ba24841"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gleam")
