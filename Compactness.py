import arcpy
import math
from arcpy import env

fc = arcpy.GetParameterAsText(0)

# Set local variables.
fieldName1 = "PP_Ratio"
fieldPrecision = 7
fieldScale = 2
fieldName2 = "S_Ratio"
fieldPrecision = 7
fieldScale = 2

# Execute AddField.
arcpy.AddField_management(fc, fieldName1, "FLOAT", fieldPrecision, fieldScale, "",
                          "", "NULLABLE")
arcpy.AddField_management(fc, fieldName2, "FLOAT", fieldPrecision, fieldScale, "",
                          "", "NULLABLE")

# Calculate the fields.
cursor = arcpy.da.UpdateCursor (fc, ["Area", "Perimeter", "PP_Ratio"])
for row in cursor:
    row [2] = (4*math.pi*row[0])/(row[1]**2)
    cursor.updateRow(row)
cursor = arcpy.da.UpdateCursor (fc, ["Area", "Perimeter", "S_Ratio"])
for row in cursor:
    row [2] = (math.sqrt(row[0]*4*math.pi))/row[1]
    cursor.updateRow(row)
