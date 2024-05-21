pkgname = "nix"
pkgver = "2.22.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_dir = "."
make_build_args = ["V=1"]
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "bash",
    "bison",
    "flex",
    "gmake",
    "gsed",
    "jq",
    "lowdown",
    "lsof",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "brotli-devel",
    "bzip2-devel",
    "gc-devel",
    "gtest-devel",
    "libarchive-devel",
    "libcurl-devel",
    "libgit2-devel",
    "libseccomp-devel",
    "libsodium-devel",
    "nlohmann-json",
    "openssl-devel",
    "rapidcheck-devel",
    "readline-devel",
    "sqlite-devel",
    "xz-devel",
]
depends = ["ca-certificates", "chimerautils-static"]
checkdepends = ["git"]
pkgdesc = "Purely functional package manager"
maintainer = "ttyyls <contact@behri.org>"
license = "LGPL-2.1-or-later"
url = "https://nixos.org"
source = f"https://github.com/NixOS/nix/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4482bc4a84c8f22af69d994362195f0f64d065cde1af76e60796baa3fc2bf5e2"
# vis: breaks internal linking, probably fixable?
# int: breaks nix parser
hardening = ["!int", "!vis"]
# lol
options = ["!check"]
exec_wrappers = [("/usr/bin/gsed", "sed")]
system_groups = ["nixbld"]


def do_configure(self):
    self.do("autoreconf", "-if")
    self.do(
        "bash",
        "./configure",
        "--prefix=/usr",
        "--sysconfdir=/etc",
        "--sbindir=/usr/bin",
        "--bindir=/usr/bin",
        "--libdir=/usr/lib",
        "--mandir=/usr/share/man",
        "--infodir=/usr/share/info",
        "--localstatedir=/nix/var",
        "--with-readline-flavor=readline",
        "--with-sandbox-shell=/usr/bin/sh.static",
        "--enable-gc",
        "--disable-cpuid",
        "--disable-external-api-docs",
    )


def post_check(self):
    self.do("gmake", "installcheck")


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_service(self.files_path / "nix")
    self.install_file(self.files_path / "nix.conf", "etc/nix")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="nix.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="nix.conf",
    )
