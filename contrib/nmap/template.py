pkgname = "nmap"
pkgver = "7.95"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-liblua=/usr/lua5.4",
    "--with-libpcap=yes",
    "--with-libpcre=yes",
    "--with-libssh2=yes",
    "--with-libz=yes",
    "--with-openssl=yes",
    "--with-zenmap=no",
]
configure_gen = []
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["automake", "gmake", "pkgconf", "python"]
makedepends = [
    "libpcap-devel",
    "libidn2-devel",
    "libssh2-devel",
    "linux-headers",
    "lua5.4-devel",
    "openssl-devel",
    "pcre2-devel",
    "zlib-devel",
]
pkgdesc = "Network discovery and security auditing"
maintainer = "ttyyls <contact@behri.org>"
license = "custom:nmap"
url = "https://nmap.org"
source = f"https://nmap.org/dist/nmap-{pkgver}.tgz"
sha256 = "015edd0091e5b017a891479ff276ca38fd50a98f7a87ea2c20664c2c5e384330"
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("nmap-devel")
def _devel(self):
    return self.default_devel()
