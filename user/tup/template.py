pkgname = "tup"
pkgver = "0.8"
pkgrel = 0
build_style = "makefile"
make_cmd = "./build.sh"
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = [
    "fuse-devel",
    "pcre2-devel",
    "sqlite-devel",
]
pkgdesc = "File based build system"
license = "GPL-2.0-only"
url = "https://gittup.org/tup"
source = f"https://gittup.org/tup/releases/tup-v{pkgver}.tar.gz"
sha256 = "840f95f5e372364904862dc5f0bb5ef2628cf7b7814b46ce7a5137d4ae0266fb"
hardening = ["vis", "cfi"]
# bootstraps before build
options = ["!cross"]


def install(self):
    self.install_bin("build/tup")
    self.install_man("tup.1")
