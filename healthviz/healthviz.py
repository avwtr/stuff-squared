import streamlit as st
from streamlit_lottie import st_lottie
from lottie import load_lottie
from database import workout_df
from database import mh_df
from database import food_df
import pandas as pd

def render_healthviz(name, username):

    user_workout_df = workout_df()
    user_workout_df = user_workout_df[user_workout_df["user"] == username]

    user_mh_df = mh_df()
    user_mh_df = user_mh_df[user_mh_df["user"] == username]

    user_food_df = food_df()
    user_food_df = user_food_df[user_food_df["user"] == username]
    

    h1, h2, h3 = st.columns(3)
    with h1:
        st.write("")
    with h2:
        st.image("assets/newlogo.png")
    with h3:
        st.write("")
    st.header("My Dashboard")
    lottie = load_lottie("lottie/charts.json")
    st_lottie(lottie, height = 150 , width = 150,key = "chart", speed = 0.7)

    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Fitness", "Diet", "Mental Health"])

    with tab1:

        lists = [user_workout_df["date"], user_mh_df["datetime"], user_food_df["datetime"]]
        months = []
        counts = []
        for i in lists: 
            for j in i: 
                month = j.split("-")[1]
                months.append(month)
        num_entries_nov = len(months)
        counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, num_entries_nov, 0]
        actual_months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]


        st.write("")
        col1, col2, col3 = st.columns(3)
        with col1: 
            st.metric("Number of workouts logged", len(user_workout_df))
        with col2: 
            st.metric("Number of calories burned", sum(user_workout_df["calories_burned"]))
        with col3:
            total_entries = len(user_workout_df) + len(user_food_df) + len(user_mh_df)
            st.metric("Total Entries made on Healthviz", total_entries)
        st.write("")
        st.write("")
        st.write("")
        ch1, ch2, ch3 = st.columns(3)
        with ch2: 
            st.write("Total Activity Per Month")
        chart_df = pd.DataFrame({"Month": actual_months, "Total Number of Entries": counts})
        st.line_chart(chart_df, x = "Month", y = "Total Number of Entries")
    with tab2:
        tcol1, tcol2, tcol3 = st.columns(3)
        
        num_cardio = len(user_workout_df[user_workout_df["workout_type"] == "Cardio"])
        num_strength = len(user_workout_df[user_workout_df["workout_type"] == "Strength"])
        num_rec = len(user_workout_df[user_workout_df["workout_type"] == "Recreation"])
        with tcol1:
            st.metric("Number of Cardio Sessions", num_cardio)
        with tcol2: 
            st.metric("Number of Strength Sessions", num_strength)
        with tcol3:
            st.metric("Number of Recreation Sessions", num_rec)

        st.write("")
        st.write("")
        st.write("")
        st.write("")
        fit_b1, fit_b2, fit_b3 = st.columns(3)

        with fit_b2: 
            st.write("Number of Sessions per Workout Type")
        fitness_bar_data = pd.DataFrame({"Workout Type": ["Cardio", "Strength", "Recreation"], "Number of Sessions": [num_cardio, num_strength, num_rec]})
        st.bar_chart(fitness_bar_data, x = "Workout Type", y = "Number of Sessions")

        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write("My Workout Logs:")
        st.dataframe(user_workout_df.drop(columns = ["key", "user"]))


    with tab3:
        

        num_carbs = sum(user_food_df["carbs"])
        num_fat = sum(user_food_df["fat"])
        num_protein = (sum(user_food_df["protein"]))
    
        f1, f2, f3 = st.columns(3)
        
        with f1:
            st.metric("Meals Logged", len(user_food_df))
        with f2:
            st.metric("Total Calories Consumed", sum(user_food_df["num_cals"]))
        with f3:
            try: 
                st.metric("Average Calories Per Meal", sum(user_food_df["num_cals"]) / len(user_food_df["num_cals"]))
            except: 
                st.metric("Average Calories Per Meal", "No entries found yet")
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write("Macro Nutrient Consumption Breakdown (g)")

        macros_df = pd.DataFrame({"Macro-nutrient": ["Carbs", "Fat", "Protein"], "Grams Consumed": [num_carbs, num_fat, num_protein]})
        st.bar_chart(macros_df, x = "Macro-nutrient", y = "Grams Consumed")




        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write("My Diet Logs:")
        st.dataframe(user_food_df.drop(columns = ["key", "user"]))

    with tab4:

        try: 
            avg_mh = sum(user_mh_df["scale_feeling"]) / len(user_mh_df)
        except: 
            avg_mh = 0
        
        t4col1, t4col2, t4col3 = st.columns(3)
        with t4col1:
            st.metric("Average Feeling Score", avg_mh)
        with t4col2: 
            flattened = []
            for i in user_mh_df["emotions"]:
                for j in i : 
                    flattened.append(j)
            if len(user_mh_df) > 0: 
                def most_frequent(arr):
                    return max(set(arr), key = arr.count)
                st.metric("Most Common Feeling", most_frequent(flattened))
            else: 
                pass
        with t4col3: 
            st.metric("Number of Mental Health Entries", len(user_mh_df))

        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write("My Mental Health Logs:")
        st.dataframe(user_mh_df.drop(columns = ["key", "user"]))
        #feeling_types = user_mh_df.groupby("emotions").size().plot()

