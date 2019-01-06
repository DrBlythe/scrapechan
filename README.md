# ScrapeChan: A quality analyzer for all current posts on any 4chan board  

This Python program scrapes 4chan board catalogs for thread titles/teasers,
uses a blacklist of phrases to determine the amount/percentage of crappy threads,
and prints that to stdout  

Dependencies:  
	python-requests  


Usage: $ python3 scrapechan.py [board name]  
i.e.   $ python3 scrapechan.py g  
       $ python3 scrapechan.py wg  


Running with no board argument will default to /g/  
Add any phrases or words that you want to filter to the lists, below  
Pay attention to the format of the phrase though, example:  
	Adding "phone" will cause a post with 'microphone' to be deemed bad, however  
	adding " phone " (spaces surrounding) will only do so if the word phone (by  
	itself) is in the thread title  
	

I use this in my i3bar to see whether or not /g/ is even worth checking (it's not)  
If you are using i3blocks:  

	# /g/ thread analyzer
	[absolute_state]
	label=/g/ Brainlet Meter
	interval=once
	command=echo $(python3 /path/to/executable/scrapechan.py)
	separator=true
