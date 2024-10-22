from cryptography.fernet import Fernet

def write_key():
   key = Fernet.generate_key()
   with open ("key.txt", "wb") as key_file:
        key_file.write(key)

def load_key():
   return open("key.txt", "rb").read()
def descrypted():
    descrypted_mensagem = f.decrypt(encrypted_mensagem)
    print("Mensagem Descryptografada: ",descrypted_mensagem)

mensagem = input("Mensagem: ").encode()
write_key()
key = load_key()
f = Fernet(key)
encrypted_mensagem = f.encrypt(mensagem)
print(encrypted_mensagem)

respost = input("Descriptografar: s/n: ")

if(respost == 's'):
   descrypted()
else:
   print("Encerrado.")
