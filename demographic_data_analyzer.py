import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r'/workspace/boilerplate-demographic-data-analyzer/adult.data.csv')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df.loc[df['education']=='Bachelors'])/len(df['age'])*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[df['education'].isin(['Bachelors', 'Masters','Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich =round(len(higher_education.loc[higher_education['salary']=='>50K'])/len(higher_education)*100,1)
    lower_education_rich = round(len(lower_education.loc[lower_education['salary']=='>50K'])/len(lower_education)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df.loc[df['hours-per-week']==1])

    rich_percentage = round(len(df.loc[(df['hours-per-week']==1)&(df['salary']=='>50K')])/len(df.loc[df['hours-per-week']==1])*100)

    # What country has the highest percentage of people that earn >50K?
    count_sal = df.loc[df['salary'] == '>50K', ['native-country', 'age']].groupby('native-country').agg(
        'count').sort_values(by='age', ascending=False)
    count_sal.reset_index(inplace=True)

    # Adding a custom index (1-based index)

    highest_earning_country = count_sal.loc[0, 'native-country']

    temp = df.loc[:, ['native-country', 'age']].groupby('native-country').agg('count')
    temp.reset_index(inplace=True)
    temp1 = pd.merge(count_sal, temp, on='native-country')
    temp1['perc'] = temp1['age_x'] / temp1['age_y']
    temp1 = temp1.sort_values(by='perc', ascending=False)
    temp1.reset_index(inplace=True)
    highest_earning_country = temp1.sort_values(by='perc', ascending=False).loc[0, 'native-country']
    highest_earning_country_percentage = round(temp1.sort_values(by='perc', ascending=False).loc[0, 'perc'] * 100, 1)
    # Identify the most popular occupation for those who earn >50K in India.
    temp2 = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K'), 'occupation'].value_counts()
    temp2 = temp2.reset_index()

    top_IN_occupation =temp2.iloc[0, 0]

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
