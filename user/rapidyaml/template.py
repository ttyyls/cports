pkgname = "rapidyaml"
pkgver = "0.9.0"
_c4ver = "0.2.6"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Library to parse and emit YAML"
license = "MIT"
url = "https://github.com/biojppm/rapidyaml"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/biojppm/c4core/archive/refs/tags/v{_c4ver}.tar.gz",
]
source_paths = [".", "ext/c4core"]
sha256 = [
    "78e62e35b61bb59db53213cc0cfc1ad408a59e62fb66af30a886b75427f26321",
    "a8877d95198da5efe30624a861bab5089ab67b4228e0ebce25c30f080298c981",
]


def post_install(self):
    self.install_license("LICENSE.txt")
