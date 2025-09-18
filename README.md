# LeapAPI

Leap Motion Controller API for Python 3 versions (currently 3.8, 3.9, 3.10, and 3.11). Tested on Ubuntu 20.04/22.04/24.04.

1. Clone to home folder `cd ~; git clone https://github.com/petrvancjr/LeapAPI.git`
2. Choose version `cd ~/LeapAPI/Leap.<YOUR VERSION>`
3. Install: `pip install .`
4. Export (single session) `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/LeapAPI/Leap3.<YOUR VERSION>/`
	- Automatic export: `echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:~/LeapAPI/Leap3.<YOUR VERSION>/" >> ~/.bashrc`
5. Usage: `import Leap`

## Note:

If some Leap Motion versions were installed, they needs to be uninstalled.

## Update: LeapSDK Installation Bug (Ubuntu24.04)

Installing LeapSDK on Ubuntu24.04 might result in missing package `libgl1-mesa-glx`, this package doesn't exists, is deprecated, and not needed. Bypass it by creating fake deb package:

```
sudo apt install equivs
equivs-build libgl1-mesa-glx-fake
sudo apt -f install
sudo dpkg -i ./libgl1-mesa-glx-fake_*.deb
sudo dpkg --configure -a
sudo dpkg --install Leap-version-x64.deb
```