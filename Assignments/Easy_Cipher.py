"""
Name: Jeron Amory
Email: j.amory268@gmail.com
Assignment: Program 1 - Easy Cipher
Due: 3 October @ 1:00 p.m.
"""

"""
@ Name: ShiftCipher
@ Description: Simple class to do a shift cipher
"""
class ShiftCipher(object):
	
	"""
	@ Name: __init__
	@ Description: 
	@ Params:
	     None
	"""
	def __init__(self):
		
		self.plainText = None
		self.cipherText = None
		self.cleanText = None
		self.shift = 3
	"""
	Nice string representation of your class to help debug.
	"""
	def __str__(self):
		return "plainText: %s\ncipherText: %s\ncleanText: %s\nshift: %d\n" % (self.plainText,self.cipherText,self.cleanText,self.shift)
	
	"""
	@ Name: promptUserMessage
	@ Description: Prompts user for message from standard in
	@ Params:
	     None
	"""
	def promptUserMessage(self):
		temp = input("Message: ")
		self.setMessage(temp)

	"""
	@ Name: setMessage
	@ Description: sets plaintext and then cleans and calls encrypt.
	@ Params:
	     message {string}: String message
	     encrypted {bool}: False = plaintext True=ciphertext
	"""
	def setMessage(self,message,encrypted=False):
		if(not encrypted):
			self.plainText = message
			self.cleanData()
			self.__encrypt()
		else:
			self.cipherText = message
			self.__decrypt()
	
	def getCipherText(self):
		return self.cipherText
		
	def getPlainText(self):
		return self.plainText

	def setShift(self,shift):
		self.shift = shift
	
	def getShift(self):
		return self.shift
		
	"""
	Returns only alphanumerics in message
	"""		
	def cleanData(self):
		self.cleanText = ''
		for letter in self.plainText:
			if (ord(letter)>122 or ord(letter)<65):
				continue
			if (ord(letter)>90 and ord(letter)<97):
				continue
			if ord(letter) > 96:
				self.cleanText += chr(ord(letter)-32)
			else:
				self.cleanText += letter

			
		

	"""
	Encrypts plaintext not ciphertext
	"""
	def __encrypt(self):
		self.cipherText = ''
		if(not self.cleanText):
			return
		for letter in self.cleanText:
		    self.cipherText += chr((((ord(letter)-65) + self.shift) % 26)+65)
		    
		
	
	"""
	Decrypts ciphertext not plaintext
	"""
	def __decrypt(self):
		self.plainText= ''
		for letter in self.cipherText:
			self.plainText += chr((((ord(letter)-65) - self.shift)%26)+65)
	
alice = ShiftCipher()
alice.promptUserMessage()
print(alice)

bob = ShiftCipher()
bob.setMessage(alice.getCipherText(),True)
print(bob)

"""
Only run this if we call this file directly:
"""
if __name__=='__main__':

   main()


   
