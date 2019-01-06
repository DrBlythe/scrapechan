'''
ABOUT:


    This script scrapes 4chan board catalogs for thread titles/teasers,
    uses a blacklist of phrases to determine the amount/percentage of zoomer/boomer/brainlet threads,
    and returns that as a string to stdout


    Usage: $ python3 scrapechan.py [board name]
    i.e.   $ python3 scrapechan.py g
           $ python3 scrapechan.py wg


    Running with no board argument will default to /g/
    Add any phrases or words that you want to filter to the lists, below
    Pay attention to the format of the phrase though, example:
        Adding "phone" will cause a post with 'microphone' to be deemed bad, however
        adding " phone " (spaces surrounding) will only do so if the word phone (by
        itself) is in the thread title
    This could all just be done with regexes probably, but it's already done, so...


    I use this in my i3bar to see whether or not /g/ is even worth checking (it's not)
    If you are using i3blocks:

        # /g/ thread analyzer
        [absolute_state]
        label=/g/ Brainlet Meter
        interval=once
        command=echo $(python3 /path/to/executable/scrapechan.py)
        separator=true
'''


import requests
import re
import sys



# Blacklisted phrases or words
# You may want separate lists for different boards
#
g_blacklist = ["bro ","seething ","apple ","install gentoo", "why haven","why doesn", "why aren","he doesnt","developer ", "based and","good afternoon","discord ","zoomers ","meme ","hey guys","smartphone"," phone","google","coding","memes ","browser","firefox","waterfox", "chrome ","chromium","sup ","rip ","gaym","android ","stickers ","game","web ","normie","itoddler","btfo "," shill"," sjw ", " interject ","one copy of","gaming","daily reminder","virtual reality"," vr "," brave", "he doesnt"," intel "," amd ","nvidia"," gpu"," 5g "," pajeet ", " burger ", " app", "freetard","windows 10","incel ","madmen","comfy","absolute state"," mac "," ios","reddit","what does g think","intellectual ","oh no no"]



# Default board is /g/ if no argument given
#
if (len(sys.argv) < 2):
    url = "http://boards.4channel.org/g/catalog"
else:
    url = "http://boards.4channel.org/" + sys.argv[1]  + "/catalog"



# Get html content
#
content = requests.get(url)


# Use regex to add all thread titles text to a list
# In the html, the format for the thread titles is: '"teaser:"*title here*"'
#
thread_list = re.findall(r'teaser":"(.*?)"',content.text)



# Make all text lowercase, remove special characters, and find percentage of bad threads
# Bad if:
#       Title is less than 5 words
#       Starts with greentext
#       Word from blacklist matches
#
special_chars = ["/","\\","-","\'","\"","?","<",";",":",".",",","!","@","#","$","%","^","&","*","(",")","0","1","2","3","4","5","6","7","8","9"]
greentext = "&gt;" #html for '>'
total_threads = 151
bad_thread_count = 0
for title in thread_list:
    if len(title.split()) < 5:
        bad_thread_count += 1
        continue
    elif (title[0:4] == greentext): # If title starts with greentext
        bad_thread_count += 1
        continue
    else:
        for char in special_chars:
            title = title.replace(char,"")
        for phrase in g_blacklist:
            if phrase in title.lower():
                bad_thread_count += 1
                '''
                #Uncomment to see title of bad thread and phrase that trigged it
                print()
                print("bad title:",title)
                print("matching phrase:",phrase)
                print()
                '''
                break

percentage = round((bad_thread_count/total_threads)*100)
print(str(percentage)+"%")
