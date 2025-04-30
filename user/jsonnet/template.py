pkgname = "jsonnet"
pkgver = "0.21.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DUSE_SYSTEM_GTEST=ON",
    "-DUSE_SYSTEM_JSON=ON",
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
]
hostmakedepends = ["cmake", "ninja"]
makedepends = ["nlohmann-json", "gtest-devel"]
pkgdesc = "Data templating language"
license = "Apache-2.0"
url = "https://jsonnet.org"
source = f"https://github.com/google/jsonnet/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a12ebca72e43e7061ffe4ef910e572b95edd7778a543d6bf85f6355bd290300e"


@subpackage("jsonnet-devel")
def _(self):
    return self.default_devel()


@subpackage("jsonnet-progs")
def _(self):
    return self.default_devel()
