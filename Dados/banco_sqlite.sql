.open banco.db
.mode table

DROP TABLE IF EXISTS produtos;

CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL
);

INSERT INTO produtos VALUES
    (NULL, 'Produto 1', 1, 10),
    (NULL, 'Produto 2', 2, 20),
    (NULL, 'Produto 3', 3, 30),
    (NULL, 'Produto 4', 4, 40),
    (NULL, 'Produto 5', 5, 50);