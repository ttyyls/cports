pkgname = "mise"
pkgver = "2024.12.17"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=native-tls,rustls-native-roots",
]
make_check_args = [
    *make_build_args,
    "--",
    "--skip=toolset::tool_version_list::tests::test_tool_version_list",
]
hostmakedepends = [
    "cargo",
    "pkgconf",
]
makedepends = [
    "libgit2-devel",
    "lua5.1-devel",
    "openssl-devel",
    "rust-std",
    "zstd-devel",
]
checkdepends = ["bash"]
pkgdesc = "Development environment setup tool"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://mise.jdx.dev"
source = f"https://github.com/jdx/mise/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8f29224ab72073d1da8d3c1527fe2c735d1b9f61a83e866d5af40d2327628543"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/mise")
    self.install_license("LICENSE")
    self.install_man("man/man1/mise.1")
