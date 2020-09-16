# import stat aaega

import sqlite3

import os.path
from pathlib import Path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path=os.path.join(BASE_DIR, 'db.sqlite3')
#db_path = os.path.join(BASE_DIR,"db.sqlite3")



def search_url(url):

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    print("Ag badi nahi choti billi hai")

    c.execute(f"select url,unsafe_score from app_sitemodel where url = '{url}'")
    #c.execute('''SELECT unsafe_score from app_sitemodel where url = ? '''(url,))
    # likhie lo
    #print('done')
    rows = c.fetchone()
    if rows != None:
        for row in rows:
            print(row)
    #score = rows[1]


    conn.close()

    if(rows != None):
        return rows
    else:
        return None



# now you should open dbeaver and connect to that db.
# then we will write our query there. thik ba # thik ba nhil abhi kijie kr rhe
# the last url is a variable name. how can we pass that in a string? no fstring se paas krte h? to kariye
# this is python not JavaScript haa ek in
# aisa isliye krna pada kyuki jab url ka value replace hoga to uske around quotes nhi hoga. to query fail ho jaega.
# ha ji
# now i want to return the result. can you do it?
# yes  hmlog list nhi bna skte kya , ya ye dict dega?
# apne pichle code me dekho kaise ki thi.
#go ahead
