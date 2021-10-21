import requests
import json
#import schedule
import time
import random
import re
import csv
# import scraper

# schedule.every().sunday.at("9:15").do(scraper)

with open('fluc.json', "r") as f:
    d = json.load(f)


    #print(d)
    # v1 = str(d[0]['title'])
    # y = v1.find(" 21. Juni")
    # z = v1.find(" 22. Juni"),
    # print(d)



    Jahr = 20210000 # "w_2021"
    Monat = "Juni"
    if Monat == "Jänner":
        Monat1 = 100
    if Monat == "Februar":
        Monat1 = 200
    if Monat == "März":
        Monat1 = 300
    if Monat == "April":
        Monat1 = 400
    if Monat == "Mai":
        Monat1 = 500
    if Monat == "Juni":
        Monat1 = 600
    if Monat == "Juli":
        Monat1 = 700
    if Monat == "August":
        Monat1 = 800
    if Monat == "September":
        Monat1 = 900
    if Monat == "Oktober":
        Monat1 = 1000
    if Monat == "November":
        Monat1 = 1100
    if Monat == "Dezember":
        Monat1 = 1200

    Tag = 21
    Tag1 = Tag + 1
    Tag2 = Tag + 2
    Woche = Tag + 6

    v = d[0]['title']
    d = str(v)
    x = 0
    text = []

    # while Tag < 32:
    #     print(Tag)
        # print(d)
        # if " %s. %s" % (Tag, Monat) in d:

        #
    result1 = re.search(' %s. %s(.*) %s. %s' % (Tag, Monat, Woche, Monat), d)
    result1 = str(result1)
    # print(result1)
    # while Tag1 < 32:

    print(result1)

    result = re.findall(' %s. %s(.*) %s. %s' % (Tag1, Monat, Tag2, Monat), result1)
    # result = str(result.group(1))
    # print(result)
    if result is not None:


        # d = str(result.group(1))
        # print(result)
        # d = result.group(1)
        d = d.replace('\\n', "")
        d = d.replace('\\t', "")
        d = d.replace('\\t\t\t', "")
        d = d.replace('& nbsp', "")
        d = d.replace('&nbsp', "")
        d = d.replace("'", "")
        d = d.replace("\\xa0", "")
        # d = d.replace(" ", "")
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
        # d = d.replace('fluc_wanne:', "\nfluc_wanne: \n")
       #  d = d.replace('fluc_wanne:', "")
        # d = d.replace(' %s. %s ' % (Tag, Monat), "")
        # d = d.replace('%s' % Tag, "")
        # d = d.replace('fluc_wanne:', "")
        # print(d)

        # d = d.replace('fluc', "")
        # print("fluc:" "\n" + d)
        # print(result.group(1))
        # for e in d:
        #     print(e)

        # if ' %s. %s' % (Tag, Monat) in d:
        #     print(' %s. %s' % (Tag, Monat))
        #     x = Jahr + Monat1 + Tag
        #     print(x)
        # print(type(d))

        # if ' %s. %s ' % (Tag, Monat) in d:
        #     print(' %s. %s %s. %s' % (Tag, Monat, Tag1, Monat))

        # cc = re.search(r' %s\. %s(.*?) %s\. %s' % (Tag, Monat, Tag1, Monat), d).group(1)
        # cc = str(cc)
        # c = cc.group(1)
    # c = str(cc)
    #



        while Tag < Woche:


            a, b = d.find(' %s. %s ' % (Tag, Monat)), d.find(' %s. %s ' % (Tag + 1, Monat))
            # d = d.replace(' %s. %s ' % (Tag, Monat), "")
            # print(d[a:b])
            # c1 = str(Jahr)
            # c2 = str(Monat1)
            # c3 = str(Tag)
            # x = c1 + "-" + c2 + "-" + c3
            x = Jahr + Monat1 + Tag
            y = str(x)
            y = y[:4] + "-" + y[4:6] + "-" + y[6:8]


            d = d.replace('\n', "")
            text.append(d[a:b])
            text.append(x)

            # print(Tag)
            # with open('fluc.csv', 'w', encoding='UTF8') as f:
            #     writer = csv.writer(f)
            #
            #     writer.writerow(y)

            print(y)
            # print(text)

            Tag += 1
            # Tag1 += 1

            # print(Woche)


            # if Tag1 == Tag + 6:
            #     break

        # print(text)
        # text[0] = text[0].replace('\n', "")

        # print(Tag, Monat)



# schleife

        # k = str(text[0])


        # text[0] = text[0].replace(' %s. %s ' % (Tag, Monat), str(text[1]))
        with open('fluc.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            writer.writerow(text[0])

        print(text[0])
        print(text[2])
        print(text[4])
        print(text[6])
        print(text[8])
        print(text[10])
        # print(text[12])

        # print(text[1])
        # print(text[3])
        # print(text[5])
        # print(text[7])
        # print(text[9])
        # print(text[11])
        # print(text[13])



    # if result is not None:
    #     str(result.group(1))
    #     if "GESCHLOSSEN" in result.group(1):
    #         result1 = "Geschlossen"
    #         print(result1)
    #     else:
    #         print(x)
    #         d = result.group(1)
    #         d = d.replace('\\n', "")
    #         d = d.replace('\\t', "")
    #         d = d.replace('\\t\t\t', "")
    #         d = d.replace('& nbsp', "")
    #         d = d.replace('&nbsp', "")
    #         d = d.replace("'", "")
    #         d = d.replace('[', "")
    #         d = d.replace(']', "")
    #         d = d.replace('\n', "")
    #         d = d.replace(',', "")
    #         d = d.replace('Montag', "")
    #         d = d.replace('Dienstag', "")
    #         d = d.replace('Mittwoch', "")
    #         d = d.replace('Donnerstag', "")
    #         d = d.replace('Freitag', "")
    #         d = d.replace('Samstag', "")
    #         d = d.replace('Sonntag', "")
    #         d = d.replace('fluc_wanne:', "\nfluc_wanne: \n")
    #         # d = d.replace('fluc', "")
    #         print("fluc:" "\n" + d)
    #         # print(result.group(1))

        # Tag += 1
        # if Tag == 32:
        #     break



    # if " 22. Juni" in d:
    #     x = 20210622
    # if " 23. Juni" in d:
    #     x = 20210623
    #     result = re.search(' 23. Juni(.*) 24. Juni', d)
    #     str(result.group(1))
    #     if "GESCHLOSSEN" in result.group(1):
    #         result1 = "Geschlossen"
    #         print(result1)
    #     else:
    #         print(x)
    #         d = result.group(1)
    #         d = d.replace('\\n', "")
    #         d = d.replace('\\t', "")
    #         d = d.replace('\\t\t\t', "")
    #         d = d.replace('& nbsp', "")
    #         d = d.replace('&nbsp', "")
    #         d = d.replace("'", "")
    #         d = d.replace('[', "")
    #         d = d.replace(']', "")
    #         d = d.replace('\n', "")
    #         d = d.replace(',', "")
    #         d = d.replace('Montag', "")
    #         d = d.replace('Dienstag', "")
    #         d = d.replace('Mittwoch', "")
    #         d = d.replace('Donnerstag', "")
    #         d = d.replace('Freitag', "")
    #         d = d.replace('Samstag', "")
    #         d = d.replace('Sonntag', "")
    #         d = d.replace('fluc_wanne:', "\nfluc_wanne: \n")
    #         # d = d.replace('fluc', "")
    #         print("fluc:" "\n" + d)

