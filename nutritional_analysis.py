#Analyzing nutrition facts of McDonald's menu items to gain a better understanding about what common fast food options are generally composed of
#Dataset taken from: https://www.kaggle.com/mcdonalds/nutrition-facts

#importing necessary libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

#importing dataset, getting a basic idea of what the data consists of
df = pd.read_csv('G:\My Drive\Python\menu.csv')
df.head()
df.columns
df.head(10)
df.tail()

#checking data for null values
print(df.isnull().any()) #all false = no null values
print(df.describe()) #no oddballs in describe() output = checks for null values complete

#After looking at the data csv file, it can be seen that the first 110 rows are those containing nutritional information of food
#To first analyze the nutritional information of McDonald's items, the average food calories will be determined for each food
food_items = df.head(110)

#dataframe that compares each food item to its calorie content
food_cals = pd.DataFrame({'Item': food_items.Item, 'Calories': food_items.Calories})
food_sorted = food_cals.sort_values('Calories')#sorts table via calorie order
food_sorted.plot.barh(x = 'Item', y = 'Calories') 
plt.title("Average Calorie Content for Food Menu Items")
plt.show()

#dataframe that displays the average calorie content of each food category
food_category_cals = food_items[['Category','Calories']].groupby('Category').mean()
food_category_cals
food_category_sorted = food_category_cals.sort_values('Category') #sorts table via alphabetic order
food_category_sorted
food_category_sorted.plot.barh()
plt.title("Average Calorie Content for Food-Based Menu Categories")
plt.show()
#As seen from the horizontal bar chart, the category with the highest average calorie content is Chicken and Fish, followed up closely with Breakfast Items and Beef & Pork Items

#Observing average calories of menu items and their relations to daily recommended calorie levels
overall_avg_cals = df["Calories"].mean()
overall_avg_cals
#Overall_avg_cals tells us the overall average calories of all menu items (including drinks) at McDonald's: 368.2692307692308 (Chicken and Fish, Breakfast, and Beef & Pork items are all significantly above this average)

overall_food_cals = food_cals["Calories"].mean()
overall_food_cals
#Overall_food_cals tells us the overall average calories of all menu items that are food at McDonald's: 462.09090909090907

daily_cal_goals_avg = 2000 #daily recommended caloric goals
contr_cal_goals = overall_avg_cals/2000
contr_cal_goals*100 # 18.41346153846154% of daily calorie goals come from one food menu item from McDonald's

beverages = df.loc[df.Category == 'Beverages']
beverages
contr_cal_goals_bev = beverages[['Category','Calories']].groupby('Category').mean()/2000
contr_cal_goals_bev*100 #5.685185% of daily calorie goals come from one beverage item from McDonald's

#from the data, we see that the remaining 150 rows after the first 110 are all different types of drinks
all_drinks = df.tail(150)
all_drinks
average_all_drinks = all_drinks["Calories"].mean()
average_all_drinks #Average calorie content of all drinks on McDonald's Menu: 299.46666666666664
cont_cal_goals_alldrinks = average_all_drinks/2000
cont_cal_goals_alldrinks * 100
#14.973333333333333% of daily calorie goals come from on average, one of the drink menu items from McDonald's

#Visual Statistical Analysis (Seaborn Library Visualization)

#Relational plots
sns.relplot(x="Category", y="Calories", data=df)
plt.title("Category vs. Calories")
plt.show() #Chicken and Fish has a large outlier seen to have over 1700 calories
df.columns
sns.relplot(x="Category", y="Calories", hue="Cholesterol", data=df)
plt.title("Category vs. Calories with Hue of Cholesterol")
plt.show() #Breakfast foods primarily have the highest cholesterol levels (most likely due to cholesterol from memnu items containing eggs)

#Distribution of Calories
plt.figure(figsize=(15,5))
plt.title("Caloric Distribution")
cal_distribution = sns.displot(df["Calories"])
plt.show()

#Distribution of Cholesterol
plt.figure(figsize=(15,5))
plt.title("Cholesterol Distribution")
chol_distribution = sns.displot(df["Cholesterol"])
plt.show()

#Overaching Conclusions:
#Breakfast foods primarily have the highest cholesterol levels (most likely due to cholesterol from memnu items containing eggs)
#Chicken and Fish Category of Food has a large outlier menu item that has been seen to have over 1700 calories
#About 15% of daily calorie goals come from, on average, one of the drink menu items from McDonald's
#About 19% of daily calorie goals come from one food menu item from McDonald's
#Food Categories Chicken and Fish, Breakfast, and Beef & Pork items are all significantly above the average caloric content of food items (Chicken and Fish has the highest)