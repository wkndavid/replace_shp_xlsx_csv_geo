import geopandas as gpd
from shapely.geometry import Point
import pandas as pd

# Caminho para o arquivo Excel (.xls) local
caminho_excel = '/home/david/autom/replace_shp_xlsx_csv_geo/files/excel_example_file.xlsx'

# Lê dados do Excel para um DataFrame do pandas
dados_excel = pd.read_excel(caminho_excel)

print(dados_excel)

# Adiciona uma geometria de ponto fictícia
geometry = [Point(0, 0) for _ in range(len(dados_excel))]
gdf = gpd.GeoDataFrame(dados_excel, geometry=geometry, crs='EPSG:4326')

# Caminho para salvar o shapefile localmente (com a extensão .shp)
caminho_shapefile = '/home/david/autom/replace_shp_xlsx_csv_geo/files/generate_shapefile/archive_shapefile.shp'

# Salva o GeoDataFrame como shapefile usando o GeoPandas
gdf.to_file(caminho_shapefile, driver='ESRI Shapefile', encoding='utf-8')

# Reabre o arquivo e trata de novo
gdf = gpd.read_file(caminho_shapefile, encoding='utf-8')

# Salva novamente para garantir a correta codificação no arquivo DBF
gdf.to_file(caminho_shapefile, driver='ESRI Shapefile')