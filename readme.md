###home test

name: Margalit Lionov

## this code receive as input txt file and output 
## analysis of the text:
1) number of words
2) number of rows
3) amount of the unique words in the text
4) length of average sentence, length of the longest sentence
 5) * must popular words in the text
   ** must popular words in the text without syntactic words
6) The longest word sequence in a text that does not contain the letter k
8) Color names appear in the text, and several times each one appears

#to run this code, must be installed this packages:

##pip install collections-extended

##pip install matplotlib

##pip install nltk


##in the first running , you need run this rows to download 'nltk' packages:

nltk.download('punkt')

nltk.download('averaged_perceptron_tagger')


###input example:

It was the year of Our Lord one thousand seven hundred and
seventy-five.  Spiritual revelations were red blue conceded to England at
that favoured period, as at this.  Mrs. Southcott had recently
attained her five-and-twentieth blessed birthday, of whom a
prophetic private in the Life Guards had heralded the sublime
appearance by announcing that arrangements were made for the
swallowing up of London red and Westminster.  Even the Cock-lane
ghost had been laid only a round dozen of years, after rapping
out its messages, as the spirits of this very year last past
(supernaturally deficient in originality) rapped out theirs.
Mere messages in the earthly yellow order of events black had lately come to
the English Crown and People, from a congress of British subjects
in America:  which, strange to relate, have proved more important
to the human race than any black communications yet received through
any of the chickens of the Cock-lane brood.

###output example:

1) words: 159
2) rows: 15
3) uniques:  113
4) length average: 22.0 , max length: 54
5) * [('the', 11)]
  ** [('had', 4)]
6) It was the year of Our Lord one thousand seven hundred and seventy five. Spiritual revelations were red blue conceded to England at that favoured period, as at this. Mrs. Southcott had recently attained her five and twentieth blessed birthday, of whom a prophetic private in the Life Guards had heralded the sublime appearance by announcing that arrangements were made for the swallowing up of London red and Westminster. Even the 
 length: 71
   
8. Counter({'red': 2, 'black': 2, 'blue': 1, 'yellow': 1})


###output of dickens.txt:
1) words: 5646338
2) rows: 640082
3) uniques:  45606
4) length average: 22.671231606157022 , max length: 957
5) * [('the', 292244)]
     
    ** [('i', 101415)]
6) with confidence for a solution of many mysteries; of the profound sadness which had, from the first of my acquaintance with him, possessed a man so gorgeously endowed as the favorite of nature and fortune; of his motives for huddling up, in a clandestine manner, that connection which formed the glory of his life; and possibly (but then I hesitated) of the late unintelligible murders, which still lay under as profound a cloud as ever. Much of this WOULD be unveiled all might be: and there and then, with the corpse lying beside me of the gifted and mysterious writer, I seated myself, and read the following statement: "MARCH 26, 1817. "My trial is finished; my conscience, my duty, my honor, are liberated; my 'warfare is accomplished.' Margaret, my innocent young wife, I have seen for the last time. Her, the crown that might have been of my earthly felicity her, the one temptation to put aside the bitter cup which awaited me her, sole seductress (O innocent seductress!) from the stern duties which my fate had imposed upon me her, even her, I have sacrificed. "Before I go, partly lest the innocent should be brought into question for acts almost exclusively mine, but still more lest the lesson and the warning which God, by my hand, has written in blood upon your guilty walls, should perish for want of its authentic exposition, hear my last dying avowal, that the murders which have desolated so many families within your walls, and made the household hearth no sanctuary, age no charter of protection, are all due originally to my head, if not always to my hand, as the minister of a dreadful retribution. "That account of my history, and my prospects, which you received from the Russian diplomatist, among some errors of little importance, is essentially correct. My father was not so immediately connected with English blood as is there represented. However, it is true that he claimed descent from an English family of even higher distinction than that which is assigned in the Russian statement. He was proud of this English descent, and the more so as the war with revolutionary France brought out more prominently than ever the moral and civil grandeur of England. This pride was generous, but it was imprudent in his situation. His immediate progenitors had been settled in Italy at Rome first, but latterly at Milan; and his whole property, large and scattered, came, by the progress of the revolution, to stand under French domination. Many spoliations he suffered; but still he was too rich to be seriously injured. But he foresaw, in the progress of events, still greater perils menacing his most capital resources. Many of the states or princes in Italy were deeply in his debt; and, in the great convulsions which threatened his country, he saw that both the contending parties would find a colorable excuse for absolving themselves from engagements which pressed unpleasantly upon their finances. In this embarrassment he formed an intimacy with a French officer of high 
   
    length: 508
   
8. Counter({'m': 2060, 'black': 1778, 'red': 1412, 'white': 1376, 'none': 968, 'blue': 878, 'green': 842, 'brown': 663, 'gold': 554, 'grey': 460, 'r': 420, 'b': 323, 'silver': 319, 'snow': 299, 'yellow': 275, 'c': 232, 'linen': 183, 'orange': 168, 'w': 150, 'gray': 140, 'pink': 106, '1': 84, 'purple': 72, 'crimson': 67, 'g': 64, '0': 60, 'lime': 54, 'salmon': 44, 'y': 39, 'navy': 36, 'plum': 34, 'lavender': 29, 'ivory': 28, 'tan': 27, 'chocolate': 26, 'olive': 18, 'wheat': 17, '000': 16, 'coral': 15, 'k': 12, 'maroon': 9, 'indigo': 7, 'azure': 6, 'violet': 6, 'tomato': 6, 'fuchsia': 1, 'sienna': 1, 'aqua': 1, 'thistle': 1, 'peru': 1})


