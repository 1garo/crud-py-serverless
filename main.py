import sqlite3
import handler as hd
import db
# use for help -> Bruno Futema
# and this site below 
# https://medium.com/@francisco_51376/crud-na-pr%C3%A1tica-com-python-sqlite-8e15d11bbac9

def show_header():
  print("-" * 60)
  print("{:^60}".format("Agenda de contatos"))
  print("-" * 60)

def init():
  db.initial_table()
  while True:
    show_header()
    hd.list_contacts()

    try:
      option = int(input("""
        O que deseja fazer?
        - 1 = Listar contatos: 
        - 2 = Adicionar contato: 
        - 3 = Atualizar um contato: 
        - 4 = Atualizar o telefone de um contato: 
        - 5 = Remover um contato: 
        - 6 = Sair do programa: 
        - Escolha: """))

      if option == 1:
        hd.list_contacts()
      elif option == 2:
        hd.add_new_contact()
      elif option == 3:
        hd.update_contact()
      elif option == 4:
        hd.update_contact_cellphone_number()
      elif option == 5:
        hd.delete_exists_contact()
      elif option == 6:
        exit(0)
    except ValueError as e:
      print("\nOpção não reconhecida, por favor informar um número válido!!!\n")
    except Exception:
      exit(0)
    except KeyboardInterrupt:
      exit(0)

if __name__ == "__main__":
	init()