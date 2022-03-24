from io import StringIO
import numpy as np
import loadyaml_url
class riinfo_db:
    def __init__(self, **kwargs):
        self.index_loaded = False
        pass
    
    def load_complete_db_index(self, **kwargs):
        print('Loading database index')
        default_url = "https://raw.githubusercontent.com/polyanskiy/refractiveindex.info-database/master/database/library.yml"
        self.riinfo_db_lib_url=kwargs.get( 'url',default_url)
        self.db_lib=loadyaml_url(self.riinfo_db_lib_url)
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
        # data = urllib.request.urlopen(loadurl).read().decode('utf8')
        
        data = loadyaml_url(loadurl)
        
        return np.genfromtxt(StringIO(data['DATA'][0]['data']))
    
    def search_and_load(self, mat):
        fn = self.search_for_material(mat)
        return(self.load_material(fn))
        
