# Package imports
import numpy as np
import pandas as pd
from plotnine import *

# good plotnine resources/examples:
# https://medium.com/@gscheithauer/data-visualization-in-python-like-in-rs-ggplot2-bc62f8debbf5

# Importing bikeshare data
bikeshare = pd.read_csv("../data/london_merged.csv", date_parser=[0])
# Changing to categorical data
bikeshare['is_holiday'] = bikeshare['is_holiday'].astype('category')
# Changing categorical data labels
bikeshare['is_holiday'] = bikeshare['is_holiday'].cat.rename_categories(["No Holiday", "Holiday"])
# Printing QC
print(bikeshare.head())

# one big diff from ggplot is that aesthetic mappings aren't carried through... though apparently
# it should... will have to double check this later.

# basic scatterplot from last time
fig = (
    ggplot(data=bikeshare) +
        geom_point(aes(x='t2', y='cnt'),
                   alpha=0.3) +
        geom_smooth(aes(x='t2', y='cnt'),
                    method="lm", color="yellow", size=1) +
        theme_classic() +
        xlab("Perceived Temperature (ºC)") +
        ylab("New Bikeshare Counts per Hour")
)

# print(fig)
# ggsave(plot=fig, filename='basic_scatter.png', dpi=300)

# Faceted
fig2 = (
        ggplot(data=bikeshare) +
        geom_point(aes(x='t2', y='cnt', color='is_holiday'),
                   alpha=0.3) +
        geom_smooth(aes(x='t2', y='cnt'),
                    method="lm", color="black", size=1) +
        theme_classic() +
        xlab("Perceived Temperature (ºC)") +
        ylab("New Bikeshare Counts per Hour") +
        facet_wrap('is_holiday')
)

print(fig2)


