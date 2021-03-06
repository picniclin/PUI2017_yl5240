<b>a. verify that their Null and alternative hypotheses are formulated correctly</b>
The Null and alternative hypotheses are formulated appropriately. The only suggestion is to do a descriptive analysis in order to better define longer riding duration. For example, you can calculate the lower 25% or the average of the riding duration for both male and females. Then set two different thresholds for both genders since men may genetically ride much longer distance than women does on average. For example, riding bikes 30 minutes may be long for women but not for men.

<b>b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)</b>
One column “trip_more_than_30_min” is added to the table as a dummy variable and all the irrelevant variables get eliminated. Good job!


<b>c. chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.</b>

According to the article ‘How to choose the right statistical test?’, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3116565/, we need to answer a first question: Is there a difference between groups that are unpaired? Groups or data sets are regarded as unpaired if there is no possibility of the values in one data set being related to or being influenced by the values in the other data sets. The riding duration for male group is theoretically independent from the one for female group, so that the two groups are unpaired and I proceed the figure 1 and determine what type of data the analysis is tackling with. Since we measure the number of trips longer than 30 minutes as a percentage of number of trips in total for each sex group, the data in this case is numerical data. Furthermore, there are only two groups to analyze, 0 for man and 1 for women’. According to the figure 1, if there are only two groups in the dataset, we should use <b>2 groups unpaired t test</b>

# FBB good (consider though that the t test is parametric and the distrbutions may not cply to the assumptions)
