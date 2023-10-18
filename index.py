import streamlit as st
from PIL import Image


# Set page config to wide layout
st.set_page_config(layout="wide")
# Set the background image

#'https://images.unsplash.com/photo-1687120096244-ca75c057e5ef?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTY5NzU2ODI1NA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1080'
# CSS styles
bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url('https://images.unsplash.com/photo-1687120096244-ca75c057e5ef?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTY5NzU2ODI1NA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1080');
background-size: cover;
background-repeat: no-repeat;
}
</style>
'''
#https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17
#https://www.gettyimages.ca/detail/photo/splashed-with-fresh-air-royalty-free-image/1127069296?adppopup=true
#WQD6TCLOozg
st.markdown(bg_img, unsafe_allow_html=True)
#st.title('Air Quality Analysis')
st.markdown(f'<h1 style="color:#336BFF;font-size:45px;">{"BreezoScan"}</h1>', unsafe_allow_html=True)
st.markdown('**Breathing Innovation: Empowering Lives with Precision Air Quality Analysis.**')
#st.markdown("**Celebrating Clean Air: Welcome to our revolutionary Air Quality Analyzer website. Our mission is to empower individuals, communities, and businesses with accurate and real-time data about the air they breathe. We understand the vital importance of clean air for overall well-being, and our advanced analyzers are designed to provide precise, actionable insights. Whether you're a concerned parent, an eco-conscious professional, or a city planner aiming for sustainable urban environments, our website serves as your comprehensive resource. Explore our website to make informed decisions about your environment. Together, let's pave the way for a healthier, cleaner world.**")

#image = Image.open('/Users/sahanamanjunath/Downloads/girl-transformed.jpg')
#st.image(image, caption='Breathing Innovation: Empowering Lives with Precision Air Quality Analysis.')
st.markdown("**Welcome to our Air Quality Analyzer website. Our mission is to empower individuals, communities, and businesses with accurate and real-time data about the air they breathe. We understand the vital importance of clean air for overall well-being, and our advanced analyzers are designed to provide precise, actionable insights. Whether you're a concerned parent, an eco-conscious professional, or a city planner aiming for sustainable urban environments, our website serves as your comprehensive resource. Explore our website by clicking on the  'Analysis Dashboard' button to make informed decisions about your environment. Together, let's pave the way for a healthier, cleaner world.**")
def redirect_to_streamline():
    # Run the other Streamlit script for the streamline page
    #st.markdown('Hii')
    import subprocess
    subprocess.run(["streamlit", "run", "proj_1.py"])




st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color:#336BFF;margin-top: 40px;">
  <a class="navbar-brand" href="#" target="_blank">BreezoScan</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active"">
        <a class="nav-link" href="https://project1-iask7czzyejqmxy8tfaimn.streamlit.app"  target="_blank">Air Quality Predition</a>
      </li>
      <li class="nav-item active"">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Researcher Login</a>
      </li>
        <li class="nav-item active"">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Contact Us</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

st.markdown(bg_img, unsafe_allow_html=True)

def redirect_to_streamline():
    # Run the other Streamlit script for the streamline page
    #st.markdown('Hii')
    import subprocess
    subprocess.run(["streamlit", "run", "proj_1.py"])

if st.button('Analysis Dashboard'):
    redirect_to_streamline()
    




