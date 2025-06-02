pkgname = "dive"
pkgver = "0.13.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
make_build_args = [f"-ldflags=-X main.version={pkgver}"]
pkgdesc = "Tool for exploring each layer in a docker image"
license = "MIT"
url = "https://github.com/wagoodman/dive"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2a9666e9c3fddd5e2e5bad81dccda520b8102e7cea34e2888f264b4eb0506852"


def post_install(self):
    self.install_license("LICENSE")
