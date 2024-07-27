pkgname = "staticcheck"
pkgver = "2023.1.7"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/staticcheck"]
hostmakedepends = ["go"]
pkgdesc = "Advanced GO linter"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://staticcheck.dev"
source = (
    f"https://github.com/dominikh/go-tools/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "9e4c710e79f9b18626ff33d225587518f2005ce9c651eda3b2fa539ee4677a20"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE-THIRD-PARTY")
