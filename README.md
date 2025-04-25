# Weather Data Pipeline with Airflow, Docker, and PostgreSQL 

This project builds a scalable and modular ETL pipeline to extract real-time weather data from the OpenWeatherMap API, transform it using Python, and load it into a PostgreSQL database. The workflow is orchestrated using Apache Airflow and runs on a fully Dockerized environment.

## Project Overview
* **Data Source:** OpenWeatherMap API

* **Tech Stack:** Apache Airflow, Docker Compose, PostgreSQL, Adminer, Python (Pandas, SQLAlchemy)

* **Schedule:** Every 3 hours

* **Database UI:** Adminer

* **Pipeline Type:** ETL (Extract, Transform, Load)

## How It Works
1. **Extract:** Weather data is pulled from the OpenWeatherMap API for specified cities

2. **Transform:**
Raw JSON is cleaned and structured — extracting temperature, humidity, wind speed, weather condition, and timestamps.

3. **Load:** The transformed data is inserted into a PostgreSQL table using SQLAlchemy.

4. **Schedule:**
Airflow schedules and monitors the ETL job to run every 3 hours.