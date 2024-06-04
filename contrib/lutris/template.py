pkgname = "lutris"
pkgver = "0.5.17"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "gettext-devel"]
makedepends = ["gettext-devel"]
depends = [
    "7zip",
    "cabextract",
    "gtk+3",
    "mesa-utils",
    "pciutils",
    "psmisc",
    "python-certifi",
    "python-dbus",
    "python-distro",
    "python-evdev",
    "python-gobject",
    "python-lxml",
    "python-magic",
    "python-pillow",
    "python-pypresence",
    "python-pyyaml",
    "python-requests",
    "unzip",
    "webkitgtk4",
    "xgamma",
]
pkgdesc = "Video game preservation platform"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://lutris.net"
source = f"https://github.com/lutris/lutris/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e913d0c70bcb8c29839fcc2368f0b672bc1e70d1bc2bc18e6fd50ac785261aa8"
# no tests defined
options = ["!check"]
