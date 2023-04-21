import numpy as np
import pandas as pd

dataFrame = pd.read_excel('27-SalarySheet.xlsx')

describe = dataFrame.describe()
#print(describe)

row_count = dataFrame.count(axis=1)
#print(row_count)

salary_mean = dataFrame.mean(axis=0,numeric_only=True)
#print(salary_mean)

department = dataFrame.groupby('Department').mean(numeric_only=True)
#print(department)

title_mean = dataFrame.groupby('Title').mean(numeric_only=True)
#print(title_mean)

software = dataFrame.loc[dataFrame['Department'] == "Software Development"].groupby('Title').mean(numeric_only=  True)
#print(software)

finance = dataFrame.loc[dataFrame['Department'] == 'Finance'].groupby('Title').mean(numeric_only=  True)
#print(finance)

c_level_soft = dataFrame.loc[dataFrame['Department'] == 'Software Development'].groupby('Title').describe()
c_level_market = dataFrame.loc[dataFrame['Department'] == 'Marketing'].groupby('Title').describe()

print(c_level_soft)
print(c_level_market)