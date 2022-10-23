# Investigation of the movie database

## Introduction

This study is about the **The TMDb movie data**, which is a dataset containing informations about around 10000 movies, collected from the The Movie Database (TMDb). The data go from 1960 to 2015. Here are the list of the informations (columns) in the dataset:

* id: the identification of the movie in the TMDb.
* imdb_id: the identification of the movie in the IMBD (Internet Movie Database).
* popularity: rate of popularity of the movie based on different metrics (Number of votes for the day, Number of views for the day, Number of users who marked it as a "favourite" for the day, Number of users who added it to their "watchlist" for the day, Release date, Number of total votes, Previous days score).
* budget: the actual budget in dollar.
* revenue: the actual revenue in dollar.
* original_title.
* cast: list of the main actors in the movie.
* homepage: the website of the movie.
* director: the name of the director.
* tagline: a catchy sentence describing the movie.
* keywords: list of the keywords.
* overview: the overview of the movie.
* runtime: length of the movie in minutes.
* genres:list of the genre of the movie (a movie can have more than one genre classification).
* production_companies: list of companies who had produced the movie (can be more than one).
* release_date.
* vote_count: number of vote.
* vote_average.
* release_year.
* budget_adj: the adjusted budget of the movie in term of 2010 dollars, accounting for inflation other time.
* revenue_adj: the adjusted revenue of the movie in term of 2010 dollars, accounting for inflation other time.

### Questions for this analysis: 
* Have movies (length, budget and revenue) changed with time?
* Is there a relationship between movie's lenght, budget and revenue?
* How are of movie's length, budget and year of release in general?
* Is a movie's popularity related to its propriety (year of release, length and budget)?

## Data cleaning
There are 21 columns in the data set, some of them are not useful in our investigation that we will drop out. Those are:

> * imdb_id.
> * cast.
> * homepage.
> * director.
> * tagline.
> * keywords.
> * overview.
> * genres.
> * production_companies.
> * release_date.

**Cleaning step 1:** indentifying and cleaning the duplicated data

**Cleaning step 2:** Conversion of the data type in the columns: budget_adj and revenue_adj

**Cleaning step 3:** replacing of budget, budget_adj, revenue, revenue_adj and runtime equal to 0 into nan
__Explanation: for some rows, the runtime, budget or revenue are zero, which is anormal. We can assume that those zero represent 'missing data'. We can't keep them as zero because it will affect the statistics we are going to compute in out analysis. (for example: the mean). So, we will convert them into nan. Then, we could drop the row with missing value, but in consequence, we will lose the informations in the other columns. Also, we can replace the missing value with the mean (for example), but given the proportion of missing value and the fact that we would do calculation year by year, it is better to keep them missing and just ignoring them in the calculation. (Remark: in the case of revenue, it can happen that the zero is normal given that the movie have been distributed for free. However, given that there was 6000 revenue equal to zero, we will simplify those zero as missing value)__