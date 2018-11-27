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
        users.append(self)
        

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

incidents = []    
        
