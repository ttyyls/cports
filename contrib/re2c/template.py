pkgname = "re2c"
pkgver = "3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "bison",
    "gm4",
    "gmake",
    "python",
]
pkgdesc = "Lexer generator for C, C++, Go and Rust"
maintainer = "ttyyls <contact@behri.org>"
license = "custom:none"
url = "https://re2c.org"
source = f"https://github.com/skvadrik/re2c/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "087c44de0400fb15caafde09fd72edc7381e688a35ef505ee65e0e3d2fac688b"
