pkgname = "multitail"
pkgver = "7.1.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
makedepends = ["ncurses-devel"]
pkgdesc = "Follow multiple files with filters and wildcards"
license = "MIT"
url = "https://github.com/folkertvanheusden/multitail"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b0c92bf5f504b39591bf3e2e30a1902925c11556e14b89a07cfa7533f9bd171b"


def post_install(self):
    self.install_license("LICENSE")
