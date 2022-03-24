import riinfo_import as rii

# Create a new refractiveindex.info class
riidb = rii.riinfo_db()
# Start a Database Search for the abbreviation
data = riidb.search_and_load('Au')

# If the relative path is known, one can load it directly
relpath_to_data = 'main/Au/Johnson.yml'
data = riidb.load_material(relpath_to_data)
