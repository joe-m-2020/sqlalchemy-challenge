# sqlalchemy-challenge
homework 10

Going on Vacation from December 3rd to December 10th.

I've decided to check the weather for this time last year using data reported by Hawaii weather stations. 

In my first analysis, the precipitation was analyzed.  The last 12 months of percipitation data from the set was queried and organized into a bar chart by daily reports of rainfall (Images\precipitation.png). Judging by the variety in the data, there doesn't appear to be a specific time of year that is free from rainfall, so this won't affect my plans. A statistics summary was created showing a .17" average rainfall which is small enough to take my chances.

Next I found the station WAIHEE 837.5, that had the most observations and began a temperature analysis showing the lowest temperature recorded was 54.0 degrees, the highest was 85.0 degrees and the average was 71.66 degrees.  The data recorded by this station is then shown in a histogram (Images\temperature.png) where the highest number of observations were between 70 and 80 degrees which is a very comfortable range for vacation weather.

I then created a flask module to display the results of my the precipitation and temperature queries (app.py). 


