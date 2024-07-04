pkgname = "oksh.static"
pkgver = "7.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-static"]
configure_gen = []
make_dir = "."
makedepends = [
    "libatomic-chimera-devel-static",
    "libunwind-devel-static",
    "musl-devel-static",
    "ncurses-devel",
]
pkgdesc = "Portable OpenBSD ksh, based on the Public Domain Korn Shell (pdksh)"
maintainer = "ttyyls <contact@behri.org>"
license = "custom:none"
url = "https://github.com/ibara/oksh"
source = f"{url}/releases/download/oksh-{pkgver}/oksh-{pkgver}.tar.gz"
sha256 = "40b895c3f8e9311bfe2b230e9b3786712550ef488ced33bfd7cd3f89fceeed5d"
hardening = ["vis", "cfi"]
# There are no tests
options = ["!check"]


def do_install(self):
    self.install_bin("oksh", name="oksh.static")
