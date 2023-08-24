# GBCamera-Border-Eliminator
This eliminates the "Gameboy Camera" border from Gameboy camera pictures. 

This eliminates the border, Nintendo logo, and Gameboy logo surrounding the initial exported images from the Gameboy camera. For now it only supports the 1x output from the Gameboy Camera Emulator exports via the RetroSpy Tech Pixel Viewer. 2x, 3x, and 4x support are to follow. Only 480 width by 432 height ".png" images are currently supported, which is the 1x export size.

The Python "Pillow" library (PIL fork) must be installed. In Windows, run the Windows Command Processor by typing "cmd" or "cmd.exe" in the "Search programs and files" bar and pressing "Enter" or "↵" after clicking on the Windows Start Menu. Type "python3 -m pip install Pillow" and press enter. This will install Pillow. Sorry, but right now this will not run on Linux or Mac do to needing the "C:\GBCam" folder.

Create a folder on the "C:" drive called "GBCam". It should look like "C:\GBCam". Place "GBCamBorderEliminator.py" in this folder. Place all the unprocessed images in this folder. 

When "GBCamBorderEliminator.py" is run, it will output the processed images to the "C:\GBCam" folder with "GBCam_" at the beginning of the original filename. So if the images you are working with are named "marblehornetsdelstill.png" and "POLYBIUS_dogbone.png", the respective outputs will be "GBCam_marblehornetsdelstill.png" and "GBCam_POLYBIUS_dogbone.png". The original files will not be deleted.

If you don't have anything to run Python code, I recommend Microsoft Visual Studio for the "in-depth" types, Mu for simplicity if you just want to run the code, or Jupyter Notebook if you like running different cells for certain reasons that require running different cells. Those installs are beyond the scope of this ReadMe and now I'm just rambling.

I'm brand new to programming so I might not be able to offer much support, but I can recommend drinking more water. 
