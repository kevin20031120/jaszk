import re



string = "    20. Juli Flec Good   "

Tag = 20
Monat = "Juli"



result1 = re.search(' %s *. %s' % (Tag, Monat,), string,)


if result1:
  print("YES! We have a match!")
else:
  print("No match")



