"""
Tool:               getCMOC
Source Name:        getCMOC
Version:            Made on arcGIS pro 2.8
Author:             Ferdinand Dorado
Usage:              Import and run script in arcGIS pro 
Description:        Gets the CMOC (Community Maps of Canada) from arcGIS Online and crops it to the province of British Columbia
"""
import arcpy
from arcgis.gis import GIS
from datetime import datetime

# ===============================================
# Global variables
# ===============================================

# Download path of tiles 
# Default = current project directory
dlPath = "."
# Query to search in arcGIS Online
q = "CMOCOffline_VTPK"
# gets the vector tiles of CMOC from arcGIS online
def getTiles():
    logMsg("Running GIS...")
    gis = GIS(set_active=True)
    logMsg("Finished GIS")

    logMsg("Searching for CMOC...")
    searchList = gis.content.search(query=q)
    item = searchList[0] # First Item In list (Should be the Offline TilePackage)
    cmocID = item.id
    logMsg("Found item: " + item.title)
    logMsg("Item id: " + cmocID)

    # ===============================
    # Note: April 2022
    # Download by ID method will not work because esri canada 
    # changes the ID when the update the dataset
    # ===============================
    # CMOC link:
    # https://www.arcgis.com/home/item.html?id=017dbc36031b40078927d85872936942
    # cmoc = gis.content.get("017dbc36031b40078927d85872936942")

    # Test data:
    # Interpreted Habitat Types Predicted from Multibeam Data Vector Package
    # https://www.arcgis.com/home/item.html?id=7a73185ea1464c7f8474d80bf5d90bf8
    # cmoc = gis.content.get("7a73185ea1464c7f8474d80bf5d90bf8")

    cmoc = gis.content.get(cmocID)
    now = datetime.now()
    dlTime = now.strftime("%m/%d/%Y, %H:%M:%S")
    logMsg("Downloading CMOC... " + dlTime)
    logMsg("Will take approx: 5-7 mins (Depending on internet speed)")
    # ===============================================
    # Downloads item to project directory
    # ===============================================
    # cmoc.download(dlPath)
    # ===============================================
    # Downloads item to project directory + date downloaded
    # ===============================================
    dlTime = now.strftime("%m-%d-%Y")
    cmoc.download(dlPath + dlTime)
    logMsg("Downloaded to: "+ dlPath + dlTime)
    logMsg("Done downloading")
    
    return

# Runs the script
def run():
    """runs the script"""
    getTiles()
    return
# prints string s to arcpy and console
def logMsg(s):
    arcpy.AddMessage(s)
    print(s)
    return

if __name__ == '__main__':
    
    run()

