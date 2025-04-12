pkgname = "crowdsec"
pkgver = "1.6.8"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Crowdsourced protection against malicious IPs"
license = "MIT"
url = "https://crowdsec.net"
source = f"https://github.com/crowdsecurity/crowdsec/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f0e381449f4aa86b9af1fd1024bc427da35104dfdb230c37bf4d471d3bbf0fdb"


def post_install(self):
    self.install_license("LICENSE")
