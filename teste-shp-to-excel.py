import geopandas as gpd

# Caminho para o shapefile (.shp) local
# Execute em algum => Terminal / Linha de comando / Shell => o comando 'pwd' (nome do diretório do arquivo exemplo do retorno => /home/david/autom/setor/setor.shp ou C:\Users\Documents\arquivo.shp => para achar o caminho do arquivo na estrutura de pastas...

caminho_shapefile = '/home/david/autom/setor/setor.shp'

# Ler o shapefile para um GeoDataFrame ajustando a codificação
try:
    gdf = gpd.read_file(caminho_shapefile)
except UnicodeDecodeError:
    try:
        gdf = gpd.read_file(caminho_shapefile)
    except UnicodeDecodeError:
        gdf = gpd.read_file(caminho_shapefile)

# Caminho para salvar o arquivo Excel localmente (com a extensão .xlsx)
caminho_excel = '/home/david/autom/setor/teste.xlsx'

# Salva o GeoDataFrame como um arquivo Excel usando o GeoPandas
gdf.to_excel(caminho_excel, index=False)
