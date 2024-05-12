pkgname = "certbot"
pkgver = "2.10.0"
pkgrel = 2
build_wrksrc = "certbot"
build_style = "python_pep517"
_plugins = [
    "certbot-apache",
    "certbot-dns-cloudflare",
    "certbot-dns-digitalocean",
    "certbot-dns-dnsimple",
    "certbot-dns-dnsmadeeasy",
    "certbot-dns-gehirn",
    "certbot-dns-google",
    "certbot-dns-linode",
    "certbot-dns-luadns",
    "certbot-dns-nsone",
    "certbot-dns-ovh",
    "certbot-dns-rfc2136",
    "certbot-dns-route53",
    "certbot-dns-sakuracloud",
    "certbot-nginx",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-acme",
    "python-configargparse",
    "python-configobj",
    "python-cryptography",
    "python-distro",
    "python-josepy",
    "python-parsedatetime",
]
checkdepends = [
    "python-pytest",
] + depends
pkgdesc = "Tool to obtain certs from Let's Encrypt"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0 AND MIT"
url = "https://github.com/certbot/certbot"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7e277bb461cae4071e22641e076d9232ae00ffda05bdb02832cbc1f862afab2d"


def post_build(self):
    for plugin in _plugins:
        self.do(
            "python",
            "-m",
            "build",
            "--wheel",
            "--no-isolation",
            f"../{plugin}",
        )


def post_install(self):
    for plugin in _plugins:
        self.do(
            "python",
            "-m",
            "installer",
            "--compile-bytecode",
            "0",
            "--destdir",
            self.chroot_destdir,
            f"../{plugin}/dist/{plugin.replace('-','_')}-{pkgver}-py3-none-any.whl",
        )
    self.install_license("LICENSE.txt")


@subpackage("certbot-plugins")
def _pluggie(self):
    self.pkgdesc = "certbot plugins meta package"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.options = ["empty"]

    return []


def _genmod(pname, pdesc):
    @subpackage(f"certbot-{pname}")
    def _plug(self):
        self.pkgdesc = f"{pdesc} plugin for certbot"
        self.install_if = [
            f"{pkgname}={pkgver}-r{pkgrel}",
            f"certbot-plugins={pkgver}-r{pkgrel}",
        ]
        self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
        match pname:
            case "dns-cloudflare":
                self.depends += ["python-cloudflare"]

        return [
            f"usr/lib/python*/site-packages/certbot_{pname.replace('-', '_')}*"
        ]


for _plugin, _desc in [
    ("apache", "Apache"),
    ("dns-cloudflare", "Cloudflare dns authenticator"),
    ("dns-digitalocean", "Digitalocean dns authenticator"),
    ("dns-dnsimple", "DNSimple dns authenticator"),
    ("dns-dnsmadeeasy", "DNS made easy dns authenticator"),
    ("dns-gehirn", "Gehirn infrastructure service dns authenticator"),
    ("dns-google", "Google cloud dns authenticator"),
    ("dns-linode", "Linode dns authenticator"),
    ("dns-luadns", "Luadns authenticator"),
    ("dns-nsone", "NS1 dns authenticator"),
    ("dns-ovh", "OVH dns authenticator"),
    ("dns-rfc2136", "RFC 2136 dns authenticator"),
    ("dns-route53", "Amazon web services route 53 dns authenticator"),
    ("dns-sakuracloud", "Sakura cloud dns authenticator"),
    ("nginx", "Nginx"),
]:
    _genmod(_plugin, _desc)
