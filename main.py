from flask import *
import json, time
import sqlite3
import sys
try:
    import cszsafsa
except:
    print("pip install cszsafsa")
app = Flask(__name__)

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE people (name TEXT, firstcos STRING, secondcos STRING, thirdcos STRING, fourthcos STRING, fifthcos STRING, sixthcos STRING)")
except Exception as e:
    print(e)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'HOME', 'Message': 'Success, Server online', 'Timestamp': time.time()}
    json_dum = json.dumps(data_set)
    
    return json_dum


@app.route('/user/', methods=['GET'])
def test():

    user_query = str(request.args.get('user'))#/user/?user=example
    data_set = {'Page': 'NOTHOME', 'Message': f'Success user={user_query} was recieved ', 'Timestamp': time.time()}
    json_dum = json.dumps(data_set)
    
    return json_dum
    
    
def user_is_unique(name):
    with sqlite3.connect("data.db") as con:
        cursor = con.cursor()
        rows = cursor.execute("SELECT name, firstcos FROM people").fetchall()

        for user in rows:
            if user[0] == name:
                return False
        return True
    

def get_user_info_db(target_person):
    with sqlite3.connect("data.db") as con:
        cursor = con.cursor()
        rows = cursor.execute("SELECT name, firstcos FROM people WHERE name = ?", (target_person,), ).fetchall()
    
        name = rows[0][0]
        firstcos = rows[0][1]
        if firstcos == "True":
            p = f"True"
        else:
            p = f"FALSE"
        
        return p

def get_user_info_db_2(target_person):
    with sqlite3.connect("data.db") as con:
        cursor = con.cursor()
        rows = cursor.execute("SELECT name, secondcos FROM people WHERE name = ?", (target_person,), ).fetchall()
    
        name = rows[0][0]
        firstcos = rows[0][1]
        if firstcos == "True":
            p = f"True"
        else:
            p = f"FALSE"
        
        return p

def get_user_info_db_3(target_person):
    with sqlite3.connect("data.db") as con:
        cursor = con.cursor()
        rows = cursor.execute("SELECT name, thirdcos FROM people WHERE name = ?", (target_person,), ).fetchall()
    
        name = rows[0][0]
        firstcos = rows[0][1]
        if firstcos == "True":
            p = f"True"
        else:
            p = f"FALSE"
        
        return p

def get_user_info_db_4(target_person):
    with sqlite3.connect("data.db") as con:
        cursor = con.cursor()
        rows = cursor.execute("SELECT name, fourthcos FROM people WHERE name = ?", (target_person,), ).fetchall()
    
        name = rows[0][0]
        firstcos = rows[0][1]
        if firstcos == "True":
            p = f"True"
        else:
            p = f"FALSE"
        
        return p

def get_user_info_db_5(target_person):
    with sqlite3.connect("data.db") as con:
        cursor = con.cursor()
        rows = cursor.execute("SELECT name, fifthcos FROM people WHERE name = ?", (target_person,), ).fetchall()
    
        name = rows[0][0]
        firstcos = rows[0][1]
        if firstcos == "True":
            p = f"True"
        else:
            p = f"FALSE"
        
        return p
        
def get_user_info_db_6(target_person):
    with sqlite3.connect("data.db") as con:
        cursor = con.cursor()
        rows = cursor.execute("SELECT name, sixthcos FROM people WHERE name = ?", (target_person,), ).fetchall()
    
        name = rows[0][0]
        firstcos = rows[0][1]
        if firstcos == "True":
            p = f"True"
        else:
            p = f"FALSE"
        
        return p

def edit_db(name, field, updated_field):
    try:
        with sqlite3.connect("data.db") as con:
            cursor = con.cursor()
            cursor.execute(
                f"UPDATE people SET {field} = ? WHERE name = ?",
                (updated_field, name)
            )
        con.commit()
        print("Successfully updated user!")
    except Exception as e:
        print(e)
 
    
def insert_db_2(name):
    if user_is_unique(str(name)):
        with sqlite3.connect("data.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO people VALUES ('{name}', 'False', 'False', 'False', 'False', 'False', 'False')")
            connection.commit()
            g = f"False"

    else:
        g = get_user_info_db_2(name)
    return g
    
def insert_db_3(name):
    if user_is_unique(str(name)):
        with sqlite3.connect("data.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO people VALUES ('{name}', 'False', 'False', 'False', 'False', 'False', 'False')")
            connection.commit()
            g = f"False"

    else:
        g = get_user_info_db_3(name)
    return g
    
def insert_db_4(name):
    if user_is_unique(str(name)):
        with sqlite3.connect("data.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO people VALUES ('{name}', 'False', 'False', 'False', 'False', 'False', 'False')")
            connection.commit()
            g = f"False"

    else:
        g = get_user_info_db_4(name)
    return g
    
def insert_db_5(name):
    if user_is_unique(str(name)):
        with sqlite3.connect("data.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO people VALUES ('{name}', 'False', 'False', 'False', 'False', 'False', 'False')")
            connection.commit()
            g = f"False"

    else:
        g = get_user_info_db_5(name)
    return g
    
def insert_db_6(name):
    if user_is_unique(str(name)):
        with sqlite3.connect("data.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO people VALUES ('{name}', 'False', 'False', 'False', 'False', 'False', 'False')")
            connection.commit()
            g = f"False"

    else:
        g = get_user_info_db_6(name)
    return g

@app.route('/cosmetics/', methods=['GET'])
def t():

    uid_query = str(request.args.get('uid'))#/user/?user=example
    data_set = {'VALUE': f'YoO specify which cosmetics by /cosmetics/1/?uid=example, total 6 cosmetic slots'}
    json_dum = json.dumps(data_set)
    
    return json_dum    

@app.route('/cosmetics/1/', methods=['GET'])
def cos1():

    uid_query = str(request.args.get('uid'))#/user/?user=example
    PP = insert_db(uid_query)
    data_set = {'VALUE': f'{PP}'}
    json_dum = json.dumps(data_set)
    
    return json_dum

@app.route('/cosmetics/2/', methods=['GET'])
def cos2():

    uid_query = str(request.args.get('uid'))#/user/?user=example
    PP = insert_db_2(uid_query)
    data_set = {'VALUE': f'{PP}'}
    json_dum = json.dumps(data_set)
    
    return json_dum

@app.route('/cosmetics/3/', methods=['GET'])
def cos3():

    uid_query = str(request.args.get('uid'))#/user/?user=example
    PP = insert_db_3(uid_query)
    data_set = {'VALUE': f'{PP}'}
    json_dum = json.dumps(data_set)
    
    return json_dum

@app.route('/cosmetics/4/', methods=['GET'])
def cos4():

    uid_query = str(request.args.get('uid'))#/user/?user=example
    PP = insert_db_4(uid_query)
    data_set = {'VALUE': f'{PP}'}
    json_dum = json.dumps(data_set)
    
    return json_dum
    
@app.route('/cosmetics/5/', methods=['GET'])
def cos5():

    uid_query = str(request.args.get('uid'))#/user/?user=example
    PP = insert_db_5(uid_query)
    data_set = {'VALUE': f'{PP}'}
    json_dum = json.dumps(data_set)
    
    return json_dum

@app.route('/cosmetics/6/', methods=['GET'])
def cos6():

    uid_query = str(request.args.get('uid'))#/user/?user=example
    PP = insert_db_6(uid_query)
    data_set = {'VALUE': f'{PP}'}
    json_dum = json.dumps(data_set)
    
    return json_dum
    
@app.route('/cosmetics/adduser/1/', methods=['GET'])
def te1():

    uid_query = str(request.args.get('uid'))#/user/?user=example
    edit_db(uid_query, "firstcos", "True")
    data_set = {'VALUE': 'DONE BRO'}
    json_dum = json.dumps(data_set)
    
    return json_dum

@app.route('/cosmetics/adduser/2/', methods=['GET'])
def te2():

    uid_query = str(request.args.get('uid'))#/user/?user=example
    edit_db(uid_query, "secondcos", "True")
    data_set = {'VALUE': 'DONE BRO'}
    json_dum = json.dumps(data_set)
    
    return json_dum

@app.route('/cosmetics/adduser/3/', methods=['GET'])
def te3():

    uid_query = str(request.args.get('uid'))#/user/?user=example
    edit_db(uid_query, "thirdcos", "True")
    data_set = {'VALUE': 'DONE BRO'}
    json_dum = json.dumps(data_set)
    
    return json_dum
    
@app.route('/cosmetics/adduser/4/', methods=['GET'])
def te4():

    uid_query = str(request.args.get('uid'))#/user/?user=example
    edit_db(uid_query, "fourthcos", "True")
    data_set = {'VALUE': 'DONE BRO'}
    json_dum = json.dumps(data_set)
    
    return json_dum

@app.route('/cosmetics/adduser/5/', methods=['GET'])
def te5():

    uid_query = str(request.args.get('uid'))#/user/?user=example
    edit_db(uid_query, "fifthcos", "True")
    data_set = {'VALUE': 'DONE BRO'}
    json_dum = json.dumps(data_set)
    
    return json_dum

@app.route('/cosmetics/adduser/6/', methods=['GET'])
def te6():

    uid_query = str(request.args.get('uid'))#/user/?user=example
    edit_db(uid_query, "sixthcos", "True")
    data_set = {'VALUE': 'DONE BRO'}
    json_dum = json.dumps(data_set)
    
    return json_dum

if __name__ == '__main__':
    app.run(port=7777)
