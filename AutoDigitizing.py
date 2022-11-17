###############################################################################
# Author: Cerys Edwards
# 16 November 2022
# This tool allows the user to convert a black and white raster image of a 
# map into a polygon vector file.
###############################################################################

# Setup
import arcpy
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
path = arcpy.GetParameterAsText(3) + "\\"
input1 = arcpy.GetParameterAsText(0)
desc = arcpy.Describe(input1)
rasterInput = desc.catalogPath + "/" + input1
output = arcpy.GetParameterAsText(1)
coord_sys = arcpy.GetParameterAsText(2)
arcpy.management.DefineProjection(input1, coord_sys)

# Reclassify raster
band1 = arcpy.Raster(rasterInput + "/Band_1")
remap = RemapRange([[0, 200, 1], [200, 255, "NODATA"]])
raster = Reclassify(band1, "Value", remap)

# raster to polygon
polygon1 = "polygon1.shp"
arcpy.conversion.RasterToPolygon(raster, polygon1)

# merge
polygon2 = "polygon2.shp"
arcpy.management.Merge(polygon1, polygon2)

# removes all except the largest part of the feature layer
# to do:
    # find a more efficient way to do this while preserving other larger parts
maximum = 0
with arcpy.da.UpdateCursor(polygon2, ['SHAPE@AREA']) as rows:
    for row in rows:
        if (row[0] > maximum):
            maximum = row[0]
    rows.reset()
    for row2 in rows:
        if (row2[0] < maximum):
            rows.deleteRow()
            
# dissolve + clean-up
poly3 = path + "poly3"
arcpy.management.Dissolve(polygon2, poly3)
arcpy.RepairGeometry_management(poly3)
poly4 = path + "poly4"
arcpy.management.EliminatePolygonPart(in_features = poly3,
                                      out_feature_class = poly4,
                                      condition = "PERCENT",
                                      part_area_percent = .01,
                                      part_option = "ANY")

# polygon to centerline
line = path + "centerline"
arcpy.topographic.PolygonToCenterline(poly4, line)

# merge again
line2 = path + "line2"
arcpy.management.Merge(line, line2)

# feature to polygon
arcpy.management.FeatureToPolygon(line, output)

# ta-da!

# Clean-up
arcpy.management.DeleteFeatures(polygon1)
arcpy.management.DeleteFeatures(poly3)
arcpy.management.DeleteFeatures(line)
arcpy.management.DeleteFeatures(line2)
arcpy.management.DeleteFeatures(polygon2)
arcpy.management.DeleteFeatures(poly4)
del polygon1, line, raster, output, rasterInput, remap, band1, line2, polygon2
del desc, input1, row, coord_sys, poly3, poly4, path
