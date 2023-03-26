# This is a sample Python script.
# Mansoor Haidari
# Kelvin Luk
# Korie Westbrook
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from data_loader import data_loader
import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("Hi")
    print("Hello Everyone")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Read File Io---------------------------------------------------------------------------------------------
with open('../MedicalAI/cardio_training10Set.csv', 'r') as f:
    # skip the header line
    next(f)
    data = []
    for line in f:
        # split the line into a list of values
        values = line.strip().split(';')
        # convert the values to the appropriate data type
        id_, age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, cardio = (
            int(values[0]), int(values[1]), int(values[2]), int(values[3]), float(values[4]), int(values[5]),
            int(values[6]), int(values[7]), int(values[8]), int(values[9]), int(values[10]), int(values[11]),
            int(values[12]))
        # store the values in a nested list
        data.append([id_, age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, cardio])

# print the first 5 rows of data
    print("   id_, age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, cardio")
for row in data[:5]:
    print(row)



# Read File Io---------------------------------------------------------------------------------------------
# Mansoor Haidari
import pandas as pd

# Open the CSV file for reading
with open('heart.csv', 'r') as f:

    # Read lines from file
    lines = f.readlines()

    # Remove newline characters from lines
    lines = [line.strip() for line in lines]

    # Split lines into fields
    fields = [line.split(';') for line in lines]


# Create a pandas DataFrame from the fields
print(data_loader())
df =data_loader()
#print("hello")
#columns1=fields[0][0]
#df = pd.DataFrame(fields[1:], columns=fields[0][0].split(','))
#print(df.keys())
# Sort the DataFrame by a category
#print(df.columns.tolist())
#df_sorted =df.sort_values(['Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope,HeartDisease'])
print(type(df))
#df= pd.DataFrame(df, columns= ['Age','Sex','ChestPainType','RestingBP','Cholesterol','FastingBS','RestingECG','MaxHR','ExerciseAngina','Oldpeak','ST_Slope','HeartDisease'])
data, infor_str = data_loader()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(data)
#df_sorted = df.sort_values(by='category')

#sorted_df = df.sort_values('AGE')
#print(f'sorted_df')


#print(df_sorted)



# Identify the high and low values for a specified column
column_name = 'column_name'
#low_value = sorted_df[column_name].min()
#high_value = sorted_df[column_name].max()

# Identify the number of 'normal' and 'ST' values in a different column
#count_normal = sorted_df[sorted_df['other_column'] == 'normal'].shape[0]
#count_st = sorted_df[sorted_df['other_column'] == 'ST'].shape[0]

# Loop through every value in the sorted DataFrame and print it
#for index, row in sorted_df.iterrows():
    #for col in sorted_df.columns:
        #print(row[col])

#print('Lowest', column_name, ':', low_value)
#print('Highest', column_name, ':', high_value)
#print('Number of normal:', count_normal)
#print('Number of ST:', count_st)

print('Sunday_marc_h26')

# Convert columns to numeric data types

df = pd.read_csv('heart.csv')

Age = pd.to_numeric(df.loc[:, 'Age'], errors='coerce')

RestingBP = pd.to_numeric(df.loc[:, 'RestingBP'], errors='coerce')

Cholesterol = pd.to_numeric(df.loc[:, 'Cholesterol'], errors='coerce')

FastingBS = pd.to_numeric(df.loc[:, 'FastingBS'], errors='coerce')

RestingECG = pd.to_numeric(df.loc[:, 'RestingECG'], errors='coerce')

MaxHR = pd.to_numeric(df.loc[:, 'MaxHR'], errors='coerce')

ExerciseAngina = pd.to_numeric(df.loc[:, 'ExerciseAngina'], errors='coerce')

Oldpeak = pd.to_numeric(df.loc[:, 'Oldpeak'], errors='coerce')

ST_Slope = pd.to_numeric(df.loc[:, 'ST_Slope'], errors='coerce')

HeartDisease = pd.to_numeric(df.loc[:, 'HeartDisease'], errors='coerce')

# print the updated variables
print(Age)
print(RestingBP)
print(Cholesterol)
print(FastingBS)
print(RestingECG)
print(MaxHR)
print(ExerciseAngina)
print(Oldpeak)
print(ST_Slope)
print(HeartDisease)

print('Sort the DataFrame by the Age column')

# Sort the DataFrame by the 'Age' column
sorted_df = df.sort_values(by='Age')

# Identify the high and low values for the 'Cholesterol' column
low_value = sorted_df['Cholesterol'].min()
high_value = sorted_df['Cholesterol'].max()

# Identify the number of 'normal' and 'ST' values in the 'ST_Slope' column

count_normal = sorted_df['RestingECG'].value_counts()['Normal']
count_st = sorted_df['RestingECG'].value_counts()['ST']
count_lvh = sorted_df['RestingECG'].value_counts()['LVH']

print('Lowest Cholesterol:', low_value)
print('Highest Cholesterol:', high_value)
print('Number of normal:', count_normal)
print('Number of ST:', count_st)

