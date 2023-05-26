Requirements:

Python 3.8 or higher
Java 11
Graphviz
GW2UPPAAL - https://github.com/iyerkumar/GW2UPPAAL
Run the following commands to support graphviz
- pip install graphviz
- pip install jsondiff

Also, after downloading graphviz, add the bin and dot.exe to the path.
Example - path/to/graphviz/bin and path/to/graphviz/bin/dot.exe
Instructions:

1. A blank output folder is provided to load the graphviz images. The same folder can be used to export the GW model
2. Open CMD or Terminal in the current directory.
3. Usee the command: java -jar Uppaal2GW.jar [Initial GW Model File Path] [Initial JSON Model File Name] [UPPAAL Model File Path] [UPPAAL XML Model File Name] [Output Folder Path] [Output JSON File Name]

Note that the Initial GW file path and name are required for Graphviz.

For example:
java -jar Uppaal2GW.jar F://SE//inputModels MessengerModel.json F://SE//GW2UPPAAL-main//ToolOutput Messanger2.xml F://SE//UPPAAL2GW//Outputs MessengerNew.json

Do note that the XML file in the above example is directly taken from GW2UPPAAL's ToolOutput folder.
