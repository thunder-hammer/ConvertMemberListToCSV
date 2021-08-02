'''
Permission is granted to the recipient of this software to retain, modify, execute, copy, and distribute this software for church use within the Church of Jesus Christ of Latter Day Saints provided that they retain this notice, and the following disclaimer in all copies, verbatim or otherwise. Attribution is not required. All other rights reserved.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''


from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
#import re
import pprint
pp = pprint.PrettyPrinter(indent=4).pprint


class Member():
    
    def __init__(self, name, address, phone):
        self.building, self.apartment = self._convert_address_to_building_and_apartment(address)
        self.name = name
        self.phone = phone

    def _convert_address_to_building_and_apartment(self, address):
        #in our case the building number is always on line one and the apartment number is on line 2 if there is one.
        #the line 2 address always starts with apt too
        line = address.split("\n")
        building = line[0]
        if line[1][0] in ["east", "west", "East", "West"]:
            if line[1][0] in ["east", "East"]:
                apt = 2
            else:
                apt = 1
        elif line[1][0] not in "Aa#0123456789":
            apt = None
        else:
            apt_split = line[1].split()
            if len(apt_split) == 2:
                apt = int(apt_split[1])
            else:
                apt = None
        return building, apt

    def __str__(self):
        return self.name + '|' + self.building + '|' + str(self.apartment) + '|' + self.phone

    def __lt__(self,other):
        if self.building == other.building:
            if self.apartment == None or other.apartment == None:
                return False
            else:
                return self.apartment < other.apartment
        else:
            return self.building < other.building
    

driver = webdriver.Firefox()
driver.get("https://id.churchofjesuschrist.org/")


input("Please enter credentials into the web page and press enter")

def get_table_from_website(website):
    '''broken into a function to allow for grabbing individuals too. it should work for both'''
    driver.get(website)
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    # member_list = mainContent.text

    memberList = driver.find_elements_by_xpath("//table")
    if len(memberList) != 1:
        print("WARNING: It appears that more than one table is present on the page using the last one")
    for table in memberList:
        data = [item.text for item in table.find_elements_by_xpath(".//*[self::td or self::th]")]

    return data

website = "https://lcr.churchofjesuschrist.org/records/member-list?lang=eng&households"
data = get_table_from_website(website)
#9 columns in the table
#'', 'Name', 'Household Members', '', '', '', 'Address', 'Phone Number', 'E-mail'
#0    1       2                   3   4   5   6          7               8

counter = 0
name = ""
address = ''
phone = ''

members = []

for d in data:
    if counter == 1:
        name = d
    elif counter == 6:
        address = d
    elif counter == 7:
        phone = d
    elif counter == 8:
        if name != "Name" and name[0] != "*":
            member = Member(name, address, phone)
            members.append(member)
        name = ""
        address = ''
        phone = ''

    counter += 1
    if counter == 9:
        counter = 0

members.sort()

with open("ward_list.csv", "w") as f:
    for m in members:
        f.write(str(m))
        f.write("\n")

print('file saved to ward_list.csv')

