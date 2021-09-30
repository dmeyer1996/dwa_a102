import geopandas as gpd

#basic function for getting the sum of area for a given GeoDataFrame with geometry Data in m²(depending on coordinate system of shapefile)
def getArea(gdf):
    map_area=gdf.area.sum()
    return(map_area)
