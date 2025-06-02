pkgname = "uxn"
pkgver = "1.0"
pkgrel = 0
hostmakedepends = ["plan9port"]
makedepends = ["sdl2-devel"]
pkgdesc = "Assembler and emulator for the Uxn stack-machine"
license = "MIT"
url = "https://100r.co/site/uxn.html"
source = f"https://git.sr.ht/~rabbits/uxn/archive/{pkgver}.tar.gz"
sha256 = "29059ee288474e48fae4b9e755bbc8e1b392a9c7ac90449d7a6599385c145460"


def build(self):
    self.do("./build.sh")


def install(self):
    self.install_license("LICENSE")


# @subpackage("uxn-cli")
# def _(self):
#     return ["cmd:uxn-cli"]
