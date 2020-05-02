# IS 437 Final Project Documentation
 
## Project Narrative:
* For technical purposes, upperclassmen (seniors) will be administrators for the UI and underclassmen will be users. 
This application will allow administrators to create events, issue equipment to users and verify attendance. 
Users’ attendance would be recorded in person and only updated by administrators later if necessary. 
Administrators will be able to employ CRUD operations across all tables populated by the UI. 
There will be five tables. One user table that contains user demographics; id, first name, last name, email and type (user or admin). 
The other two primary tables will be an equipment table that contains all possible items to be rented out to users and an event table that contains all possible events a user could attend. 
Due to the many-many relationships between the user table and the two other main tables, there need to be bridge entity tables to record the individual instances (which user has which items or which user has attended which event). 
These are the attendance and issued equipment tables. 
Furthermore, they exist because not every item in inventory is not issued to every user and not all events are mandatory. 
User information will be maintained on their behalf by administrators.

### User Table 

UserID	| UserFName	| UserLName |	Type | Email |	Password
------------ | ------------- | -------------- | -------------- | -------------- | --------------
1	| Cadet | Major | Admin | admin@rotc.com	| 12345
4 |	Cadet | Sergeant |	User |	sgt@rotc.com | qwert


## Relational Schema:

![A Relational Schema should appear here](/OverviewAndSchema/IS437_FP_Schema.png)
