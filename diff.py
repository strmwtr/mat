import arcpy

mat = r'C:\Users\brownr\Desktop\db\clean\clean.gdb\Updated_MAT'
fields = ['ST_NUMBER',	'ST_UNIT',	'UNIT_TYPE',	'PREDIR',	'ST_NAME',	
  'SUFFIX',	'POSTDIR',	'MasterAddressID',	'ST_NUMBER_1',	'ST_UNIT_1',	
  'UNIT_TYPE_1',	'PREDIR_1',	'ST_NAME_1',	'SUFFIX_1',	'POSTDIR_1',	
  'old_add',	'new_add',	'changed']
with arcpy.UpdateCursor(mat, fields) as cursor:
  for row in cursor:
    print row

