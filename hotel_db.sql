-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 23, 2022 at 07:30 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `id` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Phone_number` bigint(20) NOT NULL,
  `Date_` date NOT NULL,
  `Total_Amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`id`, `Name`, `Phone_number`, `Date_`, `Total_Amount`) VALUES
(1, 'Mahalakshmi', 9065478876, '2022-10-01', 175),
(2, 'Ashme', 7658990032, '2022-11-01', 978),
(3, 'Lakshmi', 7865778856, '2022-10-31', 114),
(4, 'mega', 2332890005, '2022-11-03', 90),
(5, 'Manju', 7888665543, '2022-11-09', 90),
(6, 'Sneha', 5566443327, '2022-10-03', 120),
(7, 'Amali', 6754338876, '2022-10-03', 75),
(8, 'Mannu', 4566773329, '2022-10-31', 249),
(9, 'rty', 56783321, '2022-10-14', 75),
(10, 'class', 896655432, '2022-11-12', 680);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
