


#Inhertiance
class Debitcard:
	def __init__(self):
		print "init from class def"
	def status(self):
		print "card status"
	def addition(self):
		print "added a method"


class standalone:
	def __init__(self):
		print "init from class stand"

	def multiclass(self):
		print "multiclass"

	def status(self):
		print "card status from stanaline"
	
class creditcard(standalone,Debitcard,): #inheritance/single inheritance, multiple inheritance
	def __init__(self):
		print "This is debit card class"

	def test(self):
		print "this is test function"


b = creditcard() #obj creation
b.test()
b.status() 
b.multiclass()