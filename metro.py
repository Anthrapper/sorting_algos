
class Metro:
	def __init__(self, name, code,dir,frequency,q1,q2,q3,q4):
		self.name = name
		self.code=code
		self.dir=dir
		self.frequency=frequency
		self.q1=q1,
		self.q2=q2,
		self.q3=q3,
		self.q4=q4,

	def __str__(self):
		return str.format("{}\t{}\t{}\t{}", self.name, self.code,self.dir,self.frequency)

	# def __repr__(self):
	# 	return str.format("{}\t{}\t{}", self.name, self.code,self.dir)
			
	def get(self,varname):
		return getattr(self,varname)
