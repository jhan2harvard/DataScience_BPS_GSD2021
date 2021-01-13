import rhinoscriptsyntax as rs
import Rhino
import time


#Load Grasshopper plugin as gh
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
 
## This is used to print the method names ###
for func in dir(gh):
    if not func.startswith('_'): print func
    
#SetSliderValue("GUID",Number)
rs.EnableRedraw(True)

# Set the parameters' list
Lst = []

for i in range(0,len(Lst)):
    ## your codes here....
    
    
    
    time.sleep(1)
