import numpy



class ReactionParser(object):
    
    @property
    def species(self):
        '''
        list of all species reacted
        '''
        return self._species
        
    
    @property
    def data_lines(self):
        '''
        dictionary of all elements in each timestep
        key: timestep
        item: dictionary:
                key: specie
                item: number of molecules
        *This item exists to not read the file two times
        '''
        return self._data_lines
        
    
    @property
    def time_indexes(self):
        return self._time_indexes
        
        
    @property
    def specs_indexes(self):
        return self._specs_indexes
        
        
    @property
    def reaction_data(self):
        return self._reaction_data
    
    
    def _readfile(self, filename):
        '''
        Reads the species out file
        Returns: structure to be read in parse method
        
        '''
        file = open(filename, 'r')
        line = file.readline()
        line_number = 0
        
        species = self.species
        data_lines = self.data_lines
        
        while line:
            if line_number % 2 == 0:
                vals = line.split()
                vals = vals[4:]
                
                spec_in_timestep = [] 
                
                for spec in vals:
                    if spec not in species:
                        species.append(spec)
                    spec_in_timestep.append(spec)
                    
                line = file.readline()
                line_number += 1
                
                vals = line.split()
                timestep = vals[0]
                total_spec_in_timestep = []
                for spec in vals[3:]:
                    total_spec_in_timestep.append(int(spec))
                    
            
            data_lines[int(timestep)] = dict(zip(
                                spec_in_timestep,
                                total_spec_in_timestep
                                                )
                                
                                            )
                                            
            line = file.readline()
            line_number += 1
            
        
                
    def _parse(self, filename):
        '''
        Get data and format it into a matrix
        Returns:
                timesteps index (line number of the timstep)
                species index (column number of the species)
                data (matrix of number of molecule per timestep)
        '''
        self._readfile(filename)
        
        total_species = len(self.species)
        total_timesteps = len(self.data_lines.keys())
        data = numpy.zeros((total_timesteps, total_species), dtype=int)
        
        items  = [i for i in xrange(total_species)]
        indexes = dict(zip(self.species, items))
        
        timesteps = self.data_lines.keys()
        timesteps.sort()
        time_indexes = {}
        
        for i in xrange(len(timesteps)):
            key = timesteps[i]
            time_indexes[key] = i
            
        for key, item in self.data_lines.iteritems():
            id = time_indexes[key]
            for spec, mol in item.iteritems():
                data[time_indexes[key]][indexes[spec]] = mol
            
        
        return  time_indexes, indexes, data      
        
        
        
        
        
                
        
    def __init__(self, filename):
        self._species = []
        self._data_lines = {}
        
        times_id, specs_id, data = self._parse(filename)
        
        self._time_indexes = times_id
        self._specs_indexes = specs_id
        self._reaction_data = data
        
        
        
        
        
if __name__ == '__main__':
    filename = 'data/out_species.out'
    
    a = ReactionParser(filename)
    
    import pdb; pdb.set_trace()
    
                
                
                
                    
                        
                        
                        
                        
                        
                        
                        
                        
                
            
    
    
   