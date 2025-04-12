pkgname = "crowdsec-firewall-bouncer"
pkgver = "0.0.31"
pkgrel = 0
build_style = "go"
pkgdesc = "Crowdsec bouncer for firewalls"
license = "MIT"
url = "https://crowdsec.net"
source = f"https://github.com/crowdsecurity/cs-firewall-bouncer/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c34963f0680ae296ae974d8f6444a2d1e2dd7617e7b05d4ad85c320529eec5f5"


def post_install(self):
    self.install_license("LICENSE")
