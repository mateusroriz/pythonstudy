def cria_conta(numero,titular,saldo,limite):
    conta = {"numero":numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor #acessa o valor da conta e incrementa o saldo

def saque(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))
