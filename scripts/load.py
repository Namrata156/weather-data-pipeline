from sqlalchemy import create_engine

def save_to_postgres(df):
    db_user = "weather_user"
    db_password = "weather_pass"
    db_host = "localhost"
    db_port = "5432"
    db_name = "weather_pipeline"
    table_name = "weather"

    engine = create_engine(
        "postgresql+psycopg2://weather_user:weather_pass@host.docker.internal:5432/weather_pipeline"  
    )

    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
    print(f"Data saved to PostgreSQL table: {table_name}")


    
