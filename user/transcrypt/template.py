pkgname = "transcrypt"
pkgver = "2.3.1"
pkgrel = 0
depends = ["bash", "git", "openssl3", "vim-xxd"]
checkdepends = [*depends, "bats"]
pkgdesc = "Transparently encrypt files within a git repository"
license = "MIT"
url = "https://github.com/elasticdog/transcrypt"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c5f5af35016474ffd1f8605be1eac2e2f17743737237065657e3759c8d8d1a66"
# needs git repo
options = ["!check"]


def check(self):
    self.do("bats", "tests")


def install(self):
    self.install_bin("transcrypt")
    self.install_man("man/transcrypt.1")
    self.install_completion("contrib/bash/transcrypt", "bash")
    self.install_completion("contrib/zsh/_transcrypt", "zsh")
    self.install_license("LICENSE")
