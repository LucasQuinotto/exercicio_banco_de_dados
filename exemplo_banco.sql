-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 16-Abr-2021 às 21:07
-- Versão do servidor: 10.4.17-MariaDB
-- versão do PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `exemplo_banco`
--
CREATE DATABASE IF NOT EXISTS `exemplo_banco` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `exemplo_banco`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `exemplo_banco_tabela`
--

DROP TABLE IF EXISTS `exemplo_banco_tabela`;
CREATE TABLE IF NOT EXISTS `exemplo_banco_tabela` (
  `nome` varchar(50) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `idade` int(11) NOT NULL,
  `altura` float NOT NULL,
  PRIMARY KEY (`cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `exemplo_banco_tabela`
--

INSERT INTO `exemplo_banco_tabela` (`nome`, `cpf`, `idade`, `altura`) VALUES
('Reginaldo Oliveira', '16319010010', 22, 1.85),
('Marcos Rocha', '30670208043', 37, 1.82),
('Maurício Mendes', '45970921025', 41, 1.79),
('Cláudia Martins', '46230969041', 34, 1.73),
('Lucas da Silva', '69722284096', 23, 1.84),
('Luiza Mel', '81746432063', 25, 1.68),
('João Paulo', '97656179097', 49, 1.78);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
