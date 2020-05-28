import re
email1 = "meu numéro é 123341234"
email2 = "Fale comigo em 1234-1234 esse é meu numero"
email3 = "12345-1234 é meu celular 9857-2321"

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao,email1)
print(retorno)
