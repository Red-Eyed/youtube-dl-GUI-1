#!/user/bin/env python3

import os
import sys
from pathlib import Path
from subprocess import call

import UI


def generate_resources():
    ui_root = Path(UI.__file__).parent
    generated_root = ui_root

    out_path = generated_root / "resource_rc.py"
    in_path = ui_root / "resources/resource.qrc"

    call(f"{sys.executable} -m PyQt5.pyrcc_main -o {out_path} {in_path}".split(),
         env=os.environ)

    for ui in (ui_root / "resources").glob("*.ui"):
        generated = str(generated_root / ui.stem) + ".py"
        call([f"{sys.executable}", "-m", "PyQt5.uic.pyuic", str(ui), "-o", generated])


if __name__ == '__main__':
    generate_resources()
