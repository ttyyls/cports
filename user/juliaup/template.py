pkgname = "juliaup"
pkgver = "1.17.21"
pkgrel = 0
archs = ["aarch64", "x86", "x86_64"]
build_style = "cargo"
make_build_args = [
    "--bins",
    "--features=binjuliainstaller,binjulialauncher",
]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Julia installer and version multiplexer"
license = "MIT"
url = "https://github.com/JuliaLang/juliaup"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9f9924f171f9dbc05b42cb8963f1f25211798c61ff1eab63b0ff2d23ae487dc7"


def init_configure(self):
    self.make_build_env = {
        "TARGET": f"{self.profile().arch}-unknown-linux-musl",
        "OUT_DIR": f"{self.chroot_cwd}",
        "CARGO_MANIFEST_DIR": f"{self.chroot_cwd}",
    }


def post_install(self):
    self.install_license("LICENSE")
