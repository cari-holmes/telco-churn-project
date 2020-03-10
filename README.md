# Why are Telco customers churning?

https://docs.google.com/presentation/d/1f4nKEBKg8zAamgG6f0L8zCPL9DCXYYjJFpozDH7vBo4/edit?usp=sharing

#### Goals: Deliver a well-rounded analysis as to why customers are churning. Create multiple predictive models in which you will select you top performing model as your MVP, perform exploratory analysis and feature engineering. Summarize conclusions based on the explore and the models created.

To create your own predictive models, use the following .py files and use the functions necessary to run through the data.
- acquire.py 
- prepare.py 
- split_scale.py  
- feature_selection.py 

Specific Deliverables:

- jupyter notebook where your work takes place that will be delivered to others to read as a report.
- csv file that predicts churn for each customer
- acquire.py, prepare.py, model.py (you may decide to separate tasks into others, such as preprocessing.py or features.py)
- google slide summarizing your model

### Acquisition
I compiled a SQL query to pull the data necessary into a panad dataframe. In order to do this, I had to join tables together for the complete information needed to answer my question of why customers are churning.

### Preparation
There were several factors that needed to be taken into consideration when looking at the data pull in. I needed to handle any missing data as I felt appropriate, use feature engineering, encode certain features, scale the data, and finally split the data into a train anda test group.

### Exploration
Answer the following questions:

1. If a group is identified by tenure, is there a cohort or cohorts who have a higher rate of churn than other cohorts? (Plot the rate of churn on a line chart where x is the tenure and y is the rate of churn (customers churned/total customers))

2. Are there features that indicate a higher propensity to churn? like type of internet service, type of phone service, online security and backup, senior citizens, paying more than x% of customers with the same services, etc.?

3. Is there a price threshold for specific services where the likelihood of churn increases once price for those services goes past that point? If so, what is that point for what service(s)?

4. If we looked at churn rate for month-to-month customers after the 12th month and that of 1-year contract customers after the 12th month, are those rates comparable?

### Modeling
I used Select K-Best to determine which features provided my model with the best outcome as to whether or not customers would churn. I used a Decision Tree and a Random Forest model in this step.


