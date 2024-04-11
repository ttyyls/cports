pkgname = "keepassxc"
pkgver = "2.7.8"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DPRINT_SUMMARY=1",
    "-DWITH_XC_ALL=1",
    "-DWITH_XC_UPDATECHECK=OFF",
]
hostmakedepends = [
    "asciidoc",
    "cmake",
    "ninja",
    "qt6ct",
    "qt6-qttools",
]
makedepends = [
    "argon2-devel",
    "botan-devel",
    "dbus-devel",
    "libxi-devel",
    "libxtst-devel",
    "minizip-devel",
    "qrencode-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "readline-devel",
    "zlib-devel",
]
pkgdesc = "Password manager"
maintainer = "ttyyls <contact@behri.org>"
license = (
    "GPL-3.0-or-later AND LGPL-2.1-only WITH custom:Nokia-Qt-exception-1.1 "
    "AND LGPL-3.0-only AND BSD-3-Clause AND MIT AND BSL-1.0 AND CC0-1.0"
)
url = "https://keepassxc.org"
source = f"https://github.com/keepassxreboot/keepassxc/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b85848a8d72deeadf2a201a926864165a7779a46af2fbc3d165efcd1d8645dcb"


def post_install(self):
    self.install_license("COPYING")
    self.install_license("LICENSE.BSD")
    self.install_license("LICENSE.MIT")
