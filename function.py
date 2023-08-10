import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import re



def fun(result,data):
    for index, i in enumerate(result):
        # name
        if index == 0:
            data['Name'].append(i[1])

        # designation
        elif index == 1:
            data['Designation'].append(i[1])
        # email-id
        elif '@' in i[1]:
            data['Email_id'].append(i[1])

        # company name
        elif len(result) < 9 and index == len(result) - 1:
            data['Company_name'].append(i[1])
        elif len(result) >= 9:
            if re.findall('^[A-Za-z]+$', i[1]) and index != 0 and 'WWW' not in i[1]:
                data['Company_name'].append(i[1])
                if len(data["Company_name"]) >= 2:
                    data["Company_name"] = [('-'.join(data["Company_name"]))]

        # website
        if "www " in i[1].lower() or "www." in i[1].lower():
            data["Website"].append(i[1])
        elif "WWW" in i[1]:
            data["Website"] = [result[4][1] + "." + result[5][1]]

        # contact info
        if "-" in i[1]:
            data["Contact_no"].append(i[1])
            if len(data["Contact_no"]) == 2:
                data["Contact_no"] = [" & ".join(data["Contact_no"])]

        # area
        match1 = re.findall('(^[0-9].+), [a-zA-Z]+', i[1])
        if match1:
            data["area"].append(match1[0])
        elif re.findall('[0-9] [a-zA-Z]+', i[1]):
            data["area"].append(i[1])

        # city
        config1 = re.findall('.+St , ([a-zA-Z]+).+', i[1])
        config2 = re.findall('.+St,, ([a-zA-Z]+).+', i[1])
        config3 = re.findall('^[E].*', i[1])
        if config1:
            data["city"].append(config1[0])
        elif config2:
            data["city"].append(config2[0])
        elif config3:
            data["city"].append(config3[0])

        # state
        state = re.findall('([a-zA-Z]{9}) +[0-9]', i[1])
        if state:
            data["state"].append(state[0])
        elif re.findall('^[0-9].+, ([a-zA-Z]+);', i[1]):
            data["state"].append(i[1].split()[-1])
        if len(data["state"]) == 2:
            data["state"].pop(0)
        if len(i[1]) >= 6 and i[1].isdigit():
            data["pin_code"].append(i[1])
        match2 = re.findall('[a-zA-Z]{9} +([0-9]{6})', i[1])
        if match2:
            data["pin_code"].append(match2[0])

    return data