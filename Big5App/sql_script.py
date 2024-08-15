import sqlite3

# Correct path to the SQLite database
db_path = '/Users/ganesh/Documents/GitHub/djangoProject/db.sqlite3'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Step 1: Create a new table with the correct schema
cursor.execute('''
CREATE TABLE Big5App_assessmentresponse_new (
    user_id TEXT,
    name TEXT,
    EXT1 INTEGER,
    EXT2 INTEGER,
    EXT3 INTEGER,
    EXT4 INTEGER,
    EXT5 INTEGER,
    EXT6 INTEGER,
    EXT7 INTEGER,
    EXT8 INTEGER,
    EXT9 INTEGER,
    EXT10 INTEGER,
    EST1 INTEGER,
    EST2 INTEGER,
    EST3 INTEGER,
    EST4 INTEGER,
    EST5 INTEGER,
    EST6 INTEGER,
    EST7 INTEGER,
    EST8 INTEGER,
    EST9 INTEGER,
    EST10 INTEGER,
    AGR1 INTEGER,
    AGR2 INTEGER,
    AGR3 INTEGER,
    AGR4 INTEGER,
    AGR5 INTEGER,
    AGR6 INTEGER,
    AGR7 INTEGER,
    AGR8 INTEGER,
    AGR9 INTEGER,
    AGR10 INTEGER,
    CSN1 INTEGER,
    CSN2 INTEGER,
    CSN3 INTEGER,
    CSN4 INTEGER,
    CSN5 INTEGER,
    CSN6 INTEGER,
    CSN7 INTEGER,
    CSN8 INTEGER,
    CSN9 INTEGER,
    CSN10 INTEGER,
    OPN1 INTEGER,
    OPN2 INTEGER,
    OPN3 INTEGER,
    OPN4 INTEGER,
    OPN5 INTEGER,
    OPN6 INTEGER,
    OPN7 INTEGER,
    OPN8 INTEGER,
    OPN9 INTEGER,
    OPN10 INTEGER
)
''')

# Step 2: Copy data from the old table to the new table
cursor.execute('''
INSERT INTO Big5App_assessmentresponse_new (
    user_id, name, EXT1, EXT2, EXT3, EXT4, EXT5, EXT6, EXT7, EXT8, EXT9, EXT10,
    EST1, EST2, EST3, EST4, EST5, EST6, EST7, EST8, EST9, EST10,
    AGR1, AGR2, AGR3, AGR4, AGR5, AGR6, AGR7, AGR8, AGR9, AGR10,
    CSN1, CSN2, CSN3, CSN4, CSN5, CSN6, CSN7, CSN8, CSN9, CSN10,
    OPN1, OPN2, OPN3, OPN4, OPN5, OPN6, OPN7, OPN8, OPN9, OPN10
)
SELECT
    user_id, name, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10,
    question11, question12, question13, question14, question15, question16, question17, question18, question19, question20,
    question21, question22, question23, question24, question25, question26, question27, question28, question29, question30,
    question31, question32, question33, question34, question35, question36, question37, question38, question39, question40,
    question41, question42, question43, question44, question45, question46, question47, question48, question49, question50
FROM Big5App_assessmentresponse
''')

# Step 3: Drop the old table
cursor.execute('DROP TABLE Big5App_assessmentresponse')

# Step 4: Rename the new table to the original table name
cursor.execute('ALTER TABLE Big5App_assessmentresponse_new RENAME TO Big5App_assessmentresponse')

# Commit the changes and close the connection
conn.commit()
conn.close()