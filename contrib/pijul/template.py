pkgname = "pijul"
pkgver = "9"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=keep-changes,openssl,git",
]
make_install_args = list(make_build_args)
make_check_args = list(make_build_args)
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "libsodium-devel",
    "openssl-devel",
    "rust-std",
]
pkgdesc = "Distributed vcs based on theory of patches"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://pijul.org"
source = (
    f"https://static.crates.io/crates/pijul/pijul-1.0.0-beta.{pkgver}.crate"
)
sha256 = "c51a43abf66dfdd63393f9d7e426129a769c7345d64d451a30be9399733062d2"
# generates completion with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "zsh", "fish"]:
        with open(self.cwd / f"pijul.{shell}", "w") as outf:
            self.do(
                f"{self.chroot_cwd}/target/release/pijul",
                "completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    for shell in ["bash", "zsh", "fish"]:
        self.install_completion(f"pijul.{shell}", shell)
