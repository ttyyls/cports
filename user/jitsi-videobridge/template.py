pkgname = "jitsi-videobridge"
pkgver = "2.0.10184"
pkgrel = 0
hostmakedepends = ["maven"]
makedepends = ["openjdk21"]
depends = ["virtual:java-jre!openjdk21-jre"]
pkgdesc = "WebRTC compatible video router"
license = "Apache-2.0"
url = "https://jitsi.org/jitsi-videobridge"
source = f"https://github.com/jitsi/jitsi-videobridge/archive/refs/tags/stable/jitsi-meet_{pkgver[pkgver.rfind('.') + 1 :]}.tar.gz"
sha256 = "cde860823973541cd91c0eb0ee68f6a5d43d561f52e9a4009626ae150dc1b057"
env = {
    "JAVA_HOME": "/usr/lib/jvm/java-21-openjdk",
    "PATH": "$PATH:$JAVA_HOME",
}


def prepare(self):
    self.do("mvn", "clean", "package", "install", allow_network=True)


def build(self):
    pass


def install(self):
    pass
