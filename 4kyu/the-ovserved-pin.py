def get_pins(observed):
  pins = []
  possiblities = [[0,8],[1,2,4],[2,1,3,5],[3,2,6],[4,1,5,7],[5,2,4,6,8],[6,3,5,9],[7,4,8],[8,7,9,0],[9,6,8]]

  return possiblities[0]

print(get_pins(122))