from deta import Deta
import os
import pandas as pd
#from dotenv import load_dotenv

DETA_KEY = os.environ.get('DETA_KEY')
deta = Deta(DETA_KEY)
db = deta.Base("health_users_db")

mh_deta = Deta(DETA_KEY)
mh_db = mh_deta.Base("mh_data")

food_deta = Deta(DETA_KEY)
food_db = food_deta.Base("food_data")

body_deta = Deta(DETA_KEY)
body_db = body_deta.Base("body_data")

workout_deta = Deta(DETA_KEY)
workout_db = workout_deta.Base("workout_data")



#users database
def insert_user(username, name, password, phone_num, date_created):
    return db.put({"key": username, "name": name, "password": password, 
                    "phone": phone_num, "date-created": date_created})
def fetch_users():
    res = db.fetch()
    return res.items

def user_df():
    df = pd.DataFrame.from_dict(fetch_users())
    return df

def delete_user(username):
    return db.delete(username)

def update_user(username, updates):
    return db.update(updates, username)

def get_user(username):
    return db.get(username)

#mental health database
def insert_mh(log_num_username, username, scale_feeling, emotions, note, datetime):
    return mh_db.put({"key": log_num_username, "user": username ,"scale_feeling": scale_feeling, "emotions": emotions, "note": note, "datetime": datetime})

def get_mh(username):
    return mh_db.get(username)

def fetch_mh():
    res = mh_db.fetch()
    return res.items

def mh_df():
    df = pd.DataFrame.from_dict(fetch_mh())
    return df

#food database
def insert_food(log_num_username, username,date, time, meal_type, liq_or_solid, food_name, num_cals, protein, fat, carbs, datetime): 
    return food_db.put({"key": log_num_username,"user": username, "date": date, "time": time, "meal_type": meal_type, "liq_or_solid": liq_or_solid, 
                        "food_name": food_name, "num_cals": num_cals, "protein": protein, "fat": fat, "carbs": carbs, "datetime": datetime})

def get_food(username):
    return food_db.get(username)

def fetch_food():
    res = food_db.fetch()
    return res.items

def food_df():
    df = pd.DataFrame.from_dict(fetch_food())
    return df

#body database
def insert_body(workout_num_username, user, weight, lean_muscle, body_fat_percentage, datetime):
    return body_db.put({"key": workout_num_username, "user": user ,"current_weight": weight, "lean_muscle": lean_muscle, 
                        "body_fat_percentage": body_fat_percentage, "datetime": datetime})

def get_body(datetime):
    return body_db.get(datetime)

def fetch_body():
    res = body_db.fetch()
    return res.items

def body_df():
    df = pd.DataFrame.from_dict(fetch_body())
    return df


#workout db
def insert_workout(key, username, date, time_started, time_finished, workout_type, sub_activity, calories_burned, sub_activity_metric, intensity_level):
    return workout_db.put({"key": key, "user": username, "date": date, "time_started": time_started, "time_finished": time_finished,
                        "workout_type": workout_type, "sub_activity": sub_activity, "calories_burned": calories_burned,
                        "sub_activity_metric": sub_activity_metric, "intensity_level": intensity_level})

def get_workout(datetime):
    return workout_db.get(datetime)

def fetch_workouts():
    res = workout_db.fetch()
    return res.items

def workout_df():
    df = pd.DataFrame.from_dict(fetch_workouts())
    return df


