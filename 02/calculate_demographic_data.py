import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'].value_counts(normalize=True)['Bachelors']) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education_rich = (
        df[df['salary'] != '<=50k']['education'].value_counts(normalize=True)[['Bachelors', 'Masters', 'Doctorate']]
    ) * 100
    
    # What percentage of people without advanced education make more than 50K?
    a = (df['salary'] == '>50K').value_counts(normalize=False)

    total = (a[True] / len(df)) * 100
    lower_education_rich = total - higher_education_rich

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = higher_education_rich + lower_education_rich
    lower_education = lower_education_rich

    # percentage with salary >50K
    higher_education_rich = higher_education_rich
    lower_education_rich = lower_education_rich

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min() 

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df['hours-per-week'].value_counts(normalize=False)[min_work_hours]

    rich_percentage = df[df['salary'] == '>50K']['hours-per-week'].value_counts(normalize= False)[1]
    rich_percentage = (rich_percentage /len(df)) * 100

    # What country has the highest percentage of people that earn >50K?

    country_rich = df[df['salary'] == '>50K']['native-country'].value_counts()
    # print(country_rich)

    highest_earning_country = country_rich.idxmax()
    highest_earning_country_percentage = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=False)[highest_earning_country]

    highest_earning_country_percentage = highest_earning_country_percentage / len(df)
    highest_earning_country_percentage = highest_earning_country_percentage * 100


    # Identify the most popular occupation for those who earn >50K in India.
    filtered_df = df[
        (df['salary'] == '>50K') &
        (df['native-country'] == 'India')
    ]

    top_IN_occupation = filtered_df['occupation'].value_counts().idxmax()


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