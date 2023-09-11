
import pandas as pd
import seaborn as sns
import numpy as np
# Reading in the Nobel Prize data
nobel = pd.read_csv('datasets/nobel.csv')
nobel.head(6)
# Display the number of (possibly shared) Nobel Prizes handed
# out between 1901 and 2016
display(len(nobel))
# Display the number of prizes won by male and female recipients.
display(nobel['sex'].value_counts())
# Display the number of prizes won by the top 10 nationalities.
nobel['birth_country'].value_counts().head(10)
#USA Dominance
# Calculating the proportion of USA born winners per decade
nobel['usa_born_winner'] = nobel['birth_country'].apply(lambda x: True if x=="United States of America" else False)
nobel['decade'] = pd.Series(np.floor(nobel['year']).astype('int64'))
prop_usa_winners = nobel.groupby('decade', as_index=False)['usa_born_winner'].mean()

# Display the proportions of USA born winners per decade
print(prop_usa_winners)
#visualisation
# Setting the plotting theme
sns.set()
# and setting the size of all plots.
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [11, 7]

# Plotting USA born winners 
ax = sns.lineplot(x=prop_usa_winners['decade'], y=prop_usa_winners['usa_born_winner'])

# Adding %-formatting to the y-axis
from matplotlib.ticker import PercentFormatter
yticks=PercentFormatter(1)
ax.yaxis.set_major_formatter(yticks)
#per gender
# Calculating the proportion of female laureates per decade
nobel['female_winner'] = nobel['sex'].apply(lambda x: True if x=='Female' else False)
prop_female_winners = nobel.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()

# Plotting USA born winners with % winners on the y-axis
# Setting the plotting theme
sns.set()
# and setting the size of all plots.
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [11, 7]

# Plotting USA born winners 
ax = sns.lineplot(x=prop_female_winners['decade'], y=prop_female_winners['female_winner'], hue=prop_female_winners['category'])

# Adding %-formatting to the y-axis
from matplotlib.ticker import PercentFormatter
yticks=PercentFormatter(1)
ax.yaxis.set_major_formatter(yticks)
#first woman
# Picking out the first woman to win a Nobel Prize
nobel[nobel['sex']=='Female'].nsmallest(1, 'year')
#repeat laureats
# Selecting the laureates that have received 2 or more prizes.
nobel.groupby('full_name').filter(lambda x: len(x) > 1)
#age
# Converting birth_date from String to datetime
nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])

# Calculating the age of Nobel Prize winners
nobel['age'] = nobel['year'] - nobel['birth_date'].dt.year 

# Plotting the age of Nobel Prize winners
sns.lmplot(x='year', y='age', data=nobel, lowess=True, aspect=2,line_kws={'color' : 'black'})
#age difference
# Same plot as above, but separate plots for each type of Nobel Prize
sns.lmplot(x='year', y='age', row='category', data=nobel, lowess=True, aspect=2,line_kws={'color' : 'black'})
#oldest and youngest winners
# The oldest winner of a Nobel Prize as of 2016
display(nobel.nlargest(1, 'age'))
# The youngest winner of a Nobel Prize as of 2016
nobel.nsmallest(1, 'age')










