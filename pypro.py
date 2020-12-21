from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
print('Welcome to the DATA VISUALISATION and ANALYSIS of WELLBEING OF PEOPLE in different parts of the world as of September, 2020')
print('In this project, we are going to analize the opinions of people belonging to different GENDERS, AGE GROUPS, ETHINICITIES regarding the standard of their lives.')
income_males = pd.read_csv('incomemales.csv')  #SOURCE OF THIS DATASET HAS BEEN MENTIONED IN THE REPORT.
parameters= income_males['parameters']
values= income_males['values']
cols = ['c', 'r', 'b', 'm']      #('c' is for cyan,'r' is for red color, 'b' is for blue, 'm' is for pink color). saw this info on google.
plt.subplot(211)                 #CONCLUSION OF ALL THESE GRAPHS HAS BEEN MENTIONED AT THE END.
plt.pie(values, labels=parameters, colors=cols , startangle=90, shadow=True, explode=(0, 0, 0.1, 0), autopct='%1.1f%%')     #(largest slice is popped out using explode function.),used autopct func to display percentages of all slices.
plt.title('Income Adequacy of males as percentages in the sample population')
#i have plotted graphs of different subcategories of a main category in a single window for easy comparision.(example,graphs of males and females are in same window)

income_females= pd.read_csv('incomefemales.csv')
parameters = income_females['parameters']
values = income_females['values']
plt.subplot(212)
plt.pie(values, labels=parameters, colors=cols , startangle=90, shadow=True, explode=(0, 0, 0.1, 0), autopct='%1.1f%%') #(largest slice is popped out)
plt.title('Income Adequacy of females as percentages in the sample population')
plt.show() #graphs in same window depict the differences in income adequacy of people belonging to different genders
income18 = pd.read_csv('income18.csv')
parameters = income18['parameters']
cols = ['pink', 'yellow', 'green', 'purple']
values = income18['values']
plt.subplot(211)
plt.pie(values, labels=parameters, colors=cols , startangle=90, shadow=True, explode=(0, 0, 0.1, 0), autopct='%1.1f%%') #(largest slice is popped out)
plt.title('Income Adequacy of people in age group of 18-24 years as percentages in sample population')

income35 = pd.read_csv('income35.csv')
parameters = income35['parameters']
values = income35['values']
plt.subplot(212)
plt.pie(values, labels=parameters, colors=cols , startangle=90, shadow=True, explode=(0, 0, 0.1, 0), autopct='%1.1f%%') #(largest slice is popped out)
plt.title('Income Adequacy of people people in age group of 35-44 years as percentages in sample population ')
plt.show()   #graphs in same window depict differences in income adequacy of people in different age groups

incomeasians = pd.read_csv('incomeasians.csv')
parameters = incomeasians['parameters']
values = incomeasians['values']
cols = ['brown', 'pink', 'yellow', 'purple']
plt.subplot(211)
plt.pie(values, labels=parameters, colors=cols , startangle=90, shadow=True, explode=(0, 0, 0.1, 0), autopct='%1.1f%%') #(largest slice is popped out)
plt.title('Income Adequacy of Asian people')

incomeeuropeons = pd.read_csv('incomeeuropeons.csv')
parameters = incomeeuropeons['parameters']
values = incomeeuropeons['values']
plt.subplot(212)
plt.pie(values, labels=parameters, colors=cols , startangle=90, shadow=True, explode=(0, 0, 0.1, 0), autopct='%1.1f%%') #(largest slice is popped out)
plt.title('Income Adequacy of Europeon people')
plt.show()     #graphs in same window depict differences in income adequacy of people of different ehinicities


#let us compare some other aspects of living between different genders.


style.use('ggplot')
parameters = ['Life Satisfaction', 'Family Wellbeing', 'Happiness Yesterday']
females = [7.9, 7.8, 7.9]
males = [7.8, 7.8, 7.8]
plt.plot(parameters,males, label='Males')
plt.plot(parameters,females,label='Females')
plt.title('How people from different genders behold their lives?')
plt.ylabel('Score out of 10 where 10 is the best')
plt.xlabel('Different Parameters')
plt.grid(True,color='black')
plt.legend()
plt.show()

 #let us compare above mentioned attributes between people of different age groupps.
age_group_18_24 = [7.7, 7.8, 7.8]
age_group_35_44 = [7.8, 7.8, 7.9]
plt.plot(parameters, age_group_18_24, label='Age Group 18-24 years',color='blue')
plt.plot(parameters, age_group_35_44, label='Age Group 35-44 years', color='brown')
plt.legend()
plt.title('How people from different age groups behold their lives?')
plt.ylabel('Score out of 10 where 10 is the best')
plt.xlabel('Different Parameters')
plt.grid(True,color='black')
plt.show()

#let us compare above mentioned attributes for people from different ethinicities.
europeons = [7.8, 7.7, 7.8]
asians = [7.7, 8, 7.9]
plt.plot(parameters, europeons,label='Europeons',color='green')
plt.plot(parameters, asians, label='Asians', color='purple')
plt.legend()
plt.title('How people from different age groups behold their lives?')
plt.ylabel('Score out of 10 where 10 is the best')
plt.xlabel('Different Parameters')
plt.grid(True,color='black')
plt.show()
#now let us see how different people trust the society and political bodies.
new_df = pd.read_csv('trust.csv')
print("Here, we can look at how different people rated their trust over different bodies out of 10 where 10 means complete trust (these are all mean values).")
new_df.set_index('index', inplace=True)  #used set_index to change index from(0-4) to (1-4).
print(new_df)
males = pd.DataFrame({'People':[6.9], 'Health System':[7.3], "Parliament":[6.1], "Police":[7.8], 'Media':[4.8] })   #created dataframes as dictionary, learnt this from Edureka -a you tube channel
females = pd.DataFrame({'People':[6.8], "Health System":[7.1], "Parliament":[6.4], "Police":[7.7], "Media":[4.8]})
age_group_18_24 = pd.DataFrame({'People':[6.7], "Health System":[7.6], "Parliament":[6.6], "Police":[7.7], 'Media':[4.8]})
age_group_35_44 = pd.DataFrame({'People':[6.9], "Health System":[7.2], "Parliament":[6.4], "Police":[7.9], 'Media':[4.8]})
Asians = pd.DataFrame({'People':[7.4], "Health System":[7.9], "Parliament":[7.2], 'Police':[8.1], 'Media':[6.3]})
Europeans = pd.DataFrame({'People':[6.8], 'Health System':[7.1], 'Parliament':[6], 'Police':[8], 'Media':[4.5]})
#created dataframes using pandas to show how people from different catagories trusted the society
print("let us see how much trust males have on the society as a score out of 10")
print(males)
print('let us see how much trust females have on the society as a score out of 10')
print(females)
print('let us see how much trust youngsters have on society as a score out of 10')
print(age_group_18_24)
print('let us see how much trust middle-aged people have on society as a score out of 10')
print(age_group_35_44 )
print('let us see how much trust Europeans have on society as a score out of 10')
print(Europeans )
print('let us see how much trust Asians have on society as a score out of 10')
print(Asians)
#let us lookmat what percentage of different populations had faced discrimination before
print('Let us look at what percentage of different populations had faced discrimination on any basis till the survay was conducted!')
onxaxis = ['Males', 'Females', 'AG(18-24)', 'AG(35-44)', 'Europeans', 'Asians']
onyaxis = [16.6, 20.3, 20.1, 19.4, 16.3, 23]
plt.bar(onxaxis, onyaxis, label='Percentage of population' )
plt.legend()
plt.xlabel('Categories of people ')
plt.ylabel('Percentage of population ')
plt.title('How many people had faced discrimination?')
plt.show()

print('As we can see in the respective bar graph, Largest portion of Asian population(23%) had faced discrimination whereas Europeans had the smallest portion of 16.3%.')
#now we will se how people rated their health using stack plots..
plt.subplot(211)
onxaxis = ['males', 'females', 'AG(18-24)', 'AG(35-44)', 'Europeans', 'Asians']
excellent = [18.5, 18.3, 22.2, 20.2, 18.8, 20.1]
very_good = [38.9, 39.2, 40.1, 40.1, 40.3, 39.0]
good = [28.7, 29.3, 28.8, 29.4, 27.3, 33.2]
poor = [13.9, 13.2, 8.9, 10.3, 13.7, 7.8]

plt.plot([], [], color = 'green', label='Excellent')
plt.plot([], [], color='blue', label='Very Good')
plt.plot([], [], color='pink', label='Good')
plt.plot([], [], color='red', label='Poor')    #plotted empty lines to provide legends to the stackplot.learnt this trick from Edureka -you tube channel.

plt.stackplot(onxaxis, excellent, very_good, good, poor, colors=['green', 'blue', 'pink', 'red'])
plt.xlabel('Categories of people')
plt.ylabel('Self-rated Health')
plt.legend()
plt.title('Self-rated Health of different people')
plt.show()


print('CONCLUSION')
print('ANALYSIS OF DATA OF COMPARISON BETWEEN OPINIONS OF MALES AND FEMALES:')
print('from the graphs regarding income adequacy we can conclude that females face more financial concerns as compared to males as there were more females not having enough money to lead a decent life as compared to males.')
print('Even so, percentage of females having just enough money to support their lives was more than as compared to males. This suggests that females are becoming more independent in terms of survival in recent times.')
print('Regarding Life Satisfaction and Happiness in the lives, females were more contented as they rated themselves higher than men in these areas. ')
print('Both males and females had the same notion about wellbeing of their families on an average as all the values in the graphs were mean values.')
print('More percentage of females faced discrimination as compared to males and the overall health rating of females was also lessre than males. This suggests that gender inequalities are still prevalent in the society.')
print('Health of females is also an area of concern and hence individuals or society as a whole should work together to increase awareness regarding health among females.')

print('ANALYSIS OF DATA OF COMPARISON BETWEEN DIFFERENT AGE GROUPS (18-24 and 35-44 years):')
print('From the graphs of INCOME ADEQUACY, it can be concluded that middle-aged people were financially more stable than youngsters.Although there was more percentage of youngsters having enough money to survive as compared to middle-aged people.')
print('It can be concluded that youngsters were less satisfied with their lives as compared to middle-aged population and the "happiness" rating of the former was also less as compared to latter ')
print('Although, both categories had same notion of wellbeing of their families.')
print('More percentage of youngsters had faced discrimination on any basis as comoared to middle-aged people. This suggests that discrimination and prejuduces are on rise among teenagers and young adults. This can be a matter of serious concern.')
print('Self-health ratings of youngsters were better than middle-aged people. Such trend could be easily predicted')


print('ANALYSIS OF DATA OF COMPARISON BETWEEN EUROPEANS AND ASIANS :')
print('From the graphs of Income Adequacy, we can conclude that Europeans are better in terms of financial status as compared to Asians.This suggests that Asian economies should innovate and inprove in order to become well-off economies.  ')
print('Asians seemed to be more satisfied with their lives whereas ratings of family-wellbeing and happiness were better of Europeans. A part of reason for this maybe related to financial status of both ethinicities.')
print('Asians suffered discrimination the most indicating that discrimination is still prevalent in intra-asian countries as well as asians face prejudices on a global level. ')
print('Health ratings of Asians were better than Europeans.')

print('At last, all the categories had enough faith in people of their societies which can be a hope of a better future, however, all of them had least trust on media.')
print('This is matter of concern and calls for ethics, values, honesty and sense of responsibility in the area of Journalism and Media')
print('All categories had not enough trust on their respective parliaments or governments which can be seen as a threat to future of the world.')
print('This situation calls for honest, ethical, morally-sound leaders to come up and govern the countries in a thoughtful way.')





















