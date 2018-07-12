'''

{
	"_id" : ObjectId("55c89cf7093a0c0fd69c6526"),
	"properties" : {
		"text" : "The best TEA'ngs in life are free! \nThank you @yo_gc! \n#koi #milktea #tgif",
		"userID" : "insta216141641",
		"userName" : "jess_alarana",
		"day" : "03",
		"month" : "07",
		"year" : "2015",
		"hour" : "17",
		"minute" : "21",
		"second" : "40",
		"source" : "instagram",
		"sentiment" : "positive",
		"sentiStrings" : "best free! \nThank ",
		"labelledSentiment" : "positive",
		"crowder" : "admin"
	},
	"coordinate" : {
		"type" : "Point",
		"coordinates" : [
			103.740123287,
			1.335298682
		]
	}
}
{
	"_id" : ObjectId("55c89cf7093a0c0fd69c67ec"),
	"properties" : {
		"text" : "Pimple popping time 💋",
		"userID" : "insta43104657",
		"userName" : "amirasyafiqah_",
		"day" : "04",
		"month" : "07",
		"year" : "2015",
		"hour" : "15",
		"minute" : "11",
		"second" : "46",
		"source" : "instagram",
		"sentiment" : "negative",
		"sentiStrings" : "💋 ",
		"labelledSentiment" : "positive",
		"crowder" : "admin"
	},
	"coordinate" : {
		"type" : "Point",
		"coordinates" : [
			103.740383629,
			1.33502658
		]
	}
}
'''

jsonlist = '''
{
	"_id" : ObjectId("55c89cf7093a0c0fd69c6526"),
	"properties" : {
		"text" : "The best TEA'ngs in life are free! \nThank you @yo_gc! \n#koi #milktea #tgif",
		"userID" : "insta216141641",
		"userName" : "jess_alarana",
		"day" : "03",
		"month" : "07",
		"year" : "2015",
		"hour" : "17",
		"minute" : "21",
		"second" : "40",
		"source" : "instagram",
		"sentiment" : "positive",
		"sentiStrings" : "best free! \nThank ",
		"labelledSentiment" : "positive",
		"crowder" : "admin"
	},
	"coordinate" : {
		"type" : "Point",
		"coordinates" : [
			103.740123287,
			1.335298682
		]
	}
}
{
	"_id" : ObjectId("55c89cf7093a0c0fd69c67ec"),
	"properties" : {
		"text" : "Pimple popping time 💋",
		"userID" : "insta43104657",
		"userName" : "amirasyafiqah_",
		"day" : "04",
		"month" : "07",
		"year" : "2015",
		"hour" : "15",
		"minute" : "11",
		"second" : "46",
		"source" : "instagram",
		"sentiment" : "negative",
		"sentiStrings" : "💋 ",
		"labelledSentiment" : "positive",
		"crowder" : "admin"
	},
	"coordinate" : {
		"type" : "Point",
		"coordinates" : [
			103.740383629,
			1.33502658
		]
	}
}'''

import json

jsonList = []
jsonstr = ''
j = 0



for i in jsonlist:


    if i == '}' and j <= 3:
        j += 1
    jsonstr += i
    if j == 3:
        jsonList.append(jsonstr)
        jsonstr = ''
        j = 0
    # print(i)
for i in jsonList:

    print(i)
print(len(jsonList))


