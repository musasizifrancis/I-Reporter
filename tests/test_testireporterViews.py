#from flask import Flask
#import unittest

#app = Flask(__name__)

#from blueprint_file import blueprint
#app.register_blueprint(blueprint, url_prefix='')

import unittest
from api import app
import json


class TestUser(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		
		
	def test_signupuser(self):

		user = dict()
		user['firstName'] = "Francis"
		user['LastName'] = "Kamanzi"
		user['otherNames'] = "Frank"
		user['email'] = "musasizifrancis@gmail.com"
		user['password'] = 12345
		user['username'] = "franko"
		user['registered'] = "registered"
		#"message": "user created successully" 
			
				#user = dict(
			 #         firstname="Francis",
		#         lastname="Kamanzi",
		#         othernames="Frank",
		#         email="musasizifrancis@gmail.com",
		#         password="12345")
		#username="franko"
		resp = self.app.post("api/v1/users", content_type="application/json", data=json.dumps(user))

		reply = json.loads(resp.data.decode())
		#self.assertIn("user created sucessfully", str(resp.data))
		self.assertEqual(resp.status_code, 201)
	
	def test_getAllusers(self):
		
		user = dict()
		user['firstName'] = "Francis"
		user['LastName'] = "Kamanzi"
		user['otherNames'] = "Frank"
		user['email'] = "musasizifrancis@gmail.com"
		user['password'] = 12345
		user['username'] = "franko"
		user['registered'] = "registered"
		
		resp = self.app.get("api/v1/users", content_type="application/json", data=json.dumps(user))
		
		#reply = json.loads(respp.data.decode())
		#self.assertEqual(resp.status_code, 201)
		
		

class TestFlags(unittest.TestCase):
	
		def setUp(self):
			self.app = app.test_client(self)
			
		def test_createIncident(self):
				createIncident = dict()
				createIncident['createdOn'] = "30-02-2018"
				createIncident['createdBy'] = "frank"
				createIncident['incidentType'] = "flooding"
				createIncident['location'] = "karamoja"
				createIncident['images'] = "images"
				
			
				resp = self.app.post("/api/v1/createIncident", content_type="application/json", data=json.dumps(createIncident))
				self.assertTrue(resp)
				#self.assertEqual(resp.status_code, 201)
				
		
		def test_get_all_red_flags_records(self):
			get_all_red_flag_records = dict()
			get_all_red_flag_records['createdBy'] = "frank"
			get_all_red_flag_records['createdOn'] = 30-02-2018,
			get_all_red_flag_records['image'] = "images"	
			
			
			resp = self.app.post("/api/v1/red-flags", content_type="application/json", data=json.dumps(get_all_red_flag_records))
			
			#self.assertEqual(resp.status_code, 200)
			
		
		def test_specific_redflag(self):
			get_specific_redflag = dict()
			get_specific_redflag['createdBy'] = "frank"
			get_specific_redflag['createdOn'] = 30-02-2018
			get_specific_redflag['image'] = "images"
			
			resp = self.app.get("/api/v1/redflags/<int:red_flag_id>", content_type="application/json", data=json.dumps(get_specific_redflag))
			
			#reply = json.loads(resp.data.decode())
    
				
		
		
	
			
			#def test_delete_specific_redflag_record(self):
				#self.app = app.test_client()	
				#resp = app.delete_client(self).get(
				#"api/v1/red-flags/red-flags/<int:red_flag_id>"
				#)
            #reply = json.loads(resp.data.decode())
        #self.assertTrue(reply)
        #self.assertEqual(resp.status_code, 201)
			#for item in list_of_Items:
				#[list_of_Items.remove(item) for key in item if item[key] == search_item]
				#return jsonify({
						#"status":200,
						#"id": search_item,
						#"data":incidents,
						#"message":"red-flag record deleted successfully"
						#})
						
		
		#def test_searchsId(search_item, list_of_Items):
			#search_list = []
			#list_of_items = []
			#for item in list_of_Items:
				#[search_list.append(item) for key in item if item[key] == search_item]
			#else search_item in list_of_Items:
				#[search_list.append(item) for key in item if item[key] == list_of_Items] 	
				#return jsonify({
                    #"status":201,
                    #"data":search_list
                    #}), 201
              				
        
