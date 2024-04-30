import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    tc = len(df.index)
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    rl = list(set(df['race']))
    race_count = pd.Series([df['race'].loc[df['race']==c].count() for c in rl], index = rl)
    

    # What is the average age of men?
    average_age_men = np.round(df['age'].loc[df.sex == 'Male'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = np.round(100* df['education'].loc[df['education'] == 'Bachelors'].count()/tc,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    ec = (df['education'] == 'Bachelors').combine(
        df['education'] ==  'Masters', max).combine(
        df['education'] ==  'Doctorate', max)
    higher_education = ec.sum()
    lower_education = (~ec).sum()
    # percentage with salary >50K
    higher_education_rich = df['salary'].loc[ec].loc[df['salary'] == '>50K'].count()/higher_education*100
    higher_education_rich = np.round(higher_education_rich,1)
    lower_education_rich = df['salary'].loc[~ec].loc[df['salary'] == '>50K'].count()/lower_education*100
    lower_education_rich = np.round(lower_education_rich,1)
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours].shape[0]

    rich_percentage = 100*df.loc[df['hours-per-week'] 
                             == min_work_hours].loc[df['salary'] == '>50K'].shape[0]/num_min_workers

    # What country has the highest percentage of people that earn >50K?
    lc = list(set(df['native-country']))
    ce = pd.Series({cn: 100*
                    df.loc[df['native-country']==cn].loc[df['salary'] == '>50K'].shape[0]
                    /df.loc[df['native-country']==cn].shape[0]
                    for cn in lc})
    highest_earning_country = ce.loc[ce == ce.max()].index[0]
    highest_earning_country_percentage = ce.loc[ce == ce.max()][0]
    highest_earning_country_percentage = np.round(highest_earning_country_percentage,1)
    # Identify the most popular occupation for those who earn >50K in India.
    ocl = list(set(df['occupation']))
    inr = df.loc[df['native-country']=='India'].loc[df['salary'] == '>50K']
    inocp = pd.Series({oc: inr.loc[inr['occupation'] == oc].shape[0]  for oc in ocl})
    top_IN_occupation = inocp.loc[inocp == inocp.max()].index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

if __name__ == '__main__':
    calculate_demographic_data()