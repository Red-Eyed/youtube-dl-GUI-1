#!/user/bin/env python3

import os
import sys
from pathlib import Path
from subprocess import call


def generate_resources():
    root = Path(__file__).parent
    out_path = root / 'resource_rc.py'
    in_path = root / 'resources/resource.qrc'

    if not out_path.exists():
        call(f"{sys.executable} -m PyQt5.pyrcc_main -o {out_path} {in_path}".split(),
             env=os.environ)

        print(f"{root}/resources.py has been generated!")

    ui_dir = Path(__file__).parent / "resources"

    for ui in ui_dir.glob("*.ui"):
        call(["pyuic5", str(ui), "-o", ui.stem + ".py"])


if __name__ == '__main__':
    generate_resources()
