

def proximity_hard_join(property_df, city_df):
    return property_df.merge(city_df[['lat', 'lng','time_city']], on=['lat','lng'], how='left')


def proximity_sjoin(property_df, city_df):
    import geopandas as gpd
    from shapely import wkt
    gdf_city_coords = gpd.GeoDataFrame(city_df, geometry=gpd.points_from_xy(city_df.lng, city_df.lat))
    
    if 'geometry' in property_df.columns:
        property_df['geometry'] = property_df['geometry'].apply(wkt.loads)
        gpd_property_df = gpd.GeoDataFrame(property_df, geometry='geometry')
    else:
        gpd_property_df = gpd.GeoDataFrame(property_df, geometry=gpd.points_from_xy(property_df.lng, property_df.lat))

    # Ensure both GeoDataFrames have the same CRS (Coordinate Reference System)
    gdf_city_coords = gdf_city_coords.set_crs("EPSG:4326")
    gpd_property_df = gpd_property_df.set_crs("EPSG:4326")

    # Perform the nearest spatial join
    joined_gdf = gpd.sjoin_nearest(gpd_property_df,gdf_city_coords[['geometry','time_city']], how="left",rsuffix='city_coords')
    joined_gdf.drop(columns=['index_city_coords'],inplace=True)
    return joined_gdf