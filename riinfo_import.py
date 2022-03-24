from io import StringIO
import numpy as np
import loadyaml_url as lyurl

class riinfo:
    def __init__(self, **kwargs):
        self.index_loaded = False
    
    def load_complete_db_index(self):
        print('Loading database index')
        default_url = "https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/library.yml"
        self.db_lib=lyurl.loadyaml_url(default_url)
        self.index_loaded = True
        
    def search_for_material(self, mat):
        if not self.index_loaded:
            self.load_complete_db_index()
        k = 0
        path_to_found = []
        for cat in self.db_lib:
            print('\tSearching category: %s'%(cat['name']))
            for el in cat['content']:
                try:
                    name = el['name']
                    if mat in name:
                            print('\t\tFound possible candidate: %s' %(name))
                            for dataset in el['content']:
                                if 'name' in dataset:
                                    k+=1
                                    print('\t\t\t%02d -> %s' % (k,dataset['name']))
                                    path_to_found.append(dataset['data'])
                except KeyError:
                    pass

                        
                                    
        no = int(input('Type in the number next to the material to load its refractive index: '))
        if no == 0:
            return("")
        else:
            self.path_to_mat = path_to_found[no-1]
            print('Found relative path: %s' % self.path_to_mat)
            return(self.path_to_mat)

    def load_material(self,path_to_material):
        loadurl="https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/data/"
        loadurl+=path_to_material        
        data=lyurl.loadyaml_url(loadurl)
        
        return np.genfromtxt(StringIO(data['DATA'][0]['data']))
    
    def search_and_load(self, mat):
        fn = self.search_for_material(mat)
        return(self.load_material(fn))
        
# # Create a new refractiveindex.info class
# riidb = rii.riinfo
# # Start a Database Search for the abbreviation
# data = riidb.search_and_load(' ')