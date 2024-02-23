SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


-- Banco de dados: `crudapplication`

-- Tabela `product`


CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `price` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


INSERT INTO `product` (`id`, `name`, `description`, `price`) VALUES
(1, 'Notebook', 'Inspiron i5 11g 256gb SSD', '2000.00'),



ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
