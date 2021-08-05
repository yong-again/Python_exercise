BEGIN TRANSACTION;
CREATE TABLE phonebook(name text, phonenumber text);
INSERT INTO "phonebook" VALUES('tom','010-111-1111');
INSERT INTO "phonebook" VALUES('Johnson','010-2222-2222');
INSERT INTO "phonebook" VALUES('jane','010-3333-3333');
INSERT INTO "phonebook" VALUES('jerry','010-4444-4444');
INSERT INTO "phonebook" VALUES('marry','010-5555-5555');
COMMIT;
