# the earliest cached bytecode

import os
import sys


def fire():
    # we need structural pattern matching in templates and cbuild itself
    if sys.version_info < (3, 12):
        sys.exit("Python 3.12 or newer is required")

    # running as root interferes with the sandbox functionality
    if os.geteuid() == 0:
        sys.exit("Please don't run cbuild as root")

    from . import runner

    # early init will set up workdir and so on
    runner.init_early()

    # depends on early init, and late init depends on this
    runner.handle_options()

    # early initialization will set up paths and other
    # stuff needed to import the rest of cbuild correctly
    runner.init_late()

    runner.fire()
