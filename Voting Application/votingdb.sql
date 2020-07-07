-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 28, 2019 at 12:05 AM
-- Server version: 10.1.29-MariaDB
-- PHP Version: 7.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `votingdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `partydb`
--

CREATE TABLE `partydb` (
  `Id` int(11) NOT NULL,
  `PartyName` varchar(80) NOT NULL,
  `PartyChar` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `partydb`
--

INSERT INTO `partydb` (`Id`, `PartyName`, `PartyChar`) VALUES
(1, 'TMC', 'Mamata Banerjee'),
(2, 'BJP', 'Narendra Modi'),
(3, 'CPI', 'R. Mutharasan');

-- --------------------------------------------------------

--
-- Table structure for table `voters`
--

CREATE TABLE `voters` (
  `Id` int(11) NOT NULL,
  `VoterName` varchar(50) NOT NULL,
  `VoterIdCard` int(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `voters`
--

INSERT INTO `voters` (`Id`, `VoterName`, `VoterIdCard`) VALUES
(1, 'Khalid', 16102),
(2, 'Drake', 17102),
(3, 'Weeknd', 15101);

-- --------------------------------------------------------

--
-- Table structure for table `votes`
--

CREATE TABLE `votes` (
  `Id` int(11) NOT NULL,
  `VoteParty` varchar(80) NOT NULL,
  `VoterName` varchar(50) NOT NULL,
  `VoterIdCard` int(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `votes`
--

INSERT INTO `votes` (`Id`, `VoteParty`, `VoterName`, `VoterIdCard`) VALUES
(1, 'TMC', 'Khalid', 16102),
(2, 'BJP', 'Drake', 17102),
(4, 'CPI', 'Weeknd', 15101);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `partydb`
--
ALTER TABLE `partydb`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `voters`
--
ALTER TABLE `voters`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `votes`
--
ALTER TABLE `votes`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `partydb`
--
ALTER TABLE `partydb`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `voters`
--
ALTER TABLE `voters`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `votes`
--
ALTER TABLE `votes`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
