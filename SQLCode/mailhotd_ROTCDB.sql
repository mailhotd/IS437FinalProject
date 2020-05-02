-- phpMyAdmin SQL Dump
-- version 4.0.10deb1ubuntu0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 02, 2020 at 12:42 PM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `mailhotd_ROTCDB`
--

-- --------------------------------------------------------

--
-- Table structure for table `AttendanceTable`
--

CREATE TABLE IF NOT EXISTS `AttendanceTable` (
  `UserID` int(11) NOT NULL,
  `EventID` int(11) NOT NULL,
  `AttendanceStatus` varchar(20) NOT NULL,
  `UserEvaluation` text NOT NULL,
  PRIMARY KEY (`UserID`,`EventID`),
  KEY `EventID` (`EventID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `EquipmentTable`
--

CREATE TABLE IF NOT EXISTS `EquipmentTable` (
  `EquipmentID` int(11) NOT NULL AUTO_INCREMENT,
  `NatoStockNumber` bigint(13) NOT NULL,
  `EquipmentName` varchar(20) NOT NULL,
  `DateAcquired` datetime DEFAULT NULL,
  `DateRetired` datetime DEFAULT NULL,
  PRIMARY KEY (`EquipmentID`),
  UNIQUE KEY `NatoStockNumber` (`NatoStockNumber`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `EquipmentTable`
--

INSERT INTO `EquipmentTable` (`EquipmentID`, `NatoStockNumber`, `EquipmentName`, `DateAcquired`, `DateRetired`) VALUES
(6, 8012547863122, 'Green Socks', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(7, 1457896521487, 'Green Socks', '2019-01-01 00:00:00', '0001-01-01 00:00:00'),
(10, 2512458763659, 'Tan Boots', '2020-01-01 00:00:00', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `EventTable`
--

CREATE TABLE IF NOT EXISTS `EventTable` (
  `EventID` int(11) NOT NULL AUTO_INCREMENT,
  `EventName` varchar(30) NOT NULL,
  `EventStartDT` datetime NOT NULL,
  `EventEndDT` datetime NOT NULL,
  `EventStatus` text NOT NULL,
  `EventSemester` text NOT NULL,
  PRIMARY KEY (`EventID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `EventTable`
--

INSERT INTO `EventTable` (`EventID`, `EventName`, `EventStartDT`, `EventEndDT`, `EventStatus`, `EventSemester`) VALUES
(6, 'PT', '2020-12-01 01:00:00', '2020-01-01 02:00:00', 'Mandatory', 'Fall');

-- --------------------------------------------------------

--
-- Table structure for table `IssuedEquipmentTable`
--

CREATE TABLE IF NOT EXISTS `IssuedEquipmentTable` (
  `UserID` int(11) NOT NULL,
  `EquipmentID` int(11) NOT NULL,
  `IssueDate` datetime NOT NULL,
  `ReturnDate` datetime NOT NULL,
  `DateReturned` datetime NOT NULL,
  `DateReplaced` datetime NOT NULL,
  `EquipmentStatus` text NOT NULL,
  PRIMARY KEY (`UserID`,`EquipmentID`),
  UNIQUE KEY `UserID` (`UserID`,`EquipmentID`),
  KEY `EquipmentID` (`EquipmentID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `UserTable`
--

CREATE TABLE IF NOT EXISTS `UserTable` (
  `UserID` int(11) NOT NULL AUTO_INCREMENT,
  `UserFName` text NOT NULL,
  `UserLName` text NOT NULL,
  `UserType` text NOT NULL,
  `UserEmail` varchar(20) NOT NULL,
  `UserPassword` varchar(30) NOT NULL,
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `UserTable`
--

INSERT INTO `UserTable` (`UserID`, `UserFName`, `UserLName`, `UserType`, `UserEmail`, `UserPassword`) VALUES
(1, 'Cadet', 'Major', 'Admin', 'admin@rotc.com', '12345'),
(4, 'Cadet', 'Sergeant', 'User', 'sgt@rotc.com', 'qwert');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `AttendanceTable`
--
ALTER TABLE `AttendanceTable`
  ADD CONSTRAINT `AttendanceTable_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `UserTable` (`UserID`),
  ADD CONSTRAINT `AttendanceTable_ibfk_2` FOREIGN KEY (`EventID`) REFERENCES `EventTable` (`EventID`);

--
-- Constraints for table `IssuedEquipmentTable`
--
ALTER TABLE `IssuedEquipmentTable`
  ADD CONSTRAINT `IssuedEquipmentTable_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `UserTable` (`UserID`),
  ADD CONSTRAINT `IssuedEquipmentTable_ibfk_2` FOREIGN KEY (`EquipmentID`) REFERENCES `EquipmentTable` (`EquipmentID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
