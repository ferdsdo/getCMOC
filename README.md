# getCMOC
Python Script for AcrGIS Pro to download the CMOC vector tile package from AcrGIS Online

## Usage

Import the script into ArcGIS Pro
Run the script in the geoprocessing tools

Note:
* The default download location will be where your ArcGIS pro project is located. You can change this by changing the 'dlPath' value to any relative or absolute path you want. 
* When the file downloads it will save it in a folder with the name of the current date and time you ran the script.
* You can also change what item to download by changing the 'q' value on line 21. Note that it will download the first item that shows up in the query.
