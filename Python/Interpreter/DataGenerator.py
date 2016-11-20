import numpy

class DataGenerator(object):
	@property
	def output_filename(self):
		'''
		 The output filename
		'''
		return self._output_filename

	@property
	def atoms(self):
		'''
		 The total of atoms
		'''
		return self._atoms

	@property
	def molecules(self):
		'''
		 The total of molecules
		'''
		return self._molecules

	@property
	def atom_types(self):
		'''
		 Dictionary with the atom types
		 KEY: Atom Name (ex. O, C, H, N)
		 ITEM: Atom index
		'''
		return self._atom_types

	@property
	def lines(self):
		'''
		 The lines that will be printed in the output file
		'''
		return self._lines

	@property
	def coordinates(self):
		'''
		 The coordinates of all atoms
		'''
		return self._coordinates

	######################################
	def _extract(self, filename):
		jump_lines = 4
		id = 0
		input = open(filename, 'r')
		line = input.readline()

		while line:

			if id > jump_lines:
				data = line.split()
				if len(data) < 10: break
				atom_id 	= int(data[1])
				atom_type 	= data[2]
				atom_molec	= int(data[5])
				atom_x		= float(data[6])
				atom_y		= float(data[7])
				atom_z		= float(data[8])
				
				self._atoms += 1

				if atom_type not in self.atom_types.keys():
					atom_id = len(self.atom_types.keys()) + 1 
					self.atom_types[atom_type] = atom_id
								
				

				str = '%i %i 0.0 %.4f %.4f %.4f' %(
						atom_id,
						self.atom_types[atom_type],
						atom_x, atom_y, atom_z)

				self.coordinates.append([atom_x, atom_y, atom_z])
				self.lines.append(str)				
							


			line = input.readline()
			id += 1
		coords = numpy.array(self.coordinates)

		x_min = numpy.min(coords[:,0])
		x_max = numpy.max(coords[:,0])

		y_min = numpy.min(coords[:,1])
		y_max = numpy.max(coords[:,1])
		
		z_min = numpy.min(coords[:,2])
		z_max = numpy.max(coords[:,2])

		masses = {}

		for key, item in self.atom_types.iteritems():
			str = 'Which mass of %s [dalton]: ' %key
			atom_mass = float(raw_input(str))
			masses[key] = atom_mass		



		print 'Total Atoms: %i' %self.atoms
		print 'Total Types: %i' %len(self.atom_types.keys())

		print '%.4f, %.4f xlo, xhi' %(x_min, x_max)
		print '%.4f, %.4f ylo, yhi' %(y_min, y_max)
		print '%.4f, %.4f zlo, zhi' %(z_min, z_max)
		

		for key, item in self.atom_types.iteritems():
			print "Mass %s (%i) => %.4f" %(key, item, masses[key])



		out = open(self.output_filename, 'w')
		out.write("#File Generate with Data Generator\n\n")

		out.write('%i atoms\n' %self.atoms)
		out.write('%i atom types\n\n' %len(self.atom_types.keys()))
		
		out.write('%.4f %.4f xlo xhi\n' %(x_min, x_max))
		out.write('%.4f %.4f ylo yhi\n' %(y_min, y_max))
		out.write('%.4f %.4f zlo zhi\n\n' %(z_min, z_max))

		out.write('Masses\n\n')

		for key, item in self.atom_types.iteritems():
			out.write('%i %.4f\n' %(item, masses[key]))

		
		out.write('\nAtoms\n\n')

		for line in self.lines:
			out.write(line + '\n')

		out.flush()
		out.close()

	def __init__(self, input_filename, output_files):
		self._lines = []
		self._coordinates = []
		self._output_filename = output_files
		self._atoms = 0
		self._atom_types = {}

		self._extract(input_filename)
	
if __name__ == '__main__':
	filename = 'data/mixture.pdb'
	DataGenerator(filename, 'out.data')
