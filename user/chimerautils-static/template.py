pkgname = "chimerautils-static"
pkgver = "14.0.7"
pkgrel = 0
_wip = "ad1717fd62d12621a421c3ca9ce1b1d019a3b565"
build_style = "meson"
configure_args = [
    "-Dstatic=enabled",
    "-Dstatic_fts=true",
    "-Dstatic_rpmatch=true",
]
hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
makedepends = [
    "acl-devel-static",
    "bzip2-devel-static",
    "libatomic-chimera-devel-static",
    "libedit-devel-static",
    "libunwind-devel-static",
    "libxo-devel",
    "linux-headers",
    "musl-bsd-headers",
    "musl-devel-static",
    "musl-fts-devel",
    "musl-rpmatch-devel",
    "ncurses-devel-static",
    "openssl-devel-static",
    "xz-devel-static",
    "zlib-devel-static",
    "zstd-devel-static",
]
pkgdesc = "Chimera Linux userland (statically linked)"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/chimerautils"
source = f"https://github.com/ttyyls/chimerautils/archive/{_wip}.tar.gz"
sha256 = "a45298008bc6bae2ad21f8c0c3ee34477d440f0008e2741071ee1dd175c1f50e"


def do_install(self):
    self.install_bin("build/src.freebsd/sh/sh.static")


def post_install(self):
    self.install_license("LICENSE")
