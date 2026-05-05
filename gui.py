import os
import sys
from ffsubsync import ffsubsync
from gooey import Gooey

# Crucial for AppImage: Include bundled FFmpeg in the path
if "APPDIR" in os.environ:
    os.environ["PATH"] = os.path.join(os.environ["APPDIR"], "usr", "bin") + os.path.pathsep + os.environ["PATH"]

@Gooey(program_name="FFsubsync GUI", default_size=(600, 720))
def main():
    # Direct call to the existing ffsubsync logic
    sys.argv[0] = 'ffsubsync'
    ffsubsync.main()

if __name__ == '__main__':
    main()
