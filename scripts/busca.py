import arcpy

arcpy.env.workspace = r"C:/Users/paulo.martins/Desktop/minhas-financas-arcgis/minhasfinancas-arcgis.gdb"
feature_class = "PT_FICTICIO"
fields = ['SHAPE@', 'id_lancamento', 'descricao', 'mes', 'ano', 'valor', 'tipo', 'latitude', 'longitude', 'categoria_id']

def search_data(feature_class, fields):
    with arcpy.da.SearchCursor(feature_class, fields) as cursor:
        for row in cursor:
            print(row)

def main():
    search_data(feature_class, fields)

if __name__ == "__main__":
    main()
