# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 18:26:31 2017

@author: Leon and Han
"""

import re
import glob
import os
import io
import cPickle
from nltk import tokenize

def get_sections(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    return content


    #Look for where it has the indicators for risk factors. 2 if cases
    #Split into sentences until indicators of the end
    #Add each sentence to sections
    #save dictionary as a p file



"""
def set_key(sections, key_count, key_value, global_key):
    if key_count == 1:
        global_key = key_value
        sections[global_key] = ""
    else:
        global_key = key_value
        sections[global_key] = ""
    


def get_sections(filename):
    business_count = 0
    risk_count = 0
    line_count = 0
    business = re.compile('^\w{4,5}\s1\.$')
    risks = re.compile('^\w{4,5}\s1A\.$')
    end_section = re.compile('^\w{4,5}\s1B\.$')
    
    file = open(filename, 'r')
    key = ""
    sections = {}

    for line in file:
        line = line.strip()
        line_count+=1
        if business.match(line):
            business_count+=1
            set_key(sections, business_count, "Business Overview", key)
            print(key)
        elif risks.match(line):
            risk_count+=1
            set_key(sections, risk_count, "Risk Factors", key)
            print(key)
        elif end_section.match(line):
            if line_count > 300:
                break
        else:
            if key != "":
                newline = sections[key] + line
                sections[key] = newline
    return sections
"""
#sections = get_sections('C:/Users/leon/Desktop/AIF-Risk/10K/CXW_10K_2015.txt')

def get_risks(filename):
    sections = get_sections(filename)

    count=0;
    startindex=0;
    endindex=0;
    outputlist=[]
    riskfactors=""
    #check if it's a new or old version of the 10-k
    #old version
    if "**Factors That May Affect Future Results and Financial Condition **" in sections or "**Factors That May Affect Future Results and Financial Condition**" in sections:
        for x, element in enumerate(sections):
            #regex
            if sections[x] == "**Factors That May Affect Future Results and Financial Condition **" or sections[x] == "**Factors That May Affect Future Results and Financial Condition**":
                startindex=x

        print(sections[startindex])

        for x in range(startindex+1,len(sections)):
            #regex
            if "**" in sections[x]:
                endindex=x
                break

        print(sections[endindex])

        for x in range(startindex+1,endindex+1):
            riskfactors=riskfactors+" "+sections[x]

        riskfactors=re.sub('_','',riskfactors)
        return riskfactors

    else:
        for x, element in enumerate(sections):
            #Should be using regex
            if "**Risk Factors **" in sections[x] or "Risk Factors**" in sections[x] or "Risk Factors **" in sections[x] or "The following discussion of risk factors contains forward-looking statements." in sections[x]:
                startindex=x

        print(sections[startindex])

        for x in range(startindex+1,len(sections)):
            #regex
            if "**Item" in sections[x] or "Item 1B." in sections[x]:
                endindex=x
                break

        print(sections[endindex])

        for x in range(startindex+1,endindex+1):
            riskfactors=riskfactors+" "+sections[x]

        riskfactors=re.sub('_','',riskfactors)
        return riskfactors


for x in range(2,17):
    if x<10:
        txtfile="AAPL_10K_200"+str(x)+".txt"
        savefile="List_AAPL_10K_200"+str(x)+".p"
    else:
        txtfile="AAPL_10K_20"+str(x)+".txt"
        savefile="List_AAPL_10K_20"+str(x)+".p"
    final_list=tokenize.sent_tokenize(get_risks(txtfile))
    cPickle.dump(final_list, open(savefile, 'wb')) 









    