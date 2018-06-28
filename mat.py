import arcpy

#MAT = r'Database Connections\Connection to GISPRDDB direct connect.sde\cvGIS.CITY.MASTERADDRESS'
MAT = r'C:\Users\brownr\Desktop\db\clean\clean.gdb\mat'
edit_fields = ['ST_NUMBER', 'ST_UNIT', 'UNIT_TYPE']
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
        print row[0]
        cursor.updateRow(row)

def pound_to_unit():
  unique = []
  with arcpy.da.UpdateCursor(MAT, ['UNIT_TYPE','ST_UNIT']) as cursor:
    for row in cursor:
      if row[0] == '#' and not row[1].isdigit():
        unique.append(row[1])
    for x in sorted(set(unique)):
      print x
      '''
      if len(row[1]) == 1 and row[1].isalpha():
        row[0] = 'UNIT'
        cursor.updateRow(row)
      '''

pound_to_unit()

def calls():
  strip_all()
  clean_unit()