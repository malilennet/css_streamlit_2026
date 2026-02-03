import streamlit a
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name = "Maqhawe Lennet Mali"
field = "Astrophysics"
institution = "Witswaterand University"

# Display basic profile information
st.header("Astrophysicists Study")
st.write(f"**Maqhawe Lennet Mali:** {name}")
st.write(f"**Astronomy of the universe:** {field}")
st.write(f"**Wits Physics and Science center:** {institution}")

st.image(
    "https://news.cnrs.fr/articles/james-webb-illuminates-the-grey-areas-of-astrophysics",
    caption="Astrophysics (CNRS)"
)

# Add a section for publications
st.header("Astrophysicists Study")
uploaded_file = st.file_uploader("Obsevervational vs Theoretical Astrophysics", type="csv")

if uploaded_file:
    publications = pd.read_csv(Stars)
    st.dataframe(Obsevational Astrophysics)

   elif data_option == "Astronomy Observations":
    st.write("Exoplanets Astronomy Observation Data")
    st.dataframe(Extreme Ojects )
    # Add widget to filter by Brightness
    brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
    filtered_astronomy = astronomy_data[
        astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
# Add a contact section
st.header("Contact Information")
email = "malilennet@yahoo.com"

st.write(f"You can reach {Maqhawe} at {malilennet@yahoo.com}.")
h







