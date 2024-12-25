pkgname = "jdtls"
pkgver = "1.43.0"
pkgrel = 0
hostmakedepends = ["maven"]
depends = ["virtual:java-jre!openjdk21-jre"]
pkgdesc = "Java language server"
maintainer = "ttyyls <contact@behri.org>"
license = "EPL-2.0"
url = "https://github.com/eclipse-jdtls/eclipse.jdt.ls"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "939993bbe060f90baf53f54d69eb1c87046b3f9baf251c50fced3f48a5665e8c"
env = {"JAVA_HOME": "/usr/lib/jvm/java-21-openjdk"}


def prepare(self):
    self.do("mvn", "dependency:go-offline", allow_network=True)
    for f in self.find("", "*.(repositories|sha1)"):
        self.rm(f)


def build(self):
    self.do("mvn", "-B", "-o", "package")


def install(self):
    self.install_dir("usr/share/jdtls")
    with self.pushd("org.eclipse.jdt.ls.product/target/repository"):
        self.install_files("config_linux", "usr/share/jdtls")
        self.install_files("config_linux", "usr/share/jdtls")
        self.install_files("config_ss_linux", "usr/share/jdtls")
        self.install_files("features", "usr/share/jdtls")
        self.install_files("plugins", "usr/share/jdtls")
        self.install_files("bin", "usr/share/jdtls")
    self.install_link("usr/bin/jdtls", "../share/jdtls/bin/jdtls")
