pkgname = "micro"
pkgver = "2.0.13"
pkgrel = 0
build_style = "makefile"
make_build_args = [f"VERSION={pkgver}"]
make_check_target = "test"
hostmakedepends = ["go"]
pkgdesc = "Terminal based text editor"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://micro-editor.github.io"
source = f"https://github.com/zyedidia/micro/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a96fff974ed6bd9a1dd58a33e54ff23b78783bbb3571b86d5c37d787b1e0e4be"


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def do_install(self):
    self.install_bin("micro")
    self.install_license("LICENSE")
    self.install_man("assets/packaging/micro.1")
    self.install_file(
        "assets/packaging/micro.desktop",
        "usr/share/applications",
    )
    self.install_file(
        "assets/micro-logo-mark.svg",
        "usr/share/icons/hicolor/scalable/apps",
        name="micro.svg",
    )
