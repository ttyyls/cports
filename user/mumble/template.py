pkgname = "mumble"
pkgver = "1.5.735"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Voice Over IP solution"
license = "BSD-3-Clause"
url = "https://www.mumble.info"
source = (
    f"https://github.com/mumble-voip/mumble/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = ""

def post_install(self):
    self.install_license("LICENSE")
