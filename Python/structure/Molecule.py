


class Molecule(object):
    @property
    def molecule_id(self):
        return self._molecule_id
        
    @property
    def atoms(self):
        return self._atoms
        
    @property
    def bonds(self):
        return self._bonds
        
    
    def __init__(self):
        self._atoms = []
        self._bonds = []
        
        
    def AddAtom(self, atom):
        self.atoms.append(atom)
        
    def AddBond(self, bond):
        self.bonds.append(bond)
        
    def GenerateFingerPrint(self):
        fp = {}
        atoms = self._atoms
        
        for i in atoms:
            if i.atom_id not in fp.keys():
                fp[i.atom_id] = 1
            else:
                fp[i.atom_id] += 1
                
        return fp
        
    def GenerateBonds(self, model):
        pass