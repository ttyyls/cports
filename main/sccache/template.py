pkgname = "sccache"
pkgver = "0.7.7"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=dist-client,redis,s3,memcached",
]
hostmakedepends = ["cargo"]
makedepends = ["rust-std", "openssl-devel"]
pkgdesc = "Distributed shared compilation cache"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/mozilla/sccache"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a5f5dacbc8232d566239fa023ce5fbc803ad56af2910fa1558b6e08e68e067e0"
