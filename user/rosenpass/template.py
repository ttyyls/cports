pkgname = "rosenpass"
pkgver = "0.2.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "pkgconf",
]
makedepends = [
    "liboqs-devel",
    "libsodium-devel",
    "linux-headers",
    "rust-std",
]
depends = [
    "bash",
    "git",
    "wireguard-tools",
]
pkgdesc = "Post-quantum-secure VPN using WireGuard"
license = "Apache-2.0 AND MIT"
url = "https://github.com/rosenpass/rosenpass"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0077cca7595a467a638988fab5267f89421d1b7589849d14c2db60636b8f353a"


def install(self):
    self.install_license("LICENSE-MIT")
    self.install_bin(f"target/{self.profile().triplet}/release/rosenpass")
    self.install_bin("rp")
    self.install_man("doc/rp.1")
