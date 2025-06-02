pkgname = "nerdlog"
pkgver = "1.8.1"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/dimonomid/nerdlog/version.version={pkgver}",
    "./cmd/nerdlog",
]
hostmakedepends = ["go"]
makedepends = ["libx11-devel"]
pkgdesc = "Remote-first, multi-host TUI log viewer"
license = "BSD-2-Clause"
url = "https://github.com/dimonomid/nerdlog"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3cc38db15e57e8106f1d2da571136b0ea4dab74a351f577a3ce8d63a16900fa1"


def post_install(self):
    self.install_license("LICENSE")
