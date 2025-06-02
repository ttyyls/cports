pkgname = "git-stack"
pkgver = "0.10.18"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Stacked branch management for Git"
license = "MIT OR Apache-2.0"
url = "https://github.com/gitext-rs/git-stack"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "46786c7509ba27a36225835aa8689445b6249d6491cf104f5a0168f8edd7ab89"


def post_install(self):
    self.install_license("LICENSE-MIT")
