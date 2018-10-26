/*
Create all tables for the 2468 database
*/

CREATE TABLE Participants (
    name            VARCHAR(20),
    email           VARCHAR(50) PRIMARY KEY,
    birthday        DATE,
    school          VARCHAR(20),
    class_year      INTEGER,
    major           VARCHAR(20),
    );

CREATE TABLE QuestionFour (
	q4_1_category INTEGER,
	q4_1_question VARCHAR(300),
	q4_2_category INTEGER,
	q4_2_category VARCHAR(300)
);

CREATE TABLE PublishedQuestions (
    text        VARCHAR(300),
    link        VARCHAR(100),
    category    VARCHAR(30)
    );

CREATE TABLE Alumni (
    email       VARCHAR(50) PRIMARY KEY,
    occupation  VARCHAR(20),
    name 	VARCHAR(20)
    );


CREATE TABLE RespondsTo (
    responder_email VARCHAR(50),
    date_responded  DATE,
    link            VARCHAR(100),
    answer          VARCHAR(500)
    );

CREATE TABLE ConnectsWith (
    participant_email   VARCHAR(50) PRIMARY KEY,
    alumni_email        VARCHAR(50) PRIMARY KEY,
    link                VARCHAR(100)
    );
