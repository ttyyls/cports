pkgname = "jsonnet-language-server"
pkgver = "0.15.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Language Server Protocol server for Jsonnet"
license = "AGPL-3.0-or-later"
url = "https://jsonnet.org"
source = f"https://github.com/grafana/jsonnet-language-server/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "085085ad1c8c75cb178876726b5a974027058cab9a83dff6435aa5681f687517"


def post_install(self):
    self.install_license("LICENSE")
