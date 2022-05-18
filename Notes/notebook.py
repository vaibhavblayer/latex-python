
import datetime
last_id = 0

class Note:
	def __init__(self, body, tags=""):
		self.body = body
		self.tags = tags
		self.creation_Date = datetime.date.today() 
		
		global last_id
		last_id += 1
		self.id = last_id



