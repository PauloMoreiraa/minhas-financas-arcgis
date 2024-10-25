import json
import arcpy

def extract_transform_data(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
    transformed_data = []
    
    sirgas2000 = arcpy.SpatialReference(4674) 
    
    for item in data:
        id_lancamento = item.get('id')
        descricao = item.get('descricao')
        mes = item.get('mes')
        ano = item.get('ano')
        valor = item.get('valor')
        tipo = item.get('tipo')
        latitude = item.get('latitude')
        longitude = item.get('longitude')
        categoria_id = item.get('categoria', {}).get('id') if item.get('categoria') else None
        
        if latitude is not None and longitude is not None:
            point = arcpy.Point(longitude, latitude)
            point_geometry = arcpy.PointGeometry(point, sirgas2000)
        else:
            point_geometry = None  
        
        transformed_data.append((point_geometry, id_lancamento, descricao, mes, ano, valor, tipo, latitude, longitude, categoria_id))
    
    return transformed_data

def load_data_to_database(transformed_data, feature_class, fields):
    with arcpy.da.InsertCursor(feature_class, fields) as cursor:
        for row in transformed_data:
            cursor.insertRow(row)

def etl_process(json_file, feature_class, fields):
    transformed_data = extract_transform_data(json_file)
    load_data_to_database(transformed_data, feature_class, fields)
    

if __name__ == "__main__":
    arcpy.env.workspace = r"C:/Users/paulo.martins/Desktop/minhas-financas-arcgis/minhasfinancas-arcgis.gdb"
    feature_class = "PT_FICTICIO"
    fields = ['SHAPE@', 'id_lancamento', 'descricao', 'mes', 'ano', 'valor', 'tipo', 'latitude', 'longitude', 'categoria_id']
    json_file = r'C:/Users/paulo.martins/Desktop/minhas-financas-arcgis/json/lancamentos.json'
    etl_process(json_file, feature_class, fields)
    print("Processo ETL concluído com sucesso!")
