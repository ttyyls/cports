pkgname = "rapidcheck"
pkgver = "0_git20231214"
_commit = "ff6af6fc683159deb51c543b065eba14dfcf329b"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DRC_ENABLE_GTEST=ON",
    "-DBUILD_SHARED_LIBS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "QuickCheck clone for C++"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-2-Clause"
url = "https://github.com/emil-e/rapidcheck"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "7ae7a8d59560f94eb68ed09fda59abd9871fe3b0cfc5acc60506de506289aa24"


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("rapidcheck-devel")
def _(self):
    return self.default_devel()
