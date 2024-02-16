import geopandas as gpd
import os
#  Fiona (usado pelo GeoPandas para lidar com dados espaciais) não consegue abrir o shapefile porque o arquivo .shx pode está ausente. Configurar a opção SHAPE_RESTORE_SHX para YES para restaurá-lo ou criá-lo.
os.environ['SHAPE_RESTORE_SHX'] = 'YES'

# Caminho para o shapefile (.shp) local
caminho_shapefile = '/home/david/autom/replace_shp_xlsx_csv_geo/files/exemplo2_p.shp'

# Lê o shapefile para um GeoDataFrame ajustando a codificação
try:
    gdf = gpd.read_file(caminho_shapefile, encoding='utf-8')
except UnicodeDecodeError:
    try:
        gdf = gpd.read_file(caminho_shapefile, encoding='utf-16')
    except UnicodeDecodeError:
        gdf = gpd.read_file(caminho_shapefile, encoding='latin-1')

# Caminho para salvar o arquivo Excel localmente (com a extensão .xlsx)
caminho_excel = '/home/david/autom/replace_shp_xlsx_csv_geo/files/exemplo_shp_to1.xlsx'

# Remove a coluna de geometria temporariamente para evitar erros
gdf_temp = gdf.copy()
del gdf_temp['geometry']

# Salva o GeoDataFrame como um arquivo Excel usando o Pandas
gdf_temp.to_excel(caminho_excel, index=False, engine='openpyxl')
