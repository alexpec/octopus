



class Atom(object):
    @property
    def atom_type(self):
        return self._atom_type
        
    @property
    def atom_id(self):
        return self._atom_id
        
    @property
    def mass(self):
        return self._mass
        
    @property
    def x(self):
        return self._x
        
    @property
    def y(self):
        return self._y
        
    @property
    def z(self):
        return self._z
        
        
    
    def __init__(self, atom_id, atom_type, mass, x, y, z):
        self._atom_type = atom_type
        self._atom_id = atom_id
        self._mass = mass
        self._x = x
        self._y = y
        self._z = z
        