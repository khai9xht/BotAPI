# Metting Note 05/08/2021

### **Setup database for bot response**
 - Temporary: use YAML file (responses.yml in data folder) instead of database to save action_id and bot response
 - format: 
 	- text response directly  
 ```
	action_id: ulter_gretting
		responses:
		  - hello {username}		
		  - hi
		  - nice to meet you
		slots:
		  - username		#username is a variable decraled as slot in domain
 ```


### **understand slot in domain**
 - Define in domain.yml
 - format: key: value
 - Save specific infomation of entity or that user provided
	- It can influence next prediction of model or not
	- type: text/bool/categorical/float/list/any/undefined