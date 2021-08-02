# Church Website Scraping: Membership List to CSV

The python file can be used to scrape the church website and get the membership list as a csv file. Currently this works on the household list so it will only show information that is considered household information. This might cause some problems with phone numbers.

Running this file requires usage of the command line. It also requires that a few software packages be installed before running. Problems with this program can happen if the church website changes even in ways that can't be seen. I don't intend to personally further maintain this file last updated about June 2021

### For users that are running Microsoft Windows

### For users that are on other operating systems

I got this working using Python 3.8, selenium, and the firefox gecko driver on Linux Mint 20.1. I don't see why this wouldn't work on everything Python 3.6 and later 3.x versions though. Go get Python, install selenium (probably with pip, I honestly don't remember) and get firefox and the gecko selenium driver for it (probably with a distro package manager). then just run `python3 ChurchWebsite.py` and it should work.

### Other notes

The license to this project is included in the python script.
