pkgname = "ponyc"
pkgver = "0.58.2"
pkgrel = 0
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "cmake"
configure_args = [
    f"-DPONYC_VERSION={pkgver}",
    "-DPONY_USE_LTO=ON",
    "-DPONY_USE_THREAD_SANITIZER=ON",
    "-DPONY_USE_ADDRESS_SANITIZER=ON",
    "-DPONY_USE_UNDEFINED_BEHAVIOR_SANITIZER=ON",
]
hostmakedepends = ["cmake", "clang-tools-extra", "ninja"]
makedepends = [
    "benchmark-devel",
    "bzip2-devel",
    "gtest-devel",
    "libarchive-devel",
    "libcurl-devel",
    "libedit-devel",
    "libexpat-devel",
    "libffi-devel",
    "libuv-devel",
    "llvm-devel",
    "ncurses-devel",
    "nghttp2-devel",
    "rhash-devel",
    "xxhash-devel",
    "xz-devel",
    "zstd-devel",
]
pkgdesc = "Pony programming language compiler"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-2-Clause"
url = "https://www.ponylang.io"
source = f"https://github.com/ponylang/ponyc/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "fcba41f9794f013e001c25a2ee4600a8398e64d9c5757f09027809443ae25181"
# plenty of weird conversions in the codegen code
hardening = ["!int"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("pony-std")
def _std(self):
    return self.default_libs()
