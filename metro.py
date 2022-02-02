class Metro:
	def __init__(self, name, code,dir,frequency):
		self.name = name
		self.code=code
		self.dir=dir
		self.frequency=frequency

	def __str__(self):
		return str.format("{}\t{}\t{}\t{}", self.name, self.code,self.dir,self.frequency)