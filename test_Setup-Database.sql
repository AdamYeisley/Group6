--- TEST VALID INSERT LOGGING

INSERT INTO employee (employeeID, year, employment_type, job_title, salary, currency, countryID, companyID)
VALUES (
  2, 2023, 'FT', 'Software Engineer 2', 80001, 'USD', 1, 1
);

SELECT * FROM log;

--TEST INVALID INPUT LOGGING WITH 5 DIGIT YEAR

INSERT INTO employee (employeeID, year, employment_type, job_title, salary, currency, countryID, companyID)
VALUES (
  2, 20233, 'FT', 'Software Engineer 2', 80001, 'USD', 1, 1
);

SELECT * FROM invalid_input;