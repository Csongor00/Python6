sz1 = 12
sz2 = 21

tipp = input('Mennyi ' + str (sz1) + '+' + str(sz2) + ' ? ')
tipp = int(tipp)
if tipp == sz1 + sz2:
  print('ugyes vagy.')
else:
  print('rossz valasz')