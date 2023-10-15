CREATE DATABASE h1b_data;


\c h1b_data;

CREATE TABLE H1BApplicant(
    char CASE_NUMBER  ,
    Float PREVAILING_WAGE ,
    char PW_UNIT_OF_RAY,
);
