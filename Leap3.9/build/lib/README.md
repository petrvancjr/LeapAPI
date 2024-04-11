Leap Motion Controller SDK setup for Python 3.9.

Install with `pip install .`
Export `LD_PRELOAD=<absolute path to current dir>/libLeap.so`
Use with: `import Leap`

If some Leap Motion versions were installed, they needs to be uninstalled.
If you're unable to do that, use: `leap_motion_python.tar`.

Then use with: `from leapmotionpython import Leap`, NOT `import Leap`! 


