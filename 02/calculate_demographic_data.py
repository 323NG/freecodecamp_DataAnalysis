import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'].value_counts(normalize=True)['Bachelors']) * 100, 1)

    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich_count = higher_education[higher_education['salary'] == '>50K'].shape[0]
    lower_education_rich_count = lower_education[lower_education['salary'] == '>50K'].shape[0]

    higher_education_rich = round((higher_education_rich_count / higher_education.shape[0]) * 100, 1)
    lower_education_rich = round((lower_education_rich_count / lower_education.shape[0]) * 100, 1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min() 

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hour_workers = df[df['hours-per-week'] == min_work_hours]

    rich_min_hour_workers = min_hour_workers[min_hour_workers['salary'] == '>50K'].shape[0]

    rich_percentage = round((rich_min_hour_workers / min_hour_workers.shape[0]) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    country_rich = df[df['salary'] == '>50K']['native-country'].value_counts()

    country_total = df['native-country'].value_counts()

    country_rich = df[df['salary'] == '>50K']['native-country'].value_counts()

    rich_percentage2 = (country_rich / country_total) * 100

    highest_earning_country = rich_percentage2.idxmax()
    highest_earning_country_percentage = round(rich_percentage2.max(), 1)


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