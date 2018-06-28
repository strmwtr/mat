import arcpy

MAT = r'Database Connections\Connection to GISPRDDB direct connect.sde\cvGIS.CITY.MASTERADDRESS'
#MATc = r'C:\Users\brownr\Desktop\db\clean\clean.gdb\mat_clean'
#MAT = r'C:\Users\brownr\Desktop\db\clean\clean.gdb\mat'
edit_fields = ['ST_NUMBER', 'ST_UNIT', 'UNIT_TYPE']

def copy_mat():
  arcpy.Delete_management(MAT)
  arcpy.Copy_management(MATc, MAT)

def get_set(field):
  with arcpy.da.SearchCursor(MAT, field) as cursor:
    values = set([row[0] for row in cursor])
  return values

def strip_all():
  for field in edit_fields:
    with arcpy.da.UpdateCursor(MAT, field) as cursor:
      for row in cursor:
        row[0] = row[0].strip()
        cursor.updateRow(row)


def clean_unit():
  with arcpy.da.UpdateCursor(MAT, 'ST_UNIT') as cursor:
    for row in cursor:
      if ' ' in row[0]:
        row[0] = row[0].replace(' ','')
        cursor.updateRow(row)

def pound_to_unit():
  values = []
  special = ['BACKFLOW', 'BSMT', 'COTT', 'DOWN', 'GARG', 'UP','UPPER']
  with arcpy.da.UpdateCursor(MAT, ['UNIT_TYPE','ST_UNIT']) as cursor:
    for row in cursor:
      #List cases where UNIT_TYPE is # and ST_UNIT is not a num
      if row[0] == '#' and not row[1].isdigit():
        if row[1] in special:
          row[0] = ''
          cursor.updateRow(row)
        else:
          row[0] = 'UNIT'
          cursor.updateRow(row)
      if row[0] == '' and row[1] != '' and row[1] not in special:
          row[0] = 'UNIT'
          cursor.updateRow(row)

def print_stuff():
  special = ['BACKFLOW', 'BSMT', 'COTT', 'DOWN', 'GARG', 'UP','UPPER']
  with arcpy.da.UpdateCursor(MAT, ['UNIT_TYPE','ST_UNIT']) as cursor:
    for row in cursor:
      # Changes # A to UNIT A
      if row[0] == '' and row[1] != '' and row[1] not in special:
        print row

def calls():
  strip_all()
  clean_unit()
  pound_to_unit()

calls()
