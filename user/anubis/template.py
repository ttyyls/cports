pkgname = "anubis"
pkgver = "1.17.1"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/TecharoHQ/anubis.Version={pkgver}",
    "./cmd/anubis",
]
hostmakedepends = ["go"]
pkgdesc = "Proof-of-work sha256 challenge to stop AI crawlers"
license = "MIT"
url = "https://github.com/TecharoHQ/anubis"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "461420249c5860cc1caed87a750c2eba3a02b1102833f3588feff75c165be78e"
# needs net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
