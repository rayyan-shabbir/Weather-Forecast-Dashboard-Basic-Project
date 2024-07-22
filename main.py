import streamlit as st
import plotly.express as px
from backend import get_data


# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for next {days} days in {place}")


if place:
    # Get temperature/Sky data
    try:
        filtered_data = get_data(place, days)


        # Create Temperature Plot
        if option == "Temperature":
            temperatures = [dic["main"]["temp"] / 10 for dic in filtered_data]
            dates = [dic["dt_txt"] for dic in filtered_data]

            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Snow": "images/snow.png", "Rain": "images/rain.png"}
            sky_conditions = [dic["weather"][0]["main"] for dic in filtered_data]

            image_paths = [images[condition] for condition in sky_conditions]
            

            st.image(image_paths, width=115)

    except KeyError:
        st.write("That place does not exists.")
