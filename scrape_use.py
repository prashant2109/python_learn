import requests, sys, os
from bs4 import BeautifulSoup
#https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=USB&type=10-K&dateb=&owner=include&start=&count=
params = {'action':'getcompany', 'CIK':'USB', 'type':'10-K'}
use_data = requests.get('https://www.sec.gov/cgi-bin/browse-edgar', params=params)
# print (use_data.text)
source = use_data.text
soup = BeautifulSoup(source, 'lxml')
comp_blog = soup.find('div', class_='companyInfo')
# print (comp_blog.text)
table_data = soup.find('table', class_='tableFile2')
tr_children = table_data.findChildren('tr', recusive=False)
for tr_chd in tr_children[1:]:
    td_children = tr_chd.findChildren('td', recusive=False)
    filings = td_children[0].text
    url_link = td_children[1].a['href']
    acc_text = td_children[2].text
    por = td_children[3].text
    print (url_link)
    ch_link = 'https://www.sec.gov'+url_link#os.path.join('https://www.sec.gov/', url_link)
    ch_use_data = requests.get(ch_link)
    # print (ch_use_data.text)
    # sys.exit()
    ch_source = ch_use_data.text
    ch_soup = BeautifulSoup(ch_source, 'lxml')
    sec_num_ele = ch_soup.find('div', {'id':'secNum'})
    # print (sec_num_ele.text)
    f_p_d = ch_soup.find_all('div', class_='info')
    filing_d = f_p_d[0].text
    ch_por   = f_p_d[-1].text
    print ([filing_d, ch_por])
    sys.exit()