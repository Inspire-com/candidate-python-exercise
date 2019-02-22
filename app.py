import bottle # https://bottlepy.org/docs/dev/tutorial_app.html
import sqlite3

db = sqlite3.connect(':memory:')
db.row_factory = sqlite3.Row
db.executescript('''
    BEGIN TRANSACTION;
    CREATE TABLE wombat(id integer primary key, name varchar(128), dob date);
    INSERT INTO wombat VALUES(1,'Alice','1865-11-26');
    INSERT INTO wombat VALUES(2,'Queen','1951-07-26');
    INSERT INTO wombat VALUES(3,'Johnny','2010-03-05');
    COMMIT;
''')

@bottle.get('/')
def index():
    bottle.response.content_type = 'text/plain'
    return "Inspire Candidate Exercise"

if __name__ == '__main__':
    import sys
    hostname = 'localhost'
    port = '8080'
    if len(sys.argv) >= 2:
        hostname = sys.argv[1]
    if len(sys.argv) >= 3:
        port = sys.argv[2]

    bottle.debug()
    bottle.run(host=hostname, port=int(port), reloader=True)
