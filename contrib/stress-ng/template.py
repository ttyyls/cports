pkgname = "stress-ng"
pkgver = "0.17.06"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = [
    "acl-devel",
    "attr-devel",
    "libaio-devel",
    "libbsd-devel",
    "libcap-devel",
    "libmd-devel",
    "libjpeg-turbo-devel",
    "linux-headers",
    "xxhash-devel",
    "zlib-devel",
]
pkgdesc = "Stress test a computer in various selectable ways"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/ColinIanKing/stress-ng"
source = f"https://github.com/ColinIanKing/stress-ng/archive/refs/tags/V{pkgver}.tar.gz"
sha256 = "f81dc1ea7f2a821dab11e46cf3a3a893ad45299e51e6976041306871ddbc7f5d"
env = {
    "MAN_COMPRESS": "1",
    "PRESERVE_CFLAGS": "1",
}
hardening = ["vis", "cfi"]
# no portable tests defined
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
