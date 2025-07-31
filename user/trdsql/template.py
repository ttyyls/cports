pkgname = "trdsql"
pkgver = "1.1.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/noborus/trdsql.Version=v{pkgver}",
    "./cmd/trdsql"
]
hostmakedepends = ["go"]
pkgdesc = "Execute SQL queries on documents"
license = "MIT"
url = "https://github.com/noborus/trdsql"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e3b8bef57330648d3f4b279bd4c652eaeba19aa4fae3fe05cfa596a2b3f4bc51"


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("completion/trdsql-completion.zsh")
