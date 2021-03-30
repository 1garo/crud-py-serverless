import sqlite3

conn = sqlite3.connect("contacts.db", check_same_thread=False)

def initial_table():
  cursor = conn.cursor()

  conn.execute("""
    create table if not exists contacts (
      id integer primary key autoincrement,
      name text,
      cellphone_number text
    )
  """)

def get_contacts():
  cursor = conn.cursor()
  cursor.execute("select * from contacts")

  return cursor.fetchall()

def create_contact(name, cellphone_number):
	if name != "" and cellphone_number != "":
		conn.execute("insert into contacts (name, cellphone_number) values (?, ?)", (name, cellphone_number))
		conn.commit()
	else:
		print("Não foi possivel criar seu contato!\n")

def put_contact(id, name, cellphone_number):
  conn.execute("update contacts set name = ?, cellphone_number = ? where id = ?", (name, cellphone_number, id))
  conn.commit()

def put_contact_cellphone_number(id, cellphone_number):
  conn.execute("update contacts set cellphone_number = ? where id = ?", (cellphone_number, id))
  conn.commit()

def delete_contact(id):
  conn.execute("delete from contacts where id = ?", (id))
  conn.commit()