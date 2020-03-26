# IS 437 Final Project Documentation
 
## Project Narrative
* For technical purposes, upperclassmen (seniors) will be administrators for the UI and underclassmen will be users. 
This application will allow administrators to create events, issue equipment to users and verify attendance. 
Users’ attendance would be recorded in person and only updated by administrators later if necessary. 
Administrators will be able to employ CRUD operations across all tables populated by the UI. 
There will be five tables. One user table that contains user demographics; id, first name, last name, email and type (user or admin). 
The other two primary tables will be an equipment table that contains all possible items to be rented out to users and an event table that contains all possible events a user could attend. 
Due to the many-many relationships between the user table and the two other main tables, there need to be bridge entity tables to record the individual instances (which user has which items or which user has attended which event). 
These are the attendance and issued equipment tables. 
Furthermore, they exist because not every item in inventory is not issued to every user and not all events are mandatory. 
Additionally, a user’s attendance percentage is only impacted by mandatory events. 


## Use Cases

*	Administrator creates user profile
*	Administrator updates user profile
*	Administrator updates user type
*	Administrator deletes user profile
*	Administrator creates event
*	Administrator updates event
*	Administrator deletes event
*	Administrator creates new item in equipment table
*	Administrator deletes item in equipment table
*	User reports attendance
*	Administrator verifies attendance record
*	System calculates attendance percentage
*	Administrator verifies issued equipment status
*	Administrator creates date replaced/returned
*	Administrator updates date replaced/returned
*	Administrator deletes date replaced/returned
*	User updates issued equipment status (lost, retired or returned)

## Relational Schema:

![A Relational Schema should appear here](/IS437_FinalProject_Folder/IS437_FP_OverviewAndSchema.png)