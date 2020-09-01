# -*- coding: UTF-8 -*-
import codecs
import json
import random
import numpy as np

def onMessage(questionGetted):
    answer=''
    result=False
    checkQuestion=False
    with open(r'data.json', 'r', encoding='utf-8') as dt:
        dataQA = json.load(dt)        
    try:
        for dataLine in dataQA:
            if type(dataLine["question"]) == list:
                for question in dataLine["question"]:
                    if question.lower() in questionGetted.lower():
                        checkQuestion=True
            else:
                if dataLine["question"].lower() in questionGetted.lower():
                    checkQuestion=True
            if checkQuestion==True:
                if type(dataLine["answer"]) == list:
                    size = len(dataLine["answer"])
                    num = random.randint(0,size-1)
                    print(num)
                    answer = dataLine["answer"][num]
                    checkQuestion=False
                else:
                    answer = dataLine["answer"]
                    checkQuestion=False
                result=True                        
        if result==False:
            answer = "Câu hỏi không có dữ liệu"
    except:
        answer = "Câu hỏi không có dữ liệu"
    return answer