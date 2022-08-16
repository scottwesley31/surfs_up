# surfs_up
Module 9

## Overview of the Analysis
Following a much-needed vacation to Hawaii, my theoretical self decided to start the process of opening a "Surf n' Shake" shop in Oahu which will provide customers with surfing gear and also ice cream. With some money in the bank to invest into this business idea, I contacted W. Avy an investor willing to support the business plan. W. Avy requests an analysis of the weather in Oahu to ensure that this business would be sustainable.

An in-depth analysis of the precipitation levels, min and max temperatures, and an average temperature that occurs at multiple stations in Oahu was completed initially. This information was made vailable on a web browser (using Flask). W. Avy now would like to gather more information about temperature trends for the months of June and December in Oahu.

## Results

### Determine the Summary Statistics for June
Utilizing a SQLite file with all of the weather data for Oahu and after setting up a session to allow for the querying of the database, a list of all of the temperatures in June (`june_temps`) can be created with the following code:

![june_temps_code](https://user-images.githubusercontent.com/107309793/184776565-5cf19adf-127c-4ea7-b76d-f9acf2189fdd.png)

This can then be converted into a Pandas DataFrame.

![june_temps_df](https://user-images.githubusercontent.com/107309793/184777547-2eea9783-6a50-4b1f-8bb6-bb51cc34e5ec.png)

The summary statistics for June can be calculated and viewed using the `describe()` function resulting in the following output:

![june_temps_stats](https://user-images.githubusercontent.com/107309793/184778450-390bbf72-3470-46d0-895b-2c0891d3a65f.png)

On average, the temperature in June is around 74.9°F. The June temperatures do not tend to deviate far from the mean (standard deviation of 3.357417).

To better visualize the distribution of all of the reported June temperatures a simple histogram was created.

![june_histogram](https://user-images.githubusercontent.com/107309793/184779680-93247da8-9bb9-44e2-992f-3c6635ea1386.png)

It's clear from this figure that most of the time the temperature is somewhere between 70-79°F (most notably 74-75°F which is consistent with the summary statistics).

### Determine the Summary Statistics for December
The same process was repeated for the temperatures in the months of December in Oahu. A list of all of the temperatures in December (`december_temps`) can be created with the following code:

![december_temps_code](https://user-images.githubusercontent.com/107309793/184780066-a94e561b-3766-481c-b740-c6012cb9ad54.png)

This can then be converted into a Pandas DataFrame.

![december_temps_df](https://user-images.githubusercontent.com/107309793/184780081-e0ddaeea-7894-4f10-a6b6-e60a52ddf81a.png)

The summary statistics for June can be calculated and viewed using the `describe()` function resulting in the following output:

![december_temps_stats](https://user-images.githubusercontent.com/107309793/184780096-c5fc681b-6a71-47d0-aa5e-0bcbd747816a.png)

On average, the temperature in December is around 71.0°F. The December temperatures do not tend to deviate far from the mean (standard deviation of 3.745920).

To better visualize the distribution of all of the reported December temperatures a simple histogram was created.

![december_histogram](https://user-images.githubusercontent.com/107309793/184780103-1c8339c2-eaf9-49c2-ba3e-cf6c4a9f34d7.png)

It's clear from this figure that most of the time the temperature is somewhere between 70-75°F (most notably 70-71°F which is consistent with the summary statistics).

## Summary
