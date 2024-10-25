import arcpy

def search_data(feature_class, fields):
    with arcpy.da.SearchCursor(feature_class, fields) as cursor:
        for row in cursor:
            print(row)

if __name__ == "__main__":
    arcpy.env.workspace = r"C:/Users/paulo.martins/Desktop/minhas-financas-arcgis/minhasfinancas-arcgis.gdb"
    feature_class = "PT_FICTICIO"
    fields = ['SHAPE@', 'id_lancamento', 'descricao', 'mes', 'ano', 'valor', 'tipo', 'latitude', 'longitude', 'categoria_id']
    search_data(feature_class, fields)
   
