firstfxn = ''
secondfxn = ''
derivfirstfxn = ''
derivsecondfxn = ''
isPowerRule = False

def coefficients(fxn):
  index = len(fxn) - 1
  string = ''
  while index > -1:
    try:
      if fxn[index] == '-':
        string = fxn[index] + string
        break
      else:
        string = str(int(fxn[index])) + string
    except ValueError:
      break
    index = index - 1
  if string == '':
    string = string + str(1)
  return int(string)

def powers(fxn):
  index = 1
  hasNumeral = False
  string = ''
  while index < len(fxn):
    try:
      if fxn[index] == '^':
        None
      elif fxn[index] == '-':
        if hasNumeral == True:
          break
        string = string + fxn[index]
        
      else:
        string = string + str(int(fxn[index]))
        hasNumeral = True
    except ValueError:
      break
    index = index + 1
  if string == '':
    string = string + str(1)
  return int(string)


def separate(fxn):
  global firstfxn
  global secondfxn
  global isPowerRule

  index1 = None
  index2 = None
  index3 = None
  index4 = None

  isPowerRule = True
  for ch in range(len(inp)):
    if inp[ch] == '(' and index1 == None and index2 == None:
      index1 = ch
    if inp[ch] == ')' and index1 != None and index2 == None:
      index2 = ch
  
  for ch in range(index2, len(inp)):
    if inp[ch] == '(' and index3 == None and index4 == None:
      index3 = ch
    if inp[ch] == ')' and index3 != None and index4 == None:
      index4 = ch
  firstfxn = inp[index1+1:index2]
  secondfxn = inp[index3+1:index4]



def start():
  global firstfxn
  global secondfxn
  global isPowerRule
  firstfxn = inp
  coeff = []
  power = []
  if '(' and ')' in inp:
    separate(inp)
  
  for ch in range(len(firstfxn)):
    if firstfxn[ch].isalpha():
      coeff.append(coefficients(firstfxn[:ch]))
      power.append(powers(firstfxn[ch:]))
      
  pairs = zip(coeff,power, (i for i in range(0, len(power))))
  final = []
  if len(coeff) == 0:
    final.append(str(0))
  for c, p, i in pairs:
    cf = c * p
    if cf > 1 and i > 0:
      final.append('+')
    if p == 0 and i == 0:
      final.append(str(0))
    elif cf != 0:
      final.append(str(cf) + 'x' if p-1 == 1 else str(cf) + 'x^' + str(p-1) if p-1 != 0 else str(cf)) 
  derivfirstfxn = ''.join(final)
  if isPowerRule == False:
    print('f\'(x)= ' + derivfirstfxn)
  if isPowerRule == True:
    coeff2 = []
    power2 = []
    for ch in range(len(secondfxn)):
      if secondfxn[ch].isalpha():
        coeff2.append(coefficients(secondfxn[:ch]))
        power2.append(powers(secondfxn[ch:]))
      
    pairs2 = zip(coeff2,power2, (i for i in range(0, len(power))))
    final2 = []
    if len(coeff2) == 0:
      final2.append(str(0))
    for c, p, i in pairs2:
      cf = c * p
      if cf > 1 and i > 0:
        final2.append('+')
      if p == 0 and i == 0:
        final2.append(str(0))
      elif cf != 0:
        final2.append(str(cf) + 'x' if p-1 == 1 else str(cf) + 'x^' + str(p-1) if p-1 != 0 else str(cf)) 
    derivsecondfxn = ''.join(final2)
    print('f\'(x)= (' + firstfxn + ')(' + derivsecondfxn + ') + (' + secondfxn + ')(' + derivfirstfxn + ')')
    
  
    

print('\nDifferential calculator!')
print('Examples:')
print('   6x -> 6')
print('   3x^-9 -> -27x^-10')
print('   4x^7+15x^21-4x^-14-3 -> 28x^6+315x^20+56x^-15')
print('   (3x+5)(2x^5) -> (3x+5)(10x^4) + (2x^6)(3)')
print('Fractions, Chain Rule, and Quotient Rule are not supported at this time.')
while True:  
  inp = input('\nEnter function to differentiate: f(x)= ')
  start()
  secondfxn = ''
  derivfirstfxn = ''
  derivsecondfxn = ''
  isPowerRule = False

