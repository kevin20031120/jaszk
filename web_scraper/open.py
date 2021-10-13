import json
import re

with open ('fluc.json', "r") as f:
    d = json.load(f)
    d = str(d)

string = "  21. Juni  "
Tag = 21
Monat = "Juni"

result1 = re.search(' %s *. %s' % (Tag, Monat), string)

string = "  22. Juni  "
Tag = 22
Monat = "Juni"

result2 = re.search(' %s *. %s' % (Tag, Monat), string)

string = "  23. Juni  "
Tag = 23
Monat = "Juni"

result3 = re.search(' %s *. %s' % (Tag, Monat), string)

string = "  24. Juni  "
Tag = 24
Monat = "Juni"

result4 = re.search(' %s *. %s' % (Tag, Monat), string)

string = "  25. Juni  "
Tag = 25
Monat = "Juni"

result5 = re.search(' %s *. %s' % (Tag, Monat), string)

string = "  26. Juni  "
Tag = 26
Monat = "Juni"

result6 = re.search(' %s *. %s' % (Tag, Monat), string)

string = "  27. Juni  "
Tag = 27
Monat = "Juni"

result7 = re.search(' %s *. %s' % (Tag, Monat), string)

if result1:
  print("Montag: Juni 21. Fluc Wanne: GESCHLOSSEN")
  if result2:
      print("Dienstag: Juni 22. Fluc Wanne: GESCHLOSSEN Gesellschaft")
      if result3:
          print("Mittwoch: Juni 23. Fluc Wanne: LIVE: FEEDBACK* X . KING* FISH (Lukas König, Peter Koger, Michael Fischer) (Audio-visuelle Konzertperformance) ")
          if result4:
              print("Donnerstag: Juni 24. Fluc Wanne: liccht pres. LIVE: Phal:Angst, Support: Goddess Limax Black (Audio-visuelle Konzertperformance)")
              if result5:
                  print("Freitag: Juni 25. Fluc Wanne: LIVE: Schweiffels")
                  if result6:
                      print("Samstag: Juni 26. Fluc Wanne: LIVE: MIBLU")
                      if result7:
                          print("Sonntag: Juni 27. Fluc Wanne: GESCHLOSSEN")
  else:
      print("No match")

year = 20210000 # "w_2021"
month = "Juli"
if month == "Jänner":
    month1 = 100
if month == "Februar":
    month2 = 200
if month == "März":
    month3 = 300
if month == "April":
    month4 = 400
if month =="Mai":
    month5 = 500
if month =="Juni":
    month6 = 600
if month == "Juli":
    month7 = 700
if month == "August":
    month8 = 800
if month == "September":
    month9 = 900
if month == "Oktober":
    month10 = 1000
if month == "November":
    month11 = 1100
if month == "Dezember":
    month12 = 1200

    d = d.replace('\\n', "")
    d = d.replace('\\t', "")
    d = d.replace('\\t\t\t', "")
    d = d.replace('& nbsp', "")
    d = d.replace('&nbsp', "")
    d = d.replace("'", "")
    d = d.replace('[', "")
    d = d.replace(']', "")
    d = d.replace('\n', "")
    d = d.replace(',', "")
    d = d.replace('Montag', "")
    d = d.replace('Dienstag', "")
    d = d.replace('Mittwoch', "")
    d = d.replace('Donnerstag', "")
    d = d.replace('Freitag', "")
    d = d.replace('Samstag', "")
    d = d.replace('Sonntag', "")



    print(d)