pkgname = "0ad"
pkgver = "0.27.0"
pkgrel = 0
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "ninja",
    "python",
]
makedepends = [
    "boost-devel",
    "curl-devel",
    "enet-devel",
    "fmt-devel",
    "icu-devel",
    "libogg-devel",
    "libpng-devel",
    "libsodium-devel",
    "libvorbis-devel",
    "libxml2-devel",
    "miniupnpc-devel",
    "openal-soft-devel",
    "rust-std",
    "sdl2-devel",
    "wxwidgets-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Game of ancient warfare"
license = "GPL-2.0-only AND CC-BY-SA-3.0"
url = "https://play0ad.com"
source = [
    f"https://releases.wildfiregames.com/0ad-{pkgver}-unix-build.tar.xz",
    f"https://releases.wildfiregames.com/0ad-{pkgver}-unix-data.tar.xz",
]
source_paths = [".", "."]
sha256 = [
    "aa94857009750d5f61dbf016bc150e3bdcbdb3acdfc8ad20b73ab8b43e9a1ba6",
    "3e48855ab8e1ef81270338462c8270b015213f14f5e054aab92ad74d5ea59dea",
]


def init_configure(self):
    self.do(
        "./update-workspaces.sh",
        f"-j{self.make_jobs}",
        wrksrc="build/workspaces",
    )


def install(self):
    pass
