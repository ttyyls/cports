pkgname = "ollama"
pkgver = "0.4.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Get up and running with large language models"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://ollama.com"
source = f"https://github.com/ollama/ollama/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "61ba8942fc85b25a0f8812e9ccc6a37c9e253627975a37c05a96230aa7745f07"

def post_install(self):
    self.install_license("LICENSE")
