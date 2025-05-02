pkgname = "memcached"
pkgver = "1.6.38"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-seccomp", "--enable-tls"]
configure_gen = []
make_dir = "."
make_check_target = "test"
makedepends = [
    "libevent-devel",
    "libsasl-devel",
    "libseccomp-devel",
    "linux-headers",
    "openssl3-devel",
]
checkdepends = [
    "ca-certificates",
    "perl",
    "perl-io-socket-ssl",
]
pkgdesc = "Distributed memory object caching system"
license = "BSD-3-Clause"
url = "https://memcached.org"
source = f"{url}/files/memcached-{pkgver}.tar.gz"
sha256 = "334d792294e37738796b5b03375c47bb6db283b1152e2ea4ccb720152dd17c66"


def post_install(self):
    self.install_license("COPYING")
    self.install_bin("scripts/memcached-tool")
    self.install_man("scripts/memcached-tool.1")
