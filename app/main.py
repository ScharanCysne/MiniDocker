import os
import subprocess
import sys

from tempfile import mkdtemp


def main():
    command = sys.argv[3]
    args = sys.argv[4:]

    temp_dir = mkdtemp()
    os.chroot(temp_dir)

    completed_process = subprocess.run([command, *args], capture_output=True)
    sys.stderr.write(completed_process.stderr.decode("utf-8"))
    sys.stdout.write(completed_process.stdout.decode("utf-8"))
    sys.exit(completed_process.returncode)


if __name__ == "__main__":
    main()
