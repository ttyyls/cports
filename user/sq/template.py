pkgname = "sq"
pkgver = "0.48.3"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/neilotoole/sq/cli/buildinfo.Version=v{pkgver}",
]
hostmakedepends = ["go"]
makedepends = ["icu-devel", "sqlite-devel", "libpq-devel"]
pkgdesc = "Tool to inspect, query, join, import, and export structured data"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://sq.io"
source = f"https://github.com/neilotoole/sq/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "46e75e2db83a6cbc98b07dbcfb23de03fc41b2b2cbc7de7aaee0425cef4fb9bb"
# requires network
options = ["!check"]


def post_build(self):
    with open(self.cwd / "sq.1", "w") as outf:
        self.do("build/sq", "man", stdout=outf)
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"sq.{shell}", "w") as outf:
            self.do(
                "build/sq",
                "completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("sq.1")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"sq.{shell}", shell)
