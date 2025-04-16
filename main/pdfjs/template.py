pkgname = "pdfjs"
pkgver = "5.1.91"
pkgrel = 0
pkgdesc = "Platform for parsing and rendering PDFs"
license = "Apache-2.0"
url = "https://github.com/mozilla/pdf.js"
source = f"{url}/releases/download/v{pkgver}/pdfjs-{pkgver}-legacy-dist.zip"
sha256 = "2fa84bda74758873a26e4a89b6e2c8b04dba5ae601003b4cb1d57431f8e25e30"
# no tests defined
options = ["!check"]


def install(self):
    self.install_files("web", "usr/share/pdf.js")
    self.install_files("build", "usr/share/pdf.js")
