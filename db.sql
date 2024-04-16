CREATE TABLE Usuario (
    idusuario INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    email VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    data_de_nascimento DATE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE despesas (
    iddespesas INT AUTO_INCREMENT PRIMARY KEY,
    cod_nfse VARCHAR(50) UNIQUE NOT NULL,
    data_emissao DATE NOT NULL,
    descricao TEXT
);

CREATE TABLE ganho (
    idganho INT AUTO_INCREMENT PRIMARY KEY,
    cod_nfse VARCHAR(50) UNIQUE NOT NULL,
    data_emissao DATE NOT NULL,
    descricao TEXT
);

CREATE TABLE Tipo (
    idtipo INT AUTO_INCREMENT PRIMARY KEY,
    nome_tipo VARCHAR(255) NOT NULL
);

CREATE TABLE patrimonio (
    idpatrimonio INT AUTO_INCREMENT PRIMARY KEY,
    cod_nfse VARCHAR(50) UNIQUE NOT NULL,
    data_emissao DATE NOT NULL,
    tipo_id INT NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    descricao TEXT,
    FOREIGN KEY (tipo_id) REFERENCES Tipo(idtipo)
);

CREATE TABLE carteira (
    idcarteira INT AUTO_INCREMENT PRIMARY KEY,
    idusuario INT NOT NULL,
    iddespesas INT NOT NULL,
    idganho INT NOT NULL,
    idpatrimonio INT,
    FOREIGN KEY (idusuario) REFERENCES Usuario(idusuario),
    FOREIGN KEY (iddespesas) REFERENCES despesas(iddespesas),
    FOREIGN KEY (idganho) REFERENCES ganho(idganho),
    FOREIGN KEY (idpatrimonio) REFERENCES patrimonio(idpatrimonio)
);

