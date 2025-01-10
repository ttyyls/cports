pkgname = "mise"
pkgver = "2025.1.3"
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
sha256 = "1ff5d6c644d724689f154b220a4c89805d5aa27a01208c043c0671d12c92af58"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/mise")
    self.install_license("LICENSE")
    self.install_man("man/man1/mise.1")
