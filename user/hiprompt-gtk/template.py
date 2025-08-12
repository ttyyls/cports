pkgname = "hiprompt-gtk"
pkgver = "0.9"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["hare"]
makedepends = [
    "hare",
    "hare-gi",
    "hare-adwaita",
    "hare-gtk4-layer-shell",
]
pkgdesc = "Prompter for himitsu"
license = "GPL-3.0-or-later"
url = "https://git.sr.ht/~sircmpwn/hiprompt-gtk"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "879bebb24ce66ff92ba28844efcbb39ae8bb514f745e2ea894ef7d8f72d69c15"
