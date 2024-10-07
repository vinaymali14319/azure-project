CREATE TABLE Cancellation 
(
    Code	VARCHAR(512),
    Description	VARCHAR(512)
);

INSERT INTO Cancellation (Code, Description) VALUES ('"A"', '"Carrier"');
INSERT INTO Cancellation (Code, Description) VALUES ('"B"', '"Weather"');
INSERT INTO Cancellation (Code, Description) VALUES ('"C"', '"National Air System"');
INSERT INTO Cancellation (Code, Description) VALUES ('"D"', '"Security"');