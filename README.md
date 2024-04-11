# LeapAPI

Leap Motion Controller API for Python 3 versions (currently 3.8, 3.9, 3.10, and 3.11). Tested on Ubuntu 20.04.

1. Clone to home folder `cd ~; git clone https://github.com/petrvancjr/LeapAPI.git`
2. Choose version `cd ~/LeapAPI/Python3.<YOUR VERSION>`
3. Install: `pip install .`
4. Export (single session) `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/LeapAPI/Leap3.<YOUR VERSION>/`
	- Automatic export: `echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:~/LeapAPI/Leap3.<YOUR VERSION>/" >> ~/.bashrc`
5. Usage: `import Leap`

## Note:

If some Leap Motion versions were installed, they needs to be uninstalled.

