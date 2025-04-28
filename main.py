import pandas as pd

def extract_movies_data(file_name):
    return pd.read_csv(file_name)

def validate_columns(data, required_columns):
    missing = [col for col in required_columns if col not in data.columns]
    if missing:
        raise ValueError(f"Lipsesc următoarele coloane din date: {missing}")

def transform_movies_data(data):
    required_columns = ['title', 'release_year', 'genre', 'director', 'box_office', 'budget', 'country']
    validate_columns(data, required_columns)

    data['box_office'] = pd.to_numeric(data['box_office'], errors='coerce')
    data['budget'] = pd.to_numeric(data['budget'], errors='coerce')
    data['bilant'] = data['box_office'] - data['budget']
    return data[['title', 'release_year', 'genre', 'director', 'bilant', 'country']]

def top_movies_by_country(data, country, n=10):
    country_data = data[data['country'] == country]
    top_films = country_data.nlargest(n, 'bilant')
    return top_films

def load_to_excel(data, country):
    file_name = f'top_movies_{country}.xlsx'
    data.to_excel(file_name, index=False)

def run_etl(file_name):
    data = extract_movies_data(file_name)
    transformed_data = transform_movies_data(data)
    countries = ['USA', 'Russia', 'UK', 'South Korea']
    
    for country in countries:
        top_movies = top_movies_by_country(transformed_data, country)
        if not top_movies.empty:
            load_to_excel(top_movies, country)

run_etl('Task_02-movies.csv')
