import pandas as pd

def demographic_data_analyzer():
    # Load the dataset
    df = pd.read_csv('adult.data.csv', header=None, names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education-num', 
        'marital-status', 'occupation', 'relationship', 'race', 
        'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 
        'native-country', 'salary'
    ])

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1
    )

    # 4. Percentage of people with advanced education (Bachelors, Masters, or Doctorate) that make more than 50K
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round(
        (df[advanced_education & (df['salary'] == '>50K')].shape[0] /
         df[advanced_education].shape[0]) * 100, 1
    )

    # 5. Percentage of people without advanced education that make more than 50K
    lower_education = ~advanced_education
    lower_education_rich = round(
        (df[lower_education & (df['salary'] == '>50K')].shape[0] /
         df[lower_education].shape[0]) * 100, 1
    )

    # 6. Minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of people who work minimum hours and earn >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] /
         num_min_workers.shape[0]) * 100, 1
    )

    # 8. Country with the highest percentage of people earning >50K
    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country = (
        (rich_country_counts / country_counts).idxmax()
    )
    highest_earning_country_percentage = round(
        (rich_country_counts / country_counts).max() * 100, 1
    )

    # 9. Most popular occupation for those earning >50K in India
    india_top_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    # Prepare the results
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'india_top_occupation': india_top_occupation
    }
