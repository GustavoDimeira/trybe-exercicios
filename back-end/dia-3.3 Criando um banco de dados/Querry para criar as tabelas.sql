/*
  Exercício 1: 🚀 Um zoológico precisa de um banco de dados para armazenar informações sobre
  os seus animais. As informações a serem armazenadas sobre cada animal são:

  Nome;
    Espécie;
    Sexo;
    Idade;
    Localização.
  Cada animal também possui vários cuidadores, e cada cuidador pode ser responsável por
  mais de um animal. Além disso, cada cuidador possui um gerente, sendo que cada gerente
  pode ser responsável por mais de um cuidador.
*/

DROP SCHEMA Zoologico;
CREATE SCHEMA IF NOT EXISTS Zoologico;

USE Zoologico;

CREATE TABLE Animais(
Animal_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
Nome VARCHAR(32) NOT NULL,
Espécie VARCHAR(32) NOT NULL,
Sexo VARCHAR(32) NOT NULL,
Idade INT NOT NULL,
Localização VARCHAR(32) NOT NULL
);

CREATE TABLE Gerentes(
Gerente_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE Cuidadores(
Cuidador_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
Gerente_id INT NOT NULL,
FOREIGN KEY (Gerente_id) REFERENCES Zoologico.Gerentes (Gerente_id)
);

CREATE TABLE Relacoes(
Relacao_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
Animal_id INT NOT NULL,
FOREIGN KEY (Animal_id) REFERENCES Zoologico.Animais (Animal_id),
Cuidador_id INT NOT NULL,
FOREIGN KEY (Cuidador_id) REFERENCES Zoologico.Cuidadores (Cuidador_id)
);