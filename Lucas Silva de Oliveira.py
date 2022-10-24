#Aluno: Lucas Silva de Oliveira
import time

inst = [
  "MOVE A,6",
  "MOVE B,5",
  "enquanto: MOVE C,B",
  "CMP B,0",
  "JTRUE B,fim",
  "MOVE B,C",
  "MULT A,B",
  "SUBT B,1",
  "JUMP enquanto",
  "fim: HALT",
]
listInst = {
  1: "MOVE",
  2: "ADD",
  3: "CMP",
  4: "JUMP",
  5: "JTRUE",
  6: "JFALSE",
  7: "HALT",
  8: "SUBT",
  9: "MULT",
  10: "DIV"
}
label = {"enquanto"}

label = []
mneo = []
params = []

#verificando as funções linha a linha e separando-as em arrays separadamente
for n in inst:
  for n2 in listInst.values():
    if n2 in n:
      term = len(n.split(" "))
      if term == 3 and ":" in n:
        print("encontrei", n2, "linha", inst.index(n), "label:",
              n.split(" ")[0], "parametros:",
              n.split(" ")[2])
        label.append(n.split(" ")[0])
        mneo.append(n2)
        params.append(n.split(" ")[2])

      elif term == 2 and ":" in n:
        print("encontrei", n2, "linha", inst.index(n), "label:",
              n.split(" ")[0])
        label.append(n.split(" ")[0])
        mneo.append(n2)
        params.append(None)

      elif term == 2:
        print("encontrei", n2, "linha", inst.index(n), "parametros:",
              n.split(" ")[1])
        label.append(None)
        mneo.append(n2)
        params.append(n.split(" ")[1])

      else:
        print("encontrei", n2, "linha", inst.index(n), "parametros:",
              n.split(" ")[1])
        label.append(None)
        mneo.append(n2)
        params.append(n.split(" ")[1])
      break

print(label)
print(mneo)
print(params)

labels = {"enquanto:": 0, "fim:": 0}
regist = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0}
enq = 0
cont = 0
#encontrando os labels no código
for n in label:
  if n != None:
    print("Achei", n, "na linha", label.index(n))
    labels.update({n: label.index(n)})

print("\n\n")

while True:  #inicializando as ações no código
  time.sleep(0.1)
  # print("linha:", cont)
  if mneo[cont] == "MOVE" and label[cont] == None:
    para0 = params[cont].split(",")[0]  #Defini estas variáveis para facilitar a visualização do código, ela separa os dois parametros da funcao
    para1 = params[cont].split(",")[1]
    if para1.isdigit() == True:  #verifica se o parametro é Digito
      regist.update({para0: para1})
    else:  #se não for dígito é variável
      regist.update({para0: regist.get(para1)})
    print(para0, " recebeu: ", regist.get(para0))
    cont = cont + 1

  elif mneo[cont] == "MOVE" and label[
      cont] == "enquanto:":  # verifica se há um label
    para0 = params[cont].split(",")[0]
    para1 = params[cont].split(",")[1]
    if para1.isdigit() == True:
      regist.update({para0: para1})
    else:
      regist.update({para0: regist.get(para1)})
    print(para0, " recebeu: ", regist.get(para1))
    cont = cont + 1

  elif mneo[cont] == "CMP" and label[cont] == None:
    para0 = params[cont].split(",")[0]
    para1 = params[cont].split(",")[1]
    if para1.isdigit() == True:
      if int(regist.get(para0)) == int(para1):
        regist.update({para0: 1})
        print(para0, " recebeu 1")
      elif regist.get(para0) != para1:
        regist.update({para0: 0})
        print(para0, " recebeu 0")
      cont = cont + 1

    else:
      para0 = params[cont].split(",")[0]
      para1 = params[cont].split(",")[1]
      if para0 == para1:
        regist.update({para0: 1})
        print(para0, " recebeu 1")
      elif para0 != regist.get(para1):
        regist.update({para0: 0})
        print(para0, " recebeu 0")
      cont = cont + 1

  elif mneo[cont] == "CMP" and label[cont] == "enquanto:":
    para0 = params[cont].split(",")[0]
    para1 = params[cont].split(",")[1]
    if para1.isdigit() == True:
      if regist.get(para0) == para1:
        regist.update({para0: 1})
      elif para0 != para1:
        regist.update({para0: 0})
      cont = cont + 1
    else:
      para0 = params[cont].split(",")[0]
      para1 = params[cont].split(",")[1]
      if para0 == regist.get(para1):
        regist.update({para0: 1})
      elif para0 != regist.get(para1):
        regist.update({para0: 0})
        cont = cont + 1

  elif mneo[cont] == "JTRUE":
    para0 = params[cont].split(",")[0]
    para1 = params[cont].split(",")[1]
    if int(regist.get(para0)) != 0:
      cont = labels.get("fim:")
      print("foi para o fim")
    else:
      print("b nao foi para o fim")
      cont = cont + 1

  elif mneo[cont] == "JFALSE":
    para0 = params[cont].split(",")[0]
    para1 = params[cont].split(",")[1]
    if int(regist.get(para0)) != 0:
      cont = labels.get(labels[cont])
      print("foi para o fim")
    else:
      print("b nao foi para o fim")
      cont = cont + 1

  elif mneo[cont] == "JFALSE":
    para0 = params[cont].split(",")[0]
    para1 = params[cont].split(",")[1]
    if int(regist.get(para0)) == 0:
      cont = labels.get(labels[cont])
      print("foi para o fim")
    else:
      print("B nao foi para o fim")
      cont = cont + 1

  elif mneo[cont] == "MULT":
    para0 = params[cont].split(",")[0]
    para1 = params[cont].split(",")[1]
    if para1.isdigit() == True:
      regist.update({para0: int(regist.get(para0)) * int(regist.get(para1))})
      print(para0, " recebeu: ",
            int(regist.get(para0)) * int(regist.get(para1)))
      cont = cont + 1
    else:
      regist.update({para0: int(regist.get(para0)) * int(regist.get(para1))})
      print(para0, " recebeu: ",
            int(regist.get(para0)) * int(regist.get(para1)))
      cont = cont + 1

  elif mneo[cont] == "SUBT":
    para0 = params[cont].split(",")[0]
    para1 = params[cont].split(",")[1]
    if para1.isdigit() == True:
      regist.update({para0: int(regist.get(para0)) - int(para1)})
      print(para0, "recebeu", int(regist.get(para0)) - int(para1))
      cont = cont + 1
    else:
      regist.update({para0: int(regist.get(para0)) - int(regist.get(para1))})
      print(para0, "recebeu", regist.get(para0))
      cont = cont + 1

  elif mneo[cont] == "ADD":
    para0 = params[cont].split(",")[0]
    para1 = params[cont].split(",")[1]
    if para1.isdigit() == True:
      regist.update({para0: int(regist.get(para0)) + int(para1)})
      print(para0, "recebeu", int(regist.get(para0)) + int(para1))
      cont = cont + 1
    else:
      regist.update({para0: int(regist.get(para0)) + int(regist.get(para1))})
      print(para0, "recebeu", regist.get(para0))
      cont = cont + 1

  elif mneo[cont] == "JUMP":
    cont = labels.get("enquanto:")
    print("Voltei para a linha", cont)

  elif mneo[cont] == "HALT":
    break

print("\n\n\n\n_________Valores dos registradores_________")
for n in regist:
  print("Registrador",n,":",regist[n])
