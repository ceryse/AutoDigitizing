# AutoDigitizing

This tool is designed for use in ArcGIS to convert black and white maps to vector files. 

## Description

This tool will be most useful for black and white maps with limited labels. It was originally designed to assist with the digitization of census maps in the UCLA Library Collection. At its simplest, it uses the Raster to Polygon tool, then Polygon to Centerline, and then Feature to Polygon, with a few dissolves and merges in between to simplify and clean up the data.

## Getting Started

### Installing

* Download the toolbox (.tbx file) 
* Open your ArcGIS project, and add the toolbox to your project toolboxes menu

### Executing program

* prepare raster by removing any unnecessary lettering or inset maps, and filling any dotted lines, if desired
* Upload to ArcGIS project and georeference raster if it is not already (accuracy is important!)
* Open the tool, and fill in the parameters. <b>Workspace must be a GEODATABASE</b>
* Click run

## Help

* If the map image contains dotted lines to represent boundaries you want included in the final vector file, you will either have to make them solid in Photoshop or Paint, or finish the digitizing using the edit feature in ArcGIS after running the tool
* Most map images have imperfections, so it is suggested that you look over the resulting features and use the built in ArcGIS Edit tools to reshape as needed after running the tool.

## Authors

Cerys Edwards (cerysedwards@g.ucla.edu)

## Version History

* 1 - Initial Release
