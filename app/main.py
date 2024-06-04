import ctypes
import os
import shutil
import subprocess
import sys

from tempfile import mkdtemp


def main():
    command = sys.argv[3]
    args = sys.argv[4:]

    temp_dir = mkdtemp()
    libc = ctypes.cdll.LoadLibrary("libc.so.6")
    libc.unshare(0x20000000)

    shutil.copy(command, temp_dir)
    os.chroot(temp_dir)
    command = os.path.join("/", os.path.basename(command))

    completed_process = subprocess.run([command, *args], capture_output=True)
    sys.stderr.write(completed_process.stderr.decode("utf-8"))
    sys.stdout.write(completed_process.stdout.decode("utf-8"))
    sys.exit(completed_process.returncode)


if __name__ == "__main__":
    main()
