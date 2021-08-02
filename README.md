# Church Website Scraping: Membership List to CSV

The python file can be used to scrape the church website and get the membership list as a csv file. Currently this works on the household list so it will only show information that is considered household information. This might cause some problems with phone numbers.

When running this file plese be careful to check the web address of the page that requests you put in credentials to ensure it makes sense. Feel free to interact with the page, check the script to ensure it is going to the proper sign in page, etc to ensure that you are not putting youre credentials in the wrong place.

Running this file requires usage of the command line. It also requires that a few software packages be installed before running. Problems with this program can happen if the church website changes even in ways that can't be seen. I don't intend to personally further maintain this file last updated about June 2021

## For users that are running Microsoft Windows

### Setup (only do the first time)

1. Get and install the firefox web browser (skip if you already have it, firefox is required I had a hard time getting chrome to work right) https://www.mozilla.org/en-US/firefox/new/
2. Get Python and install it https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7?activetab=pivot:overviewtab This will make the .py file executable.
3. Open up the command prompt. click start. type `cmd`. run the program called command prompt.
4. In the command prompt window type `pip install selenium`
5. Download the Geckodriver https://github.com/mozilla/geckodriver/releases this will let us interact with firefox to get the data from the member list.
6. Extract the geckodriver.exe (Geckodriver executable application) from the .zip that it came in. The extracted executable needs to be placed in the same folder as the ChurchWebsite.py
7. Download the .py file that is associated with this repository. It can be copy and pasted into a new file if needed. Just make sure that it is .py (not txt) and in the same folder as the geckodriver.exe application (this folder will also be the location of the output)

### Running the program

1. In windows explorer, In the folder where the ChurchWebsite.py and geckodriver.exe are located
2. hold the shift key and right click on a blank space in the explorer window
3. click open powershell window here (a blue window should appear with the name of the folder)
4. type `python3 .\ChurchWebsite.py` then hit enter
5. A new firefox window should open up, Double check that it opened to the church website https://id.churchofjesuschrist.org/
6. Put in your username and password to the church website and click login. The main page of the website should now be visible.
7. Select the blue windows powershell window and press enter. It should prompt you to login and then press enter.
8. wait about 15 seconds and a new file called ward_list.csv will be created, or overwritten in the folder where ChurchWebsite.py is located.

## For users that are on other operating systems

I got this working using Python 3.8, selenium, and the firefox gecko driver on Linux Mint 20.1. I don't see why this wouldn't work on everything Python 3.6 and later 3.x versions. Go get Python, install selenium (probably with pip, I honestly don't remember) and get firefox and the gecko selenium driver for it (probably with a distro package manager). then just run `python3 ChurchWebsite.py` and it should work. I just didn't take notes when doing this so your on your own but it should work.

### Usage notes

This application will overwrite any file named ward_list.csv in the directory where it is run.

Addresses are assumed to be in a pretty narrow format. for example:

`200 E 200 N
Apt 12
city, state zip`

When entering these addresses on the website I try to ensure the address is put in with spaces after the street numbers, before the n,e,s,w directions. The apartment number is on line 2 of the address with apt preceeding it. Some variations on the format are accounted for but it's safest to just try to make sure they look like this.

### License and disclaimer

Permission is granted to the recipient of this software to retain, modify, execute, copy, and distribute this software for church use within the Church of Jesus Christ of Latter Day Saints provided that they retain this notice, and the following disclaimer in all copies, verbatim or otherwise. Attribution is not required. All other rights reserved.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
