import json
import streamlit as st
from streamlit_lottie import st_lottie
col1, col2 = st.columns(2)
with col1:

    st.markdown("""## Tinder Lite""")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)



with col1:
    lottie_now = load_lottiefile("file/code.json")
st_lottie(
    lottie_now,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    height=400,
    key=None,

)
st.subheader("Welcome to Tinder Lite")

user_name = st.text_input("Your name ")

crush_name = st.text_input("Your crush name ")

date_of_birth = st.text_input("Date of birth of your Crush (DD/MM/YYYY)? ")


if date_of_birth.strip() != "":
    love_score = 15


else:
    love_score = 0
    dob_answer = st.text_input("Do you Know your crush's date of birth? (y/n) ").lower()
    if dob_answer == "y":
        love_score += 5
    elif dob_answer == "Y":
        love_score += 5
    elif dob_answer == "Yes":
        love_score += 5
    elif dob_answer == "yes":
        love_score += 5

    else:
        love_score -= 5


your_color = st.text_input("What's your favorite color? ")


crush_color = st.text_input("What's your crush's favorite color? ")


if crush_color.strip() != "":
    love_score += 5


else:
    color_answer = st.text_input(
        "You know Your crush's favorite color? (y/n) ").lower()
    if color_answer == "y":
        love_score += 5
    elif color_answer == "Y":
        love_score += 5
    elif color_answer == "Yes":
        love_score += 5
    elif color_answer == "yes":
        love_score += 5

    else:
        love_score += 5


if crush_color == your_color:
    love_score += 10

last_time_met = st.text_input("When was the last time you saw your crush? ")


if last_time_met.strip() != "":
    love_score += 5


else:
    last_time_answer = st.text_input(
        "Do You remember when you saw your crush last time? (y/n) ").lower()

    if last_time_answer == "y":
        love_score += 5
    else:
        love_score -= 5


crush_knowledge = st.text_input(
    "Does your crush know that you like them? (y/n) ").lower()


if crush_knowledge == "y":
    love_score += 10


else:
    love_score -= 10


crush_likes = st.text_input("What does your crush like? ")


if crush_likes.strip() != "":
    love_score += 5


else:
    crush_likes_answer = st.text_input(
        "Do You know what your crush likes? (y/n) ").lower()

    if crush_likes_answer == "n":
        love_score -= 15


user_dob = st.text_input("Your date of birth (DD/MM/YYYY)? ")


if user_dob.strip() != "":

    user_dob_year = int(user_dob.split("/")[2]
                        )

    crush_dob_year = int(date_of_birth.split("/")[2])

    if user_dob_year < crush_dob_year:
        love_score += 20


def shared_letters(name1, name2):
    score = 0
    for letter in name1:
        if letter in name2:
            score += 5
    return score


love_score += shared_letters(user_name, crush_name)


if user_name == "Sudhanshu" and crush_name == "Kajal":
    st.success("Bestest couple in the world!")
    st.success("You two are a greatest match!")
    st.success("Your love score is:")
    st.success(love_score+1000)
    st.success(("Matching Percentage= ",(love_score+1000)/(1050)*100,"%"))

elif user_name == "sudhanshu" and crush_name == "kajal":
    st.success("Bestest couple in the world!")
    st.success("You two are a greatest match!")
    st.success("Your love score is:")
    st.success(love_score+1000)
    st.success(("Matching Percentage= ",(love_score+1000)/(1050)*100,"%"))

elif user_name == "SUDHANSHU" and crush_name == "KAJAL":
    st.success("Bestest couple in the world!")
    st.success("You two are a greatest match!")
    st.success("Your Matching score is:")
    st.success(love_score+1000)
    st.success(("Matching Percentage= ",(love_score+1000)/(1050)*100,"%"))



else:
    k = st.text_input("Do You want to answer more quetion about your crush(y/n) ")
    if k == "y":
        favorite_food = st.text_input("What's your crush's favorite food? ")
        if favorite_food.strip() != "":
            love_score += 10

        favorite_movie = st.text_input("What's your crush's favorite movie? ")
        if favorite_movie.strip() != "":
            love_score += 10

        favorite_music = st.text_input("What's your crush's favorite music genre? ")
        if favorite_music.strip() != "":
            love_score += 10

        favorite_hobby = st.text_input("What's your crush's favorite hobby? ")
        if favorite_hobby.strip() != "":
            love_score += 10

        favorite_animal = st.text_input("What's your crush's favorite animal? ")
        if favorite_animal.strip() != "":
            love_score += 10

        favorite_book = st.text_input("What's your crush's favorite book? ")
        if favorite_book.strip() != "":
            love_score += 10

            favorite_sport = st.text_input("What's your crush's favorite sport? ")
        if favorite_sport.strip() != "":
                love_score += 10

        favorite_destination = st.text_input(
            "What's your crush's favorite holiday destination? ")
        if favorite_destination.strip() != "":
            love_score += 10
        st.success(("Your love score is:", love_score))

        if love_score >= 80:
            st.success("You two are a greatest match!")
            st.success(("Matching Percentage= ",(love_score)/(300)*100,"%"))

        elif love_score >= 50:
            st.success("You two are a great match!")
            st.success(("Matching Percentage= ",(love_score)/(300)*100,"%"))

        else:
            st.warning("You two might need more time to get to know each other.")

    else:
        st.success(("Your love score is:", love_score))

        if love_score >= 80:
            st.success("You two are a greatest match!")
            st.success(("Matching Percentage= ",(love_score)/(120)*100,"%"))

        elif love_score >= 50:
            st.success("You two are a great match!")
            st.success(('Matching Percentage = ',(love_score)/(120)*100,'%'))


        else:
            st.warning("You two might need more time to get to know each other.")
