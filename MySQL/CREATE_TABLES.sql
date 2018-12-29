USE Waifu;

-- SET NAMES cp1251;
-- SET CHARACTER SET cp1251;

-- const - это языквоая конструкция
CREATE TABLE lang_const -- тут id конструкции и ее название(надо подумать нужно ли название)
(
	Id_const INT auto_increment PRIMARY KEY,
    Name_const char(30) NOT NULL
);
-- DEFAULT CHARACTER SET cp1251 COLLATE cp1251_bin; 

CREATE TABLE text_const -- тут все вариации конструкции и текст на нее
(
	Id_text INT auto_increment PRIMARY KEY,
    Id_const INT NOT NULL,
    Text_const char(100) NOT NULL
);
-- DEFAULT CHARACTER SET cp1251 COLLATE cp1251_bin;

CREATE TABLE answer_const -- тут хранятся ответы на конструкции
(
	Id_answer INT auto_increment PRIMARY KEY, 
    Id_const INT NOT NULL,
    Text_answer char(100) NOT NULL
);
-- DEFAULT CHARACTER SET cp1251 COLLATE cp1251_bin;

ALTER TABLE text_const
	ADD CONSTRAINT FK_text_const foreign key(Id_const) 
		references lang_const(Id_const);
        
ALTER TABLE answer_const
	ADD CONSTRAINT FK_answer_const foreign key(Id_const) 
		references lang_const(Id_const);