class User:

    def __init__(self, userId=int, firstName="", lastName="", 
                otherNames="", userName="", email="", password="", 
                registered="", isAdmin="False"):

        self.userId = userId
        self.firstName = firstName
        self.lastName = lastName
        self.otherNames = otherNames
        self.userName = userName
        self.email = email
        self.password = password
        self.registered = registered
        self.Admin = False
        
        
        def validate_input(self):
	    if not self.userId or self.userId.isspace():
	       return 'userId field can not be left empty.'
	    elif not self.firstName or self.firstName.isspace():
	       return 'firstName field can not be left empty.'
            elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
	       return 'Enter a valid email address.'
            elif not self.lastName or self.lastName.isspace():
		  return 'lastName field can not be left empty.'
	    elif not self.otherNames or self.otherNames.isspace():
			    return 'otherNames field can not be left empty.'	    
            elif not self.password or self.password.isspace():
                return 'Password field can not be left empty.'
            elif len(self.password) < 8:
                return 'Password has to be longer than 8 characters.'
                
		#users.append(user)
        
        def to_json(self):
			return {
					"userId": self.userId,
					"firstName": self.firstName,
					"lastName": self.lastName,
					"otherNames": self.otherNames,
					"userName": self.userName,
					"email": self.email,
					"password": self.password,
					"registered": self.registered					
			       }
			       
        

users = []

class Incident:
    def __init__(self, incidentId=int, createdOn="", createdBy="", incidentType="",
                location="", status="draft", images=[], 
                comment=""):
        self.incidentId = incidentId
        self.createdOn = createdOn
        self.createdBy = createdBy
        self.incidentType = incidentType
        self.location = location
        self.status = status
        self.images = images

def to_json(self):
			return {
					"incidentId": self.incidentId,
					"createdOn": self.createdOn,
					"createdBy": self.createdBy,
					"incidentType": self.incidentType,
					"location": self.location,
					"status": self.draft,
					"images": self.images
			       }   
        
incidents = []
