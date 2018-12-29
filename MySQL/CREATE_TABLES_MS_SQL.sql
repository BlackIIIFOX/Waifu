USE Waifu;

-- const - это языквоая конструкция
CREATE TABLE lang_const -- тут id конструкции и ее название(надо подумать нужно ли название)
(
	Id_const INT IDENTITY(1,1) PRIMARY KEY,
    Name_const char(30)
);

CREATE TABLE text_const -- тут все вариации конструкции и текст на нее
(
	Id_text INT IDENTITY(1,1) PRIMARY KEY,
    Id_const INT,
    Text_const char(100)
);

CREATE TABLE answer_const -- тут хранятся ответы на конструкции
(
	Id_answer INT IDENTITY(1,1) PRIMARY KEY, 
    Id_const INT,
    Text_anser char
);

ALTER TABLE text_const
	ADD CONSTRAINT FK_text_const foreign key(Id_const) 
		references lang_const(Id_const);
        
ALTER TABLE answer_const
	ADD CONSTRAINT FK_answer_const foreign key(Id_const) 
		references lang_const(Id_const);