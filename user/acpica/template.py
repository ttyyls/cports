pkgname = "acpica"
pkgver = "20241212"
pkgrel = 0
build_style = "makefile"
make_dir = "."
make_build_args = [
    "NOWERROR=TRUE",
    "NOFORTIFY=TRUE",
]
hostmakedepends = ["bison", "flex"]
pkgdesc = "ACPI Component Architecture"
license = "GPL-2.0-or-later"
url = "https://www.acpica.org"
source = f"https://downloadmirror.intel.com/843320/acpica-unix-{pkgver}.tar.gz"
sha256 = "9dca83cfee390b710485fbdf787048370049c05723b10cc220cfef6e13c31961"
# no tests
options = ["!check"]


def install(self):
    pass
