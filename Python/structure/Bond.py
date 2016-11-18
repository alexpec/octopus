


class Bond(object):
    @property
    def bond_type(self):
        return self._bond_type
    
    @property
    def bond_id(self):
        return self._bond_id
    
    @property
    def a(self):
        return self._a
        
    @property
    def b(self):
        return self._b
        
        
    def __init__(self, bond_id, bond_type, a, b):
        self._bond_id = bond_id
        self._bond_type = bond_type
        self._a = a
        self._b = b