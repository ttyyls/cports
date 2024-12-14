pkgname = "chisel"
pkgver = "1.10.1"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags", f"-X github.com/jpillora/chisel/share.BuildVersion={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "TCP/UDP tunnel, transported over HTTP, secured via SSH"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jpillora/chisel"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "85d121087ea3e1139f63eaa389642bd6d8c2584728ec80d16315b17410844269"


def post_install(self):
    self.install_license("LICENSE")
