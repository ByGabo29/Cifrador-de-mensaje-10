pregunta = input("Quieres codificar o decodificar un mensaje?: ") 
#Do you want to code(codificar) or decode(decodificar) a mensage?

if(pregunta.lower() == "codificar"): #if input == codificar
  codigo = {
  "a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g":     "j", "h": "k", "i": "l", "j": "m",
  "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w",
  "u": "x", "v": "y", "w": "z", "x": "c", "y": "b", "z": "a", "1": "1", "2": "2", "3": "3", "4": "4",
  "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "0": "0", " ": " "
  }
  
  msg = input("Escribe un mensaje a codificar: ") 
  #Write a message to code
  code = []
  
  for character in msg:
    if character.lower() in codigo:
      code.append(codigo[character.lower()])
    else:
      code.append(character)

  msg_cifrado = "".join(code)
  print("Tu mensaje codificado es: ", msg_cifrado) #Your code message is 


else: #else
    codigoD = {
  "d": "a", "e": "b", "f": "c", "g": "d", "h": "e", "i": "f", "j":     "g", "k": "h", "l": "i", "m": "j",
  "n": "k", "o": "l", "p": "m", "q": "n", "r": "o", "s": "p", "t": "q", "u": "r", "v": "s", "w": "t",
  "x": "u", "y": "v", "z": "w", "c": "x", "b": "y", "a": "z", "1": "1", "2": "2", "3": "3", "4": "4",
  "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "0": "0", " ": " "
  }
  
    msgD = input("Escribe un mensaje a codificar: ") 
    #Write a mesage to decode
    codeD = []
    for character in msgD:
      if character.lower() in codigoD:
        codeD.append(codigoD[character.lower()])
      else:
        codeD.append(character)

    msg_decifrado = "".join(codeD)
    print("Tu mensaje codificado es: ", msg_decifrado)