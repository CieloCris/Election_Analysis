# Election Analysis

## Project Overview

In this challenge, we performed an analysis and a report of the results of a local Congressional Election in Colorado using Python and Visual Studio Code. Our job was to help Tom, a Colorado Board Election employee, who had given us the task of analyzing a CSV file format with the election results.

In other words, our purpose was to make a report of the election in the counties of Denver, Jefferson, and Arapahoe. We'll be reporting the total numbers of the votes cast, the total number of votes each candidate received, the percentages of votes for each candidate, and the winner of the election based on popular votes.

## Resources
We perform an analysis with Python 3.9.7 and VS Code 1.66.1 using a CSV file to report the election results.
  * Data Source: election_results.csv
  * Data size: 369,712 rows and 3 columns (Ballot ID, County and Candidate)
  * Software: Python 3.9.7, Visual Studio Code version 1.66.1


## Summary

The analysis of the election shows that there were **369,711 votes cast** in the election.

The running candidates of the election and their results were:
  * **Charles Casper Stockham** received 85,213 votes, which was 23.0% of the total votes.
  * **Diana DeGette** received 272,892, which was 73.0% of the total votes.
  * **Raymon Anthony Doane**, received 11,606 votes, which was 3.1% of the total votes.

The winner of the election was **Diana DeGette** with **272,892 of 369,711 votes**, which represents **73.8%** of the total votes.

There were three counties where the election was held and the results of voter turnout were:
  * **Jefferson County** had 38,855 voters and 10.5% of the total votes.
  * **Denver County** had 306,055 voters and 82.8% of the total votes.
  * **Arapahoe County** had 24,801 voters and 6.7% of the total votes.

The County with the highest voter turnout was **Denver**, with **307,055 voters** and **82.8% of the total votes**.

The following screenshot shows the election results printed in the command line:

![Alt text](/Resources0/electionresults.png "imagen1")

## Election-Audit Summary

The Python script that we utilized to analyze the election results can be used in the performance of future elections. That is, the code can be adapted for not only local but also state and federal elections.

In other words, we can customize the code according to the requirements of each election. For example, we can analyze a federal election and report the results for each State in a similar way as we did for counties, but with some specific modifications. This Python script can also be adjusted for elections in other countries.

The use of this script is convenient because it provides a lot of information in a short time and adapts according to the needs of the election. It's important to highlight that using programming languages such as Python in electoral processes is practical, safer and, allows fewer errors and  transparency in the analysis.

## Challenge Overview and Summary

This project allowed us to understand the fundamentals of Python and its utility in the field of data analysis. In this challenge, we expanded the code for researching voter turnout by county. The adjustments to the code allowed us to extend the analysis, which still can improve more by reporting the percentage of votes for each candidate in each county and the winning candidate by county (for that, we can use for loops and if-statements).

Finally, the image bellow shows the text file with the election results:

![Alt text](/Resources0/textfile.png "imagen0")
