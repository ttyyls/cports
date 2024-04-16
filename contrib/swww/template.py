pkgname = "swww"
pkgver = "0.9.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf", "scdoc"]
makedepends = ["lz4-devel", "rust-std"]
pkgdesc = "Solution to your Wayland Wallpaper Woes"
maintainer = "Nova <froggo8311@proton.me>"
license = "GPL-3.0-only"
url = "https://github.com/LGFae/swww"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b190f9fa63ca9952e12c8b3982862a75f714af5546e1c5e34adc17f9764b1bf4"


def post_build(self):
    self.do("./doc/gen.sh")


def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/swww")
    self.install_bin(f"target/{self.profile().triplet}/release/swww-daemon")
    self.install_man("doc/generated/*", glob=True)
    with self.pushd("completions"):
        self.install_completion("swww.bash", "bash")
        self.install_completion("_swww", "zsh")
        self.install_completion("swww.fish", "fish")
