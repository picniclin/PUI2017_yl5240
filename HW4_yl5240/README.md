## 1. Assignment 1:Review your classmate's Citibike project proposal
- Fork Srikanth's repo [srikanth261/PUI2017_sn2495](https://github.com/srikanth261/PUI2017_sn2495)
- Review his HW3_Assignment's hypothesis and data processed
- Propose to take t test or Z test for his hypothesis according to his hypothesis and the data type of varialbes
- The two steps above is written down in a markdown file, which could be found [here](https://github.com/picniclin/PUI2017_sn2495/blob/master/HW3_sn2495/CitibikeReview_yl5240.md) 
- Submit a pull request to Srikanth's repo. The request has been merged, which could be found [here](https://github.com/srikanth261/PUI2017_sn2495/tree/master/HW3_sn2495).

## 2. Assignment 2:Literature choices of statistical tests

This assignment was done by team and each one did one choice of tests

't-Test' ChunChieh Tsai. NetID:cct367

'Path Analysis'. Ci He   NetID: ch3183

'Logistic Regression'. Yuwei Lin NetID:yl5240

Literature choices of statistical tests

**Statistical Analyses	IV(s)	IV type(s)	DV(s)	DV type(s)	Control Var	Control Var type	Question to be answered	H0	alpha	link to paper **
t-Test	1, types of music	categorical	1, mood condition	ordinary	2, lights, place	condition	Do participants who listening happy music are more creative than control group	Listen happy music groups divergent thinking <= control group	0.05	Happy creativity: Listening to happy music facilitates divergent thinking
path analysis	women age (X1), place of residence (X2), religion (X3), socioeconomic status (X4) and use of family planning methods (X5)	catogorical	women education (X6), age at first marriage (X7) and unwanted births (X8)	categorical	women whose most recent pregnancy occurred five years preceding the date of interview or women who were currently pregnant	catogorical	How women age (X1), place of residence (X2), religion (X3), socioeconomic status (X4) and use of family planning methods (X5) are directly or indirectly impact the DVs(women education (X6), age at first marriage (X7) and unwanted births (X8).Is there causal links between the socio-demographic variables ( women’s age, education, age at first marriage, religion, parity, residence, socioeconomic status, and use of family planning methods) and unwanted births in Bangladesh?	there is no causal correlation between the socio-demographic variables ( women’s age, education, age at first marriage, religion, parity, residence, socioeconomic status, and use of family planning methods) and unwanted births in Bangladesh	0.05	Hierarchy of Correlates of Unwanted Births in Bangladesh: A Study through Path Analysis
logistic regression	community size	counts	not critical/critical scalar stress	nominal	-	-	Could a predictive model of scalar stress be built to work when estimates of settlement population are available.	there is significant difference between what the model predicts and what the analyst observes in the data	0.05	Modeling Group Size and Scalar Stress by Logistic Regression from an Archaeological Perspective
**

## 3. Assignment 3 : Reproduce the analysis of the Hard to Employ program in NY

reproduce the result in http://www.mdrc.org/sites/default/files/What%20Strategies%20Work%20for%20the%20Hard%20FR.pdf
Use Z test and Chi-squared test to check the statistical difference between test sample and control sample.
The datasets has been analysized:
"Ever employed in a CEO transitional job" data
"Convicted of a felony after 3 years" data

## Assignment 4: Tests of correlation using the scipy package with citibike data

Use 3 tests to check is there statistical difference between two distribution. 
First, use KS test to check are they from the same continuous distribution.
Then, use Pearson’s test and Spearman’s test to check are they correlated.

Three comparison of 2-sample has been analysized seperatly:
- age of male vs female riders
- trip duration of bikers that ride during the day vs night
- age of bikers for trips originating in Manhattan and in Brooklyn

The results are similar:
the two distributions are highly correlatedare, but not from the same distribution.
