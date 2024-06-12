pkgname = "sapling"
pkgver = "0.2.20240718"
_ref = "145624+f4e9df48"
pkgrel = 0
build_style = "cargo"
make_dir = "eden/scm"
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "ninja",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
    "yarn",
]
makedepends = [
    "openssl-devel",
    "rust-std",
    "zstd-devel",
]
pkgdesc = "Scalable and user friendly vcs"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-only"
url = "https://sapling-scm.com"
source = f"https://github.com/facebook/sapling/archive/refs/tags/{pkgver}-{_ref}.tar.gz"
sha256 = "8081d405cddb9dc4eadd96f4c948b7686b0b61f641c068fc87b9c27518fb619e"


def post_prepare(self):
    self.do("yarn", allow_network=True)


@subpackage("sapling-isl")
def _(self):
    self.subdesc = "interactive smartlog webui"
    self.depends = ["nodejs"]

    return ["usr/bin/sapling-isl"]
