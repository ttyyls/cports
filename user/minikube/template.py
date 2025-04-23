pkgname = "minikube"
pkgver = "1.35.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X k8s.io/minikube/pkg/version.version={pkgver}",
    "./cmd/minikube",
    "./cmd/drivers/kvm",
]
hostmakedepends = ["go", "pkgconf"]
makedepends = ["libvirt-devel"]
pkgdesc = "Kubernetes cluster tool"
license = "Apache-2.0"
url = "https://minikube.sigs.k8s.io/docs"
source = (
    f"https://github.com/kubernetes/minikube/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "6e19aa1441a3bcf6d3ba3d71df0515f23d3fd2c6f6fbf9f1438c746675e652e1"
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"minikube.{shell}", "w") as outf:
            self.do(
                "./build/minikube",
                "completion",
                shell,
                stdout=outf,
            )


def check(self):
    self.do("make", "check", env={"TESTSUITE": ["unittest"]})


def install(self):
    self.install_bin("build/minikube")
    self.install_bin("build/kvm", name="docker-machine-driver-kvm2")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"minikube.{shell}", shell)
