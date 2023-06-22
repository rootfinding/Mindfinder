import ast
import json
import pandas as pd

def clean_salary(df):
    for index, _ in df.iterrows():
        val = df.at[index, 'salary']
        transformed_val = val.replace(',', '').replace('$', '').split('\r')[0]
        df.at[index, 'salary'] = int(transformed_val.split('.')[0])
    return df

def process_location(df):
    df[['location_city', 'location_state']] = df['location'].str.split(', ', expand=True)
    df.drop('location', axis=1, inplace=True)
    return df

def process_criteria(df):
    df['criteria'] = df['criteria'].apply(ast.literal_eval)
    df[['Seniority level', 'Employment type', 'Job function', 'Industries']] = \
        df['criteria'].apply(lambda x: pd.Series({k: v for d in x for k, v in d.items()}))
    df.drop('criteria', axis=1, inplace=True)
    return df

def drop_na(df):
    df.dropna(inplace=True)
    return df

if __name__ == "__main__":

    # df_africa = pd.read_csv('./data/linkedin/job_posting/linkedin-jobs-africa.csv')
    # df_canada = pd.read_csv('./data/linkedin/job_posting/linkedin-jobs-canada.csv')
    df_usa = pd.read_csv('./data/linkedin/job_posting/linkedin-jobs-usa.csv')

    df_usa = df_usa[["title", "company", "description", "onsite_remote", "salary", "location", "criteria", "posted_date", "link"]]
    df_usa = drop_na(df_usa)
    df_usa = clean_salary(df_usa)
    df_usa = process_location(df_usa)
    df_usa = drop_na(df_usa)
    df_usa = process_criteria(df_usa)
    df_usa = drop_na(df_usa)
    df_usa.reset_index(drop=True, inplace=True)
    gb_cnt = 1
    out_json = []
    for index, row in df_usa.iterrows():
        out_json.append({
            "id": gb_cnt,
            "title": df_usa.at[index, 'title'],
            "company": df_usa.at[index, 'company'],
            "description": df_usa.at[index, 'description'],
            "onsite_remote": df_usa.at[index, 'onsite_remote'],
            "salary": df_usa.at[index, 'salary'],
            "location_city": df_usa.at[index, 'location_city'],
            "location_state": df_usa.at[index, 'location_state'],
            "Seniority level": df_usa.at[index, 'Seniority level'],
            "Employment type": df_usa.at[index, 'Employment type'],
            "Job function": df_usa.at[index, 'Job function'],
            "Industries": df_usa.at[index, 'Industries'],
            "posted_date": df_usa.at[index, 'posted_date'],
            "link": df_usa.at[index, 'link'],
        })
        gb_cnt += 1
    
    with open('./data/linkedin/job_posting.json', 'w') as f:
        json.dump(out_json, f, indent=4)
