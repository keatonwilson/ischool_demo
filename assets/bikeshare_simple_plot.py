# Package imports
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Importing bikeshare data
bikeshare = pd.read_csv('./data/london_merged.csv', parse_dates = [0])
print(bikeshare.head())
# quality control - making sure it imported correctly
print(bikeshare.info())

# Basic plotting with matplotlib
# setting size
plt.figure(figsize=[10,8])
# plotting a histogram, specifying number of bins
hist = plt.hist(x=bikeshare['cnt'], bins=22)
# labeling
plt.xlabel('Number of New Bikeshares/Hour')
plt.ylabel('N')
# print the plot
# plt.savefig('hist.png', dpi=300hist, bbox_inches='tight')
plt.show(hist)

# Boxplot with matplotlib
plt.figure(figsize=[10,8])
boxplot = bikeshare.boxplot(column='cnt', by='season', grid=False)
# plt.savefig('boxplot.png', dpi=300, bbox_inches='tight')
plt.show(boxplot)


# Scatterplot of cnt by perceived temperature
plt.figure(figsize=[10,8])
scatter = bikeshare.plot.scatter(y='cnt',
                       x='t2')
# plt.savefig('scatter.png', dpi=300, bbox_inches='tight')
plt.show(scatter)
