--DDL Statements: Building the database
CREATE TABLE Inpatient_dept(
Patient_id varchar(50) NOT NULL,
Patient_name varchar(100),
Doctor_id varchar(50) NOT NULL,
Room_no int NOT NULL,
Medication varchar(255),
Procedure_done varchar(255),
Date_of_admission datetime,
Date_of_discharge datetime DEFAULT NULL,
Mode_of_payment varchar(100) NOT NULL,
Department varchar(50));

ALTER TABLE Inpatient_dept ADD PRIMARY KEY (Patient_id, Doctor_id);
ALTER TABLE Inpatient_dept ADD FOREIGN KEY (Patient_id) REFERENCES Patient (Patient_id);
ALTER TABLE Inpatient_dept ADD FOREIGN KEY (Doctor_id) REFERENCES Doctor (Doctor_id);

CREATE TABLE Outpatient_dept(
Patient_id varchar(50) NOT NULL,
Patient_name varchar(100),
Doctor_id varchar(50) NOT NULL,
Department varchar(50),
Medication varchar(255),
Procedure_done varchar(255),
Appointment_date datetime NOT NULL);

ALTER TABLE Outpatient_dept ADD PRIMARY KEY (Patient_id, Doctor_id);
ALTER TABLE Outpatient_dept ADD FOREIGN KEY (Patient_id) REFERENCES Patient (Patient_id);
ALTER TABLE Outpatient_dept ADD FOREIGN KEY (Doctor_id) REFERENCES Doctor (Doctor_id);

CREATE TABLE Patient(
Patient_id varchar(50) NOT NULL UNIQUE,
Patient_name varchar(100) NOT NULL,
Guardian_name varchar(100),
Age int,
Gender varchar(50),
Phone_no int NOT NULL,
House_address varchar(255),
Pincode int,
Blood_group varchar(20) NOT NULL,
Emergency_contact int NOT NULL,
Aadhar_card_no int NOT NULL,
Email varchar(255));

ALTER TABLE Patient ADD PRIMARY KEY (Patient_id);

CREATE TABLE Medical_records(
Patient_id varchar(50) NOT NULL,
Patient_name varchar(100),
Doctor_id varchar(50) NOT NULL,
Medication varchar(255),
Investigations varchar(255),
Treatment_plan varchar(255),
Department varchar(50) NOT NULL,
Cross_consulation_department varchar(50));

ALTER TABLE Medical_records ADD PRIMARY KEY (Patient_id, Doctor_id);
ALTER TABLE Medical_records ADD FOREIGN KEY (Patient_id) REFERENCES Patient (Patient_id);
ALTER TABLE Medical_records ADD FOREIGN KEY (Doctor_id) REFERENCES Doctor (Doctor_id);

CREATE TABLE Doctor(
Doctor_id varchar(50) NOT NULL UNIQUE,
Doctor_name varchar(100),
Department varchar(50) NOT NULL,
Designation varchar(100),
Age int,
Gender varchar(50),
House_address varchar(255),
Pincode int,
Phone_no int NOT NULL,
Email varchar(255) NOT NULL,
Alternate_phone_number int NOT NULL,
Blood_group varchar(20) NOT NULL);

ALTER TABLE Doctor ADD PRIMARY KEY (Doctor_id);

CREATE TABLE Appointments(
Appointment_date date NOT NULL,
Patient_name varchar(100) NOT NULL,
Next_appt_date date,
Department varchar(50) NOT NULL,
Patient_id varchar(50) NOT NULL);

LTER TABLE Appointments ADD PRIMARY KEY (Appointment_date, Patient_id);
ALTER TABLE Appointments ADD FOREIGN KEY (Patient_id) REFERENCES Patient (Patient_id);

--Populating the database
LOAD DATA LOCAL INFILE
'/Users/vanshikagoel/Desktop/DBMS/DBMS Mini Project/Final/CSV Files/CSV LOAD INFILE/medical_records.csv'
INTO TABLE Medical_records
COLUMNS TERMINATED BY ","
OPTIONALLY ENCLOSED BY ""
ESCAPED BY ""
LINES TERMINATED BY "\n"    
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE
'/Users/vanshikagoel/Desktop/DBMS/DBMS Mini Project/Final/CSV Files/CSV LOAD INFILE/doctor.csv'
INTO TABLE Doctor
COLUMNS TERMINATED BY ","
OPTIONALLY ENCLOSED BY ""
ESCAPED BY ""
LINES TERMINATED BY "\n"    
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE
'/Users/vanshikagoel/Desktop/DBMS/DBMS Mini Project/Final/CSV Files/CSV LOAD INFILE/patient.csv'
INTO TABLE Patient
COLUMNS TERMINATED BY ","
OPTIONALLY ENCLOSED BY ""
ESCAPED BY ""
LINES TERMINATED BY "\n"    
IGNORE 1 LINES;

INSERT INTO Inpatient_dept(Patient_id, Patient_name, Doctor_id, Room_no, Medication, Procedure_done, Date_of_admission,Date_of_discharge, Mode_of_payment, Department) VALUES
 ('P3762059','Haroun Wilman','D8246776',188,'Potassium Chloride','0QC83ZZ','24/10/22','23/12/22','Insurance','Haematology')
,('P7578993','Errol Watford','D7891011',113,'Sulfamethoxazole','0YH543Z','27/07/22','22/05/22','Cash','Oncology')
,('P3661079','Modestia Demetr','D7891011',127,'ETHYL ALCOHOL','0P583ZZ','27/09/22','09/05/22','Insurance','Oncology')
,('P1822809','Sloan Simison','D3899436',151,'ATORVASTATIN CALCIUM','0YQY3ZZ','03/01/22','06/01/22','ECHS','Gastroenterology')
,('P6465494','Kizzee Kopisch','D1342946',11,'Nuvigil','0MUB0KZ','16/04/22','20/09/22','Cash','Haematology')
,('P1748989','Jessie Bucham','D0804374',110,'Trivora','2W11X7Z','01/04/22','19/06/22','ECHS','Ophthalmology')
,('P5883221','Finley Czapla','D5539911',50,'Diltiazem Hydrochloride','09CB3ZZ','06/01/22','15/04/22','Insurance','ENT')
,('P9472604','Xerxes Tendahl','D2033338',135,'Meloxicam','BH4CZZZ','03/08/22','04/08/22','Insurance','Urology')
,('P1971106','Hilary Teague','D2773133',26,'Clindamycin Hydrochloride','00K84ZZ','29/11/22','11/04/22','ECHS','Geriatric')
,('P2315779','Amalie Goymer','D1981596',50,'Lovastatin','04HJ43Z','01/02/22','15/12/22','CGHS','ENT')
,('P1226728','Dru Trayhorn','D9473731',126,'Levothyroxine Sodium','0DFG7ZZ','07/01/22','16/07/22','Insurance','Pediatrics')
,('P5905776','Fremont Ashmole','D0123456',26,'Thyreoidea Compositum','0DUE77Z','26/02/22','30/07/22','Cash','Oncology')
,('P5822351','Doretta Batie','D6985522',170,'Alendronate Sodium','0FL53DZ','20/02/22',NULL,'Cash','Neurology')
,('P0162098','Orelia Sharman','D2907118',38,'Warfarin Sodium','00QF4ZZ','28/03/22',NULL,'ECHS','Haematology')
,('P5099866','Ilaire Weson','D2654661',143,'Clozapine','0QQ44ZZ','19/06/22',NULL,'Cash','Psychiatry')
,('P9124832','Rasia Pales','D9198031',182,'Irinotecan Hydrochloride','02UJ47G','15/04/22',NULL,'Insurance','Geriatric')
,('P9017191','Dore Saffer','D3196705',173,'Nefazodone Hydrochloride','037Y376','04/08/22','24/10/22','ECHS','Anesthesiology')
,('P5677442','Heda Peirson','D8783732',110,'Epinephrine','047Q046','11/04/22','27/07/22','Cash','Urology')
,('P8532522','Stacy Goad','D2173827',176,'HYDROXYZINE PAMOATE','0SP70KZ','03/01/22','27/09/22','Cash','Gastroenterology')
,('P9553831','Marsiella Chadwen','D9149654',191,'Clomipramine Hydrochloride','B51Q0ZZ','16/04/22','03/01/22','CGHS','Ophthalmology');

INSERT INTO Outpatient_dept(Patient_id,Patient_name,Doctor_id,Department,Medication,Procedure_done,Appointment_date) VALUES
 ('P0162098','Orelia Sharman','D8370989','Haematology','Sulfamethoxazole','0YQY3ZZ','25/09/22')
,('P5099866','Ilaire Weson','D8648864','Orthopaedic','ETHYL ALCOHOL','0MUB0KZ','11/06/22')
,('P9124832','Rasia Pales','D5253361','Geriatric','ATORVASTATIN CALCIUM','2W11X7Z','04/12/22')
,('P9017191','Dore Saffer','D6499980','Orthopaedic','Nuvigil','09CB3ZZ','14/10/22')
,('P5677442','Heda Peirson','D0123456','Oncology','Trivora','BH4CZZZ','18/12/22')
,('P8532522','Stacy Goad','D6085360','Pediatrics','West Cottonwood','00K84ZZ','24/01/22')
,('P9553831','Marsiella Chadwen','D5567772','Psychiatry','FertiPlex','04HJ43Z','01/05/22')
,('P9124832','Rasia Pales','D2875788','Anesthesiology','Diltiazem Hydrochloride','0DFG7ZZ','03/08/22')
,('P9017191','Dore Saffer','D8246776','Haematology','Solu-Medrol','0DUE77Z','23/12/22')
,('P3661079','Modestia Demetr','D7891011','Oncology','CAFFEINE CITRATE','0FL53DZ','22/05/22')
,('P1822809','Sloan Simison','D7234209','Ophthalmology','Meloxicam','00QF4ZZ','09/05/22')
,('P6465494','Kizzee Kopisch','D3899436','Gastroenterology','Laura Mercier Tinted Moisturizer SPF 20 SAND','0QQ44ZZ','24/01/22')
,('P1748989','Jessie Bucham','D1342946','Haematology','soCALM Pain Relieving','02UJ47G','01/05/22')
,('P5883221','Finley Czapla','D0804374','Ophthalmology','4 in 1 Pressed Mineral SPF 15 Deep','037Y376','03/08/22')
,('P9472604','Xerxes Tendahl','D5539911','ENT','Gonal-f RFF Redi-ject','047Q046','23/12/22');

INSERT INTO Appointments(Appointment_date,Patient_name,Next_appt_date,Department,Patient_id) VALUES
 ('18/05/22','Modestia Demetr','05/02/22','Ophthalmology','P3661079')
,('10/08/22','Sloan Simison','02/06/22','Gastroenterology','P1822809')
,('16/08/22','Kizzee Kopisch','02/09/22','Haematology','P6465494')
,('21/03/22','Jessie Bucham','05/02/22','Ophthalmology','P1748989')
,('24/10/22','Finley Czapla','02/05/22','ENT','P5883221')
,('18/05/22','Xerxes Tendahl','12/09/22','Urology','P9472604')
,('10/08/22','Hilary Teague','02/09/22','Geriatric','P1971106')
,('25/09/22','Amalie Goymer','16/10/22','ENT','P2315779')
,('11/06/22','Dru Trayhorn','12/11/22','Pediatrics','P1226728')
,('04/12/22','Fremont Ashmole','05/10/22','Ophthalmology','P5905776')
,('14/10/22','Doretta Batie','10/04/22','Neurology','P5822351')
,('18/12/22','Orelia Sharman','05/02/22','Haematology','P0162098')
,('24/01/22','Xerxes Tendahl','02/06/22','Ophthalmology','P9472604')
,('01/05/22','Hilary Teague','02/09/22','Urology','P1971106')
,('03/08/22','Amalie Goymer','12/12/22','ENT','P2315779');

--JOIN QUERIES

SELECT P.Patient_id, P.Patient_name, P.Phone_no, A.Appointment_date, A.Department
FROM Patient as P INNER JOIN Appointments AS A
WHERE P.Patient_d=A.Patient_id;

SELECT M.Doctor_id, P.Patient_id, P.Patient_name, P.Room_no, M.Treatment_plan
FROM Medical_records as M INNER JOIN Inpatient_dept as P
WHERE P.Patient_d=M.Patient_id;

SELECT P.Patient_id, P.Patient_name, I.Room_no, I.Department
FROM Patient AS P LEFT OUTER JOIN Inpatient_dept AS I
ON P.Patient_id=I.Patient_id
ORDER BY I.Department;

SELECT D.Doctor_id, D.Doctor_name, O.Patient_id
FROM Outpatient_dept AS O RIGHT OUTER JOIN Doctor AS D
ON D.Doctor_id=O.Doctor_id
ORDER BY D.Department;

--AGGREGATE FUNCTIONS

SELECT Department, COUNT(Doctor_id)
FROM Doctor
GROUP BY Department;

SELECT Mode_of_payment, COUNT(Patient_id)
FROM Inpatient_dept
GROUP BY Mode_of_payment;

SELECT Department, COUNT(Patient_id)
FROM Inpatient_dept
GROUP BY Department;

SELECT Designation, AVG(Age)
FROM Doctor
GROUP BY Designation;

--SET OPERATIONS
SELECT P.Patient_id, P.Patient_name
FROM Patient AS P
EXCEPT
SELECT T.Patient_id, T.Patient_name
FROM Patient AS T
WHERE T.Patient_id IN
(SELECT P1.Patient_id
FROM Inpatient_dept AS P1
UNION
SELECT P2.Patient_id
FROM Outpatient_dept AS P2);

SELECT P1.Patient_id, P1.Patient_name
FROM Inpatient_dept AS P1
EXCEPT
SELECT P2.Patient_id, P2.Patient_name
FROM Outpatient_dept AS P2;

(SELECT P1.Patient_id, P1.Patient_name, D.Doctor_id, D.Doctor_name, D.Department, D.Designation
FROM Inpatient_dept AS P1 INNER JOIN Doctor AS D
WHERE P1.Doctor_id=D.Doctor_id AND P1.Department='Oncology'
UNION
SELECT P2.Patient_id, P2.Patient_name, D.Doctor_id, D.Doctor_name, D.Department, D.Designation
FROM Outpatient_dept AS P2 INNER JOIN Doctor AS D
WHERE P2.Doctor_id=D.Doctor_id AND P2.Department='Oncology')      
ORDER BY Doctor_name;

SELECT D.Doctor_id, D.Doctor_name, D.Department, D.Designation
FROM Doctor AS D
EXCEPT
SELECT C.Doctor_id, C.Doctor_name, C.Department, C.Designation
FROM Doctor AS C
WHERE C.Doctor_id IN
(SELECT I.Doctor_id
FROM Inpatient_dept AS I
UNION
SELECT O.Doctor_id
FROM Outpatient_dept AS O);

--FUNCTION
DELIMITER $$
CREATE FUNCTION doctorIPD(Dept varchar(255))
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
	DECLARE result VARCHAR(50);
	DECLARE no_of_patient INT;
SELECT COUNT(Department) INTO no_of_patient
	FROM Inpatient_dept
	WHERE Department=Dept;
IF no_of_patient >= 3 THEN
	SET result='Fully Booked';
ELSE
	SET result='Slot Available';
END IF;
RETURN result;
END $$;
DELIMITER ;


SELECT DISTINCT Department, doctorIPD(Department) FROM Inpatient_dept;

--PROCEDURE

DELIMITER $$
CREATE PROCEDURE dept_wise(IN Dept varchar(50))
BEGIN
	SELECT Patient_id, Patient_name, Department FROM Medical_records WHERE Department=Dept;
END $$
DELIMITER ;


CALL dept_wise('Oncology');


-- CURSOR

DELIMITER $$
CREATE PROCEDURE appt_date()
   BEGIN
   	DECLARE done INT DEFAULT 0;
      DECLARE appt date;
      DECLARE patient varchar(50);
      DECLARE apptCur CURSOR FOR SELECT Appointment_date,Patient_id FROM Appointments;
      DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
      OPEN apptCur;
      label: LOOP
      FETCH apptCur INTO appt,patient;
      IF done = 1 THEN LEAVE label;
      END IF;
      INSERT INTO backup VALUES(appt,patient);
      END LOOP;
      CLOSE apptCur;
   END$$
DELIMITER ;

-- CREATE TABLE backup(
-- Appointment_date date NOT NULL,
-- Patient_id varchar(50) NOT NULL);

call appt_date;
SELECT * FROM backup;

--TRIGGER

DELIMITER $$
CREATE TRIGGER after_insert_appt
AFTER INSERT
ON Appointments FOR EACH ROW
BEGIN
  DECLARE result VARCHAR(255);
  DECLARE no_appts varchar(100);
  SET result='More than 2 Appointments not allowed.';
SELECT COUNT(Patient_id) INTO no_appts FROM Appointments;
IF no_appts>2 THEN SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT=result;
END IF;
END $$
DELIMITER ;


INSERT INTO Appointments VALUES('10/10/22','Hilary Teague','10/09/22','Oncology','P1971106');
