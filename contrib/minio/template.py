pkgname = "minio"
pkgver = "2024.08.03"
_timestamp = "04-33-23"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags",
    f"-X github.com/minio/mc/cmd.Version={pkgver.replace('.', '-')}T{_timestamp}"
    f" -X github.com/minio/mc/cmd.ReleaseTag=RELEASE.{pkgver.replace('.', '-')}Z",
]
hostmakedepends = ["go"]
go_build_tags = ["kqueue"]
go_check_tags = ["kqueue", "dev"]
pkgdesc = "S3 compatible object storage server"
maintainer = "ttyyls <contact@behri.org>"
license = "AGPL-3.0-or-later"
url = "https://min.io"
source = f"https://github.com/minio/minio/archive/refs/tags/RELEASE.{pkgver.replace('.', '-')}T{_timestamp}Z.tar.gz"
sha256 = "b0223962d0d46fd0a98ec7c08faaa2b89a1947bf4fd8ce7ed1792dcdf82f6098"
# some tests require internet access
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
