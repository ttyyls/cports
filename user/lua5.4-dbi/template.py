pkgname = "lua5.4-dbi"
pkgver = "0.7.5"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "psql",
    "sqlite3",
]
make_install_target = "install_lua"
make_install_args = [
    "install_psql",
    "install_sqlite3",
]
hostmakedepends = ["lua5.4"]
makedepends = [
    "lua5.4-devel",
    "postgresql16-client-devel",
    "sqlite-devel",
]
pkgdesc = "Multi-backend SQL database library for Lua"
license = "MIT"
url = "https://github.com/mwild1/luadbi"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d11990029946cf29ee33cdb563900ba8e105207c507b08887896e88e429d8429"
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
