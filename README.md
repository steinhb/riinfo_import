# riinfo_import

Module to easily load refractive index data from the refractiveindex.info database.

Usage (starts a search in the database for the abbreviation)
    
    import riinfo_import as rii
    data = riidb.search_and_load('Au')

If the relative path is already known one can load it directly with:
    
    relpath_to_data = 'main/Au/Johnson.yml'
    data = riidb.load_material(relpath_to_data)

The data is a numpy array holding the tabulated data.