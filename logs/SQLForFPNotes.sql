CREATE TABLE AttendanceTable (AttendancePctg INT NOT NULL, PRIMARY KEY(UserID,EventID), FOREIGN KEY (UserID) REFERENCES UserTable(UserID), FOREIGN KEY (EventID) REFERENCES EventTable(EventID));

CREATE TABLE `AttendanceTable` (`UserID`INT NOT NULL,`EventID`INT NOT NULL,`AttendancePctg`INT NOT NULL, PRIMARY KEY(`UserID`,`EventID`), FOREIGN KEY (`UserID`) REFERENCES `UserTable`(`UserID`), FOREIGN KEY (`EventID`) REFERENCES `EventTable`(`EventID`));




CREATE TABLE `IssuedEquipmentTable` (`UserID`INT NOT NULL,

`EquipmentID`INT NOT NULL,`IssueDate`INT NOT NULL,

`ReturnDate`INT NOT NULL, `DateReturned`INT NOT NULL, `DateReplaced`INT NOT NULL,

`EquipmentStatus` INT NOT NULL,

PRIMARY KEY(`UserID`,`EquipmentID`), 

FOREIGN KEY (`UserID`) REFERENCES `UserTable`(`UserID`), 
FOREIGN KEY (`EquipmentID`) REFERENCES `EquipmentTable`(`EquipmentID`));