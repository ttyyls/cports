pkgname = "lem"
pkgver = "2.2.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["qlot", "sbcl"]
pkgdesc = "Common Lisp editor/IDE with high expansibility"
license = "MIT"
url = "http://lem-project.github.io"
source = (
    f"https://github.com/lem-project/lem/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "7dcfff8a56190da64518ae97cd37962678cad4b6f6a1804045d92bf95c6e9d0b"


def post_install(self):
    self.install_license("LICENCE")
