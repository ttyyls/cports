pkgname = "qlot"
pkgver = "1.7.1"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["sbcl"]
pkgdesc = "Project local library installer for Common Lisp"
license = "MIT"
url = "https://qlot.tech"
source = f"https://github.com/fukamachi/qlot/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0712d5a6b34441a2b97e85621ce20b62ed50fa367fc3e81c04f652fb83beda8f"


def post_install(self):
    self.install_license("LICENSE.txt")
