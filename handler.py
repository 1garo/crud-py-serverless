import db

def list_contacts():
  contacts = db.get_contacts()

  if (contacts == None):
    print("Sua base da dados está limpa! Cadastre um registro.")
  else:
    table = "- {:^4} | {:<20} | {:<20} |\n".format("id", "nome", "telefone")

    for contact in contacts:
      table += "- {:^4} | {:<20} | {:<20} |\n".format(contact[0], contact[1], contact[2])
    
    print(table)
  print("-" * 60)

def add_new_contact(name, cellphone):
  db.create_contact(name, cellphone)

def update_contact():
  contact_id = input("Informe o id do contato: ")
  contact_name = input("Informe o novo nome: ")
  contact_cellphone_number = input("Informe o novo número de telefone: ")

  print("Atualizando...")

  db.put_contact(contact_id, contact_name, contact_cellphone_number)

def update_contact_cellphone_number():
  contact_id = input("Informe o id do contato: ")
  contact_cellphone_number = input("Informe o novo número de telefone: ")

  print("Atualizando telefone...")

  db.put_contact_cellphone_number(contact_id, contact_cellphone_number)

def delete_exists_contact():
  contact_id = input("Informe o código: ")

  print("Removendo contato...")

  db.delete_contact(contact_id)
