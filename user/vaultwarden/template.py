pkgname = "vaultwarden"
pkgver = "1.32.3"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=sqlite,postgresql",
]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "libpq-devel",
    "openssl-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "Bitwarden compatible server"
maintainer = "ttyyls <contact@behri.org>"
license = "AGPL-3.0-or-later"
url = "https://github.com/dani-garcia/vaultwarden"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "026ee532f3fea0c6707f3d83eaad44327dd8e845bc6f367a8d8e2ee482a8518c"


def post_install(self):
    self.install_license("LICENSE.txt")
