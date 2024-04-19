pkgname = "ifupdown-ng"
pkgver = "0.12.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "scdoc"]
checkdepends = ["atf-devel", "kyua"]
pkgdesc = "Flexible ifup/ifdown implementation"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://github.com/ifupdown-ng/ifupdown-ng"
source = f"{url}/archive/refs/tags/{pkgname}-{pkgver}.tar.gz"
sha256 = "d42c8c18222efbce0087b92a14ea206de4e865d5c9dde6c0864dcbb2b45f2d85"
env = {
    "EXECUTOR_SCRIPTS_OPT": [
        "ppp",
        "wireguard",
        "wireguard-quick",
        "ethtool",
        "wifi",
    ]
}
hardening = ["vis", "cfi"]
# unpackaged dependencies
options = ["!check"]


def post_build(self):
    self.do("gmake", "docs")


def post_install(self):
    self.install_license("COPYING")
    self.do("gmake", "install_docs")


@subpackage("ifupdown-ng-iproute2")
def _iproute2(self):
    self.depends = [f"{pkgname}={pkgver}-{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-{pkgrel}", "iproute2"]
    self.pkgdesc = "ifupdown integration for iproute2"
    return ["usr/libexec/ifupdown-ng/iproute2"]


@subpackage("ifupdown-ng-ppp")
def _ppp(self):
    self.depends = [f"{pkgname}={pkgver}-{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-{pkgrel}", "ppp"]
    self.pkgdesc = "ifupdown integration for ppp"
    return ["usr/libexec/ifupdown-ng/ppp"]


@subpackage("ifupdown-ng-wireguard")
def _wireguard(self):
    self.depends = [f"{pkgname}={pkgver}-{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-{pkgrel}", "wireguard-tools"]
    self.pkgdesc = "ifupdown integration for wireguard"
    return ["usr/libexec/ifupdown-ng/wireguard"]


@subpackage("ifupdown-ng-wireguard-quick")
def _wgquick(self):
    self.depends = [f"{pkgname}={pkgver}-{pkgrel}"]
    self.install_if = [
        f".{pkgname}={pkgver}-{pkgrel}",
        "wireguard-tools-wg-quick",
    ]
    self.pkgdesc = "ifupdown integration for wireguard-tools-wg-quick"
    return ["usr/libexec/ifupdown-ng/wireguard-quick"]


@subpackage("ifupdown-ng-ethtool")
def _ethtool(self):
    self.depends = [f"{pkgname}={pkgver}-{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-{pkgrel}", "ethtool"]
    self.pkgdesc = "ifupdown integration for ethtool"
    return ["usr/libexec/ifupdown-ng/ethtool"]


@subpackage("ifupdown-ng-wifi")
def _wifi(self):
    self.depends = [f"{pkgname}={pkgver}-{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-{pkgrel}", "wpa_supplicant"]
    self.pkgdesc = "ifupdown integration for wpa_supplicant"
    return ["usr/libexec/ifupdown-ng/wifi"]
