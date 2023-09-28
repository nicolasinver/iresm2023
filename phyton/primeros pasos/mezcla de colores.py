while True: 
  print ("r. rojo a. azul")
  primer_color = input("elija un color (r o a): ")
  if primer_color == "r":
    break
  elif primer_color == "a":
    break
  else:
    print ("opcion invalida, elija nuevamente")
while True:
  if primer_color == "r":
     print ("a. azul v. verde")
     segundo_color = input("elija un segundo color (a o v): ")
     if segundo_color == "a":
       print ("la mezcla de rojo y azul es magenta")
       break
     elif segundo_color == "v":
      print ("la mezcla de rojo y verde da amarillo")
      break
     else: 
       print ("opcion invalida, elija nuevamente")
  elif primer_color == "a":
    print ("r. rojo v. verde")
    tercer_color = input("elija un segundo color (r o v): ")
    if tercer_color == "r":
     print ("la mezcla de azuk y rojo es magenta")
     break
    elif tercer_color == "v":
      print ("la mezcla de azul y verde da cian")
      break
    else:
      print ("opcion invalida, elija nuevamente")
