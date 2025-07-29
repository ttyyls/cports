pkgname = "plumber"
pkgver = "2.9.0"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X github.com/streamdal/option.VERSION=v{pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Cli tool for interacting with messaging systems"
license = "MIT"
url = "https://github.com/streamdal/plumber"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6ccdf3231a2789cbdb8d9258e88a3e33b97c0e8575c99a8b7ac240a666a84a43"


def install(self):
    self.install_bin("build/plumber")
    self.install_license("LICENSE")
