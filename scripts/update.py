import arcpy

arcpy.env.workspace = r"C:/Users/paulo.martins/Desktop/minhas-financas-arcgis/minhasfinancas-arcgis.gdb"
feature_class = "PT_FICTICIO"
fields = ['id_lancamento', 'descricao',  'valor', 'tipo', 'status', 'categoria_id']

# with arcpy.da.SearchCursor(feature_class, fields) as cursor:
#     for row in cursor:
#         print(row)
        
# print("--------------------------")
where = "id_lancamento = 2"
with arcpy.da.UpdateCursor(feature_class, fields, where_clause=where) as cursor:
    for row in cursor:
        row[4] = 2
        
        cursor.updateRow(row)
        
# print("--------------------------")

# with arcpy.da.SearchCursor(feature_class, fields) as cursor:
#     for row in cursor:
#         print(row)