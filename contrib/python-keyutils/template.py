pkgname = "python-keyutils"
pkgver = "1.6"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "python",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = [
    "gettext-devel",
    "keyutils-devel",
    "linux-headers",
    "python-cython",
    "python-devel",
]
pkgdesc = "Python bindings for keyutils"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://people.redhat.com/~dhowells/keyutils"
source = f"{url}/keyutils-{pkgver}.tar.bz2"
sha256 = "d3aef20cec0005c0fa6b4be40079885567473185b1a57b629b030e67942c7115"
env = {"USRLIBDIR": "/usr/lib"}
# tests rely on pytest-runner (deprecated)
# keyutils lib version mismatch
options = ["!check", "linkundefver"]


# def do_install(self):
#     pass
