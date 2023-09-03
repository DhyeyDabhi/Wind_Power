from model import *
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown(
    """
    <style>
    body {
        background-color: ##CDE6F7; /* Set your desired background color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.title("Wind Power Prediction")
    st.write("WindHack employs time-series forecasting and gradient boosting to predict output from a wind turbine for the coming time can predict power output for coming 1 hr upto 72 hrs. Implemented in PyTorch and CatBoost and served with streamlit.")

    x = st.slider('Prediction Hours: ',min_value=2,max_value=72,value=10,step=1)
    places = ['New Delhi,IN','Tokyo,JP','Mumbai,IN','Surat,IN','London,UK']
    loc = st.selectbox('Select a location: ',places)
    try:
        result = in_out(x,loc)

        vis_df = pd.DataFrame({'Days':range(1,len(result)+1),'Prediction':result})
        sns.set_style('darkgrid')
        plt = sns.lineplot(data=vis_df,x='Days',y='Prediction')
        st.pyplot(plt.figure)
    except:
        st.write("Not able to fetch the live weather data!")

with col2:
    st.text("")
    st.text("")
    st.image('pexels-pixabay-70846.jpg',use_column_width=True)



