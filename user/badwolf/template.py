pkgname = "badwolf"
pkgver = "1.3.0"
pkgrel = 0
build_style = "configure"
make_cmd = "ninja"
hostmakedepends = ["ninja", "pkgconf", "gettext-devel"]
makedepends = ["libxml2-devel", "webkitgtk-devel"]
pkgdesc = "Minimalist WebKitGTK+ browser"
license = "BSD-3-Clause AND MPL-2.0 AND CC-BY-SA-4.0"
url = "https://hacktivis.me/projects/badwolf"
source = f"https://distfiles.hacktivis.me/releases/badwolf-{pkgver}.tar.gz"
sha256 = "276dfccba8addfc205ceb10477668e4b2b6a4853f344c86d5c1e35b1c703459f"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSES/BSD-3-Clause.txt")
