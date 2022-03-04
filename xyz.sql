-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 03, 2020 at 10:57 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `xyz`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE IF NOT EXISTS `account` (
  `email` varchar(100) NOT NULL COMMENT 'Primary key',
  `password` varchar(100) NOT NULL,
  `address` varchar(300) NOT NULL,
  `location` varchar(300) NOT NULL,
  `files` varchar(100) NOT NULL,
  `religion` varchar(100) NOT NULL,
  `phone` int(10) NOT NULL,
  `family` int(100) NOT NULL,
  `senior` int(100) NOT NULL,
  `children` int(100) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`email`, `password`, `address`, `location`, `files`, `religion`, `phone`, `family`, `senior`, `children`) VALUES
('aromal@gmail.com', 'aromal', 'kdhcnvifjn', 'ljvkofdi', 'IMG-20200122-WA0003.jpg', 'hindu', 2147483647, 5, 2, 1),
('aswath@gmail.com', 'aswath', 'hhdfddfgdfg', 'hdgfdfg', 'lamp-technology-3-638.jpg', 'hindu', 2147483647, 3, 1, 1),
('dilshamdeleep20@gmail.com', '123456', 'karimbil house,kra-14 ', 'Thaikkattukara, Choornikkara, Aluva, Kerala, India', '5555 - DILSHA M DELEEPPASSPORT_54FkV4G.jpg', 'muslim', 2147483647, 5, 2, 1),
('dyan@gmail.com', '123456', 'glkjtrkyngjhg', 'dkjfhtrn', 'Admin-icon.png', 'christian', 2147483647, 7, 2, 1),
('hema@gmail.com', '123456', 'sweet  home', 'ernakulam', 'S0-14-512_MmKx9Hr.png', 'hindu', 2147483647, 8, 2, 3),
('hima@gmail.com', '123456', 'sweet  home', 'kochi', 'IMG-20191120-WA0010.jpg', 'muslim', 2147483647, 5, 3, 1),
('jissjohn@gmail.com', '123456', 'sweet  home', 'kottayam', 'S0-14-512.png', 'christian', 2147483647, 5, 0, 3),
('praveen@gmail.com', '123456', 'snehatheeram', 'ankamali', 'Admin-icon.png', 'hindu', 2147483647, 7, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `addpro`
--

CREATE TABLE IF NOT EXISTS `addpro` (
  `pdtname` varchar(100) NOT NULL,
  `pdttype` varchar(50) NOT NULL,
  `description` varchar(300) NOT NULL,
  `startdate` date NOT NULL,
  `enddate` date NOT NULL,
  `files` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL COMMENT 'Primary key',
  `password` varchar(100) NOT NULL,
  `phno` varchar(100) NOT NULL,
  `pdt_id` varchar(100) NOT NULL COMMENT 'Primary key',
  `price` int(11) NOT NULL,
  `time` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `addpro`
--

INSERT INTO `addpro` (`pdtname`, `pdttype`, `description`, `startdate`, `enddate`, `files`, `location`, `email`, `password`, `phno`, `pdt_id`, `price`, `time`) VALUES
('flat', 'House & Rooms', '3bhk apartment near railway station and city hopital ernakulam', '2019-12-01', '2020-09-30', '3_bhk_apartment-for-rent-hsr_layout_bangalore-Bangalore_5SzdXtn.webp', 'ernakulam', 'aromal@gmail.com', '123456', '9207543608', '305', 1200, '2019-10-29 22:49:10.822144'),
('apartment', 'House & Rooms', '2 bhk apartment near marine drive , childrens park, shopping mall and medical center', '2019-12-24', '2020-05-26', '45b0cdf193f178d675391d4095b5ef83a77a87cd.jpg', 'thevara', 'aromal@gmail.com', '123456', '9207543608', '170', 1000, '2019-10-29 22:52:21.350469'),
('house', 'House & Rooms', 'house near lulu mall, school,renai school at edappally', '2019-12-01', '2020-12-01', '302-tx_aus_hyde_park_271437_0087_256x256_cfill_JScSWbZ.jpg', 'edappally', 'aromal@gmail.com', '123456', '9207543608', '885', 1000, '2019-10-29 22:58:07.429071'),
('flat', 'House & Rooms', 'flat near st.antony church , metro and bus station,kaloor', '2019-12-17', '2020-08-17', '517da4582f0554835bd39c873c9cb673c-f0od-w480_h360.jpg', 'kaloor', 'aromal@gmail.com', '123456', '9207543608', '960', 1300, '2019-10-29 23:01:30.002554'),
('flat', 'House & Rooms', '2 bhk apartment near st.xavior,s college and aluva bus and train station', '2019-12-29', '2020-11-29', '8025e85266bd73.jpg', 'aluva', 'aromal@gmail.com', '123456', '9207543608', '355', 740, '2019-10-29 23:04:34.752502'),
('flat', 'House & Rooms', '4bhk near aster medicity ', '2019-12-08', '2020-12-08', '11830825.jpg', 'cheranallur', 'aromal@gmail.com', '123456', '9207543608', '495', 1500, '2019-10-29 23:10:08.692531'),
('flat', 'House & Rooms', '1 bhk ac room near mattancery ferry', '2019-12-12', '2020-02-27', '1440760999-65231130.jpg', 'mattanchery', 'aromal@gmail.com', '123456', '9207543608', '870', 1500, '2019-10-29 23:13:25.502393'),
('flat', 'House & Rooms', '2 bhk apartment near marine drive , childrens park, shopping mall and medical center', '2019-12-23', '2020-12-23', 'b43406edebc98d504cf7b0d6193e55bc0a1346d1.jpg', 'ernakulam', 'aromal@gmail.com', '123456', '9207543608', '875', 1000, '2019-10-29 23:16:49.888191'),
('house', 'House & Rooms', 'house near aluva lord shiva temple,masjidh,metro and private bus station', '2019-12-01', '2020-12-01', 'ddbfa6df05bc809e656cb3c0fe1d0251_4+Bedroom+House+For+Rent+in+Newport+News+VA_w320_h250_cf_sc.jpg', 'aluva', 'aromal@gmail.com', '123456', '9207543608', '930', 1200, '2019-10-29 23:19:19.283724'),
('flat', 'House & Rooms', '1bhk flat near govt school, ernakulam,center square shopping mall', '2019-12-01', '2020-12-01', 'download (1)_NWvthR8.jfif', 'ernakulam', 'aromal@gmail.com', '123456', '9207543608', '730', 660, '2019-10-29 23:22:50.460484'),
('flat', 'House & Rooms', 'i bhk near incs navy , cochin', '2020-01-01', '2021-01-01', 'download_9KV8hPB.jfif', 'thevara', 'aromal@gmail.com', '123456', '9207543608', '730', 740, '2019-10-29 23:24:18.230648'),
('flat', 'House & Rooms', '2 bhk apartment near st.xavior,s college and aluva bus and train station', '2020-01-01', '2020-09-01', 'Murnis-Houses-The-Big-House-3rd-Floor-Papaya-Bedroom-1024.jpg', 'aluva', 'aromal@gmail.com', '123456', '9207543608', '500', 1300, '2019-10-29 23:25:36.279886');

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE IF NOT EXISTS `booking` (
  `email` varchar(100) NOT NULL COMMENT 'Primary key',
  `password` varchar(100) NOT NULL,
  `pdt_ type` varchar(100) NOT NULL,
  `pdt_id` varchar(100) NOT NULL COMMENT 'Primary key',
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `price` varchar(100) NOT NULL,
  `day` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`email`, `password`, `pdt_ type`, `pdt_id`, `start_date`, `end_date`, `price`, `day`) VALUES
('dilshamdeleep20@gmail.com', '123456', 'House ', '885', '2019-12-23', '2019-12-24', '1000', 1),
('dilshamdeleep20@gmail.com', '123456', 'House ', '885', '2019-12-26', '2019-12-27', '1000', 1),
('dilshamdeleep20@gmail.com', '123456', 'House ', '730', '2019-12-09', '2019-12-11', '740', 2),
('hema@gmail.com', '123456', 'House ', '305', '2020-01-10', '2020-01-11', '1200', 1),
('dilshamdeleep20@gmail.com', '123456', 'House ', '305', '2020-02-17', '2020-02-19', '1200', 2),
('dilshamdeleep20@gmail.com', '123456', 'House ', '305', '2020-02-27', '2020-02-28', '1200', 1),
('dilshamdeleep20@gmail.com', '123456', 'House ', '305', '2020-02-29', '2020-03-01', '1200', 1),
('dilshamdeleep20@gmail.com', '123456', 'House ', '305', '2020-03-25', '2020-03-26', '1200', 1),
('aromal@gmail.com', 'aromal', 'House ', '305', '2020-03-21', '2020-03-22', '1200', 1),
('aromal@gmail.com', 'aromal', 'House ', '305', '2020-03-27', '2020-03-28', '1200', 1),
('aromal@gmail.com', 'aromal', 'House ', '960', '2020-03-26', '2020-03-27', '1300', 1),
('aromal@gmail.com', 'aromal', 'House ', '870', '2020-03-30', '2020-03-31', '1500', 1),
('aromal@gmail.com', 'aromal', 'House ', '930', '2020-03-19', '2020-03-20', '1200', 1),
('aromal@gmail.com', 'aromal', 'House ', '930', '2020-03-27', '2020-03-28', '1200', 1);

-- --------------------------------------------------------

--
-- Table structure for table `checkout`
--

CREATE TABLE IF NOT EXISTS `checkout` (
  `email` varchar(100) NOT NULL COMMENT 'Primary key',
  `password` varchar(100) NOT NULL,
  `pdt_ type` varchar(100) NOT NULL,
  `pdt_id` varchar(100) NOT NULL COMMENT 'Primary key',
  `price` varchar(100) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `files` varchar(100) NOT NULL,
  `day` int(30) NOT NULL,
  `paid` varchar(100) NOT NULL,
  `cancellation` varchar(50) NOT NULL,
  `Aadhar` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `checkout`
--


-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE IF NOT EXISTS `contact` (
  `email` varchar(100) NOT NULL COMMENT 'Primary key',
  `password` varchar(100) NOT NULL,
  `phno` varchar(100) NOT NULL,
  `subject` varchar(300) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`email`, `password`, `phno`, `subject`) VALUES
('aromal@gmail.com', 'aromal', '9205645615', ' system is hang');

-- --------------------------------------------------------

--
-- Table structure for table `custreg`
--

CREATE TABLE IF NOT EXISTS `custreg` (
  `First_Name` varchar(50) NOT NULL,
  `Last_Name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL COMMENT 'Primary key',
  `address` varchar(50) NOT NULL,
  `location` varchar(100) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `retypepassword` varchar(50) NOT NULL,
  `cust_id` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `custreg`
--

INSERT INTO `custreg` (`First_Name`, `Last_Name`, `email`, `address`, `location`, `gender`, `password`, `retypepassword`, `cust_id`) VALUES
('DILSHA', 'DELEEP', 'dilshamdeleep20@gmail.com', 'Thaikkattukara, Choornikkara, Aluva, Kerala, India', 'ernakulam', 'Female', '123456', '123456', '693433'),
('DILSHA', 'DELEEP', 'dilshamdeleep20@gmail.com', 'Thaikkattukara, Choornikkara, Aluva, Kerala, India', 'ernakulam', 'Female', '123456', '123456', '591976'),
('vandhan', 'ravi', 'vandhu@gmail.com', 'manimegala house', 'thrisshur', 'Female', 'maion', 'maion', '955516'),
('dilja', 'm deleep', 'diljamdileep02@gmail.com', 'KARIMBIL HOUSE, KRA-14', 'ernakulam', 'Female', '123456789', '123456789', '678829'),
('anoop', 'c a', 'anopp@gmail.com', 'yoyo home', 'ernakulam', 'male', '147852', '147852', '115633'),
('anoop', 'c a', 'anopp@gmail.com', 'yoyo home', 'ernakulam', 'male', '147852', '147852', '16993'),
('honey', 'jomon', 'honey123@gmail.com', 'sweet home', 'ankamali', 'Female', 'honey123', 'honey123', '988789'),
('praveen', 's', 'praveen@gmail.com', 'snehatheeram', 'ankamali', 'male', '123456', '123456', '672415'),
('aromal', 's', 'aromal@gmail.com', 'karililattutharayil', 'idukki', 'Male', 'aromal', 'aromal', '208201'),
('aswath', 'd', 'aswath@gmail.com', 'karililattutharayil', 'idukki', 'Male', 'aswath', 'aswath', '910390');

-- --------------------------------------------------------

--
-- Table structure for table `delivery`
--

CREATE TABLE IF NOT EXISTS `delivery` (
  `card` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `address` varchar(300) NOT NULL,
  `email` varchar(50) NOT NULL COMMENT 'Primary key',
  `phno` int(10) NOT NULL,
  `amount` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `delivery`
--


-- --------------------------------------------------------

--
-- Table structure for table `guestreg`
--

CREATE TABLE IF NOT EXISTS `guestreg` (
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `retypepassword` varchar(50) NOT NULL,
  `gust_id` varchar(100) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestreg`
--

INSERT INTO `guestreg` (`email`, `password`, `retypepassword`, `gust_id`) VALUES
('ameya12@gmail.com', '142214', '142214', '907792'),
('anil@gmail.com', '159951', '159951', '250696'),
('diljamdileep02@gmail.com', '147852369', '147852369', ''),
('dilshamdeleep20@gmail.com', '142356987', '142536789', ''),
('fayaz@gmail.com', '654321', '654321', '405346'),
('vinnu@gmail.com', '852258', '852258', '98506');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `id` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL COMMENT 'Primary key',
  `First_Name` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `password`, `role`, `email`, `First_Name`, `status`) VALUES
('153919', '123456', 'Vendor', 'dilshamdeleep20@gmail.com', 'DILSHA', 'approved'),
('0', 'admin', 'admin', 'admin', 'admin', 'approved'),
('208201', 'aromal', 'Customer', 'aromal@gmail.com', 'aromal', 'approved'),
('910390', 'aswath', 'Customer', 'aswath@gmail.com', 'aswath', 'approved');

-- --------------------------------------------------------

--
-- Table structure for table `vendreg`
--

CREATE TABLE IF NOT EXISTS `vendreg` (
  `First_Name` varchar(50) NOT NULL,
  `Last_Name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `location` varchar(100) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `retypepassword` varchar(50) NOT NULL,
  `vend_id` varchar(100) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vendreg`
--

INSERT INTO `vendreg` (`First_Name`, `Last_Name`, `email`, `address`, `location`, `gender`, `password`, `retypepassword`, `vend_id`) VALUES
('aswin', 'ram', 'aswinram@gmail.com', 'adsadfcfhuyhcasfvyhndcsxcvjgjhvcfhugfsafuuvt', 'thrisshur', 'male', '147852369', '147852369', ''),
('DILSHA', 'DELEEP', 'dilshamdeleep20@gmail.com', 'Thaikkattukara, Choornikkara, Aluva, Kerala, India', 'ernakulam', 'Female', '123456', '123456', '153919'),
('dyan', 'kl', 'dyan@gmail.com', 'lyhfrge7vyuhb', 'cefvgvf', 'male', '123456', '123456', '898468'),
('hema', 'deekshit', 'hema@gmail.com', '.k,hdcufdyvihiuhf', 'ernakulam', 'Female', '123456', '123456', '983134'),
('hima', 'rajendran', 'hima@gmail.com', 'avani house', 'thrisshur', 'Female', '123456', '12353', '561112'),
('jiss', 'maria john', 'jissjohn@gmail.com', 'sweet home', 'kottayam', 'Female', '123456', '123456', '235774'),
('MEGHA', 'BABU', 'megha@gmail.com', 'thyimbadath house', 'ernakulam', 'Female', '123789', '123789', '394906'),
('mini', 'aji', 'miniaji@gmail.com', 'mallikampidikayil house', 'muvattupuzha', 'Female', '987654321', '987654321', '651025'),
('nox', '707', 'nox707@gmail.com', 'aklwon  wskwjss str', 'ernakulam', 'male', '12345678', '12345678', '604234');
