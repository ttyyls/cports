pkgname = "git-who"
pkgver = "0.6"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Git blame for file trees"
license = "MIT"
url = "https://github.com/sinclairtarget/git-who"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4d81d2bdbd3fb2a0f393feb76981e33b3d31aa49bf97b4c0a69bad148aa8fbc0"


def post_install(self):
    self.install_license("LICENSE")
