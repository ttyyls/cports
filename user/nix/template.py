pkgname = "nix"
pkgver = "2.24.10"
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
depends = ["ca-certificates", "oksh.static"]
checkdepends = ["git"]
pkgdesc = "Purely functional package manager"
maintainer = "ttyyls <contact@behri.org>"
license = "LGPL-2.1-or-later"
url = "https://nixos.org"
source = f"https://github.com/NixOS/nix/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6a7da2160a76aaf303b40cc7afdb8da71c04c8b05f238656e0914a032d1acce3"
# vis: breaks internal linking
# int: breaks nix parser
hardening = ["!int", "!vis"]
# rotten cleanup
options = ["!check"]
exec_wrappers = [("/usr/bin/gsed", "sed")]


def configure(self):
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
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
