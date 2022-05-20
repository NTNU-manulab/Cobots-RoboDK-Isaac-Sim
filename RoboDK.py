# Copyright 2017 - RoboDK Inc. - https://robodk.com/
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ----------------------------------------------------
# This project is the compiled version of the RoboDK Add-In for Autodesk Fusion 360
# Follow these steps to load the plugin:
#   1- Make sure to install/update RoboDK:
#      https://robodk.com/download
#   2- Unzip the contents of this folder in:
#      C:/RoboDK/Other/Plugin-Fusion360/RoboDK/  
#      (Mac) -> /home/username/RoboDK/Other/Plugin-Fusion360/RoboDK/   
#   3- Open Autodesk Fusion 360
#   4- Select Add-Ins->Scripts and Add-Ins   (in the Model section)
#   5- Select Add-Ins tab
#   6- Select the green "+" button right beside My Add-Ins
#   7- Provide the foder:
#      C:/RoboDK/Other/Plugin-Fusion360/RoboDK/ 
#   8- Select Run
#
# More information about the RoboDK Add-In for Autodesk Fusion 360:
#   https://robodk.com/doc/en/Plugin-Fusion360.html 
#
# More information about the RoboDK API:
#   Documentation: https://robodk.com/doc/en/RoboDK-API.html
#   Reference:     https://robodk.com/doc/en/PythonAPI/index.html
#   GitHub:        https://github.com/RoboDK/RoboDK-API/
#
#------------------------------------------------------

import sys
import os



print("Using Python version: " + str(sys.version_info))
PATH_ABS_FILE = os.path.dirname(__file__).replace("\\","/")
print("RoboDK Plug-in Path: " + PATH_ABS_FILE)


if sys.version_info[:2] == (3, 7):
    # Latest Python 3.7.3 since September 2019
    sys.path.insert(0, PATH_ABS_FILE + '/v373')
    
elif sys.version_info[:2] == (3, 5):
    # Python 3.5.3 before September 2019
    sys.path.insert(0, PATH_ABS_FILE + '/v353')
    
else:
    raise Exception("Using a non compatible Python version: " + str(sys.version_info))
    
from robodk_autodesk import *

def run_custom(context):
    ui = getUI()
    try:
        # Auto setup command
        _register_command(Cmd_AutoSetup())
    
        # Command to load the 3D model
        _register_command(Cmd_LoadPart())

        # Command to load curves
        _register_command(Cmd_LoadCurves())

        # Command to load points
        _register_command(Cmd_LoadPoints())
        
        # General settings:
        _register_command(RoboDk())
        
        # Command to load CAM file (NC)
        _register_command(Cmd_LoadCAM())
        
        # Command to post all programs
        _register_command(Cmd_GenerateProg())
 
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

if __name__== "__main__":
    run()