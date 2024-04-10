pkgname = "qbe"
pkgver = "1.2"
pkgrel = 0
archs = ["x86_64", "aarch64", "riscv64"]
build_style = "makefile"
pkgdesc = "Compiler backend"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://c9x.me/compile"
source = f"{url}/release/qbe-{pkgver}.tar.xz"
sha256 = "a6d50eb952525a234bf76ba151861f73b7a382ac952d985f2b9af1df5368225d"
tool_flags = {"CFLAGS": ["-std=c99"]}


def post_install(self):
    self.install_license("LICENSE")
    self.install_files("doc", "usr/share", "qbe")
