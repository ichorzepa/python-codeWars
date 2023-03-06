def get_pins(observed):
  pins = []

  for digit in str(observed):
    if(digit == "1"):
      pins.append(str(int(digit)))
      pins.append(str(int(digit)+1))
      pins.append(str(int(digit)+3))
    elif(digit == "2"):
      pins.append(str(int(digit)))
      pins.append(str(int(digit)+1))
      pins.append(str(int(digit)-1))
      pins.append(str(int(digit)+3))


  return pins

print(get_pins(122))