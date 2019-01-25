# ScrapeChan: A quality analyzer for all current posts on any 4chan board  

This Python program scrapes 4chan board catalogs for thread titles/teasers,
uses a blacklist of phrases to determine the amount/percentage of crappy threads,
and prints that to stdout  

### Dependencies:  
	python-requests  


### Example Usage: 
	$ python3 scrapechan.py g
	$ python3 scrapechan.py a


Running with no board argument will default to /g/  
Add any phrases or words that you want to filter to the lists within the code  
You'd probably want to add separate lists for each board you use  


Pay attention to the format of the phrase though, example:  

Adding "phone" will cause a post with 'microphone' to be deemed bad, however  
adding " phone " (spaces surrounding) will only do so if the word phone (by  
itself) is in the thread title  
	

I use this in my i3bar to see whether or not /g/ is even worth checking at the moment(it's not)  
If you are using i3blocks:  

	# /g/ thread analyzer
	[absolute_state]
	label=Absolute State
	interval=once
	command=echo $(python3 /path/to/executable/scrapechan.py)
	separator=true

### Screenshot of use in i3bar
![screenshot](https://raw.githubusercontent.com/DrBlythe/scrapechan/master/sc-screenshot.png)  
