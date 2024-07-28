import streamlit as st
import requests

# Define your backend URL
backend_url = "http://127.0.0.1:8000/"

# Page configuration
st.set_page_config(
    page_title='Sepsis Prediction',
    page_icon='🚀',
    layout='wide'
)

st.title('SepsisAlert: An Early Detection Tool For Sepsis')
st.markdown("""
Welcome to the SepsisAlert App 🩺🚨

SepsisAlert is designed to help healthcare professionals quickly and accurately predict sepsis. Sepsis is a severe and
potentially life-threatening condition caused by the body's response to an infection, leading to organ dysfunction 
and septic shock. Early detection is critical for effective treatment and improved survival rates.

Key App Features:
- Quick Assessment: Input patient details and receive an immediate prediction of sepsis risk.
- User-Friendly Interface: Intuitive design makes it easy to navigate and use.
- Real-Time Data: Provides real-time analysis based on the latest medical guidelines and data.

Why SepsisAlert?
- Save Lives: Early detection and treatment can significantly increase survival rates.
- Reduce Healthcare Costs: Timely intervention can reduce the length of hospital stays and prevent complications.
- Empower Healthcare Providers: Equip medical staff with a reliable tool for early sepsis diagnosis.

How to Use the App:
- Enter Patient Details: Fill in the required patient information in the form below.
- Get Instant Results: Receive a sepsis risk prediction within seconds.
- Take Action: Use the results to make informed decisions about the next steps in patient care.

Ready to make a difference? Enter the patient’s details below and start the assessment now! 👇
""")

def show_form():
    st.header('Patient Details 💉')
    with st.form('patient-details'):
        col1, col2, col3 = st.columns(3)
        with col1:
            PRG = st.number_input('Plasma Glucose (PRG)', min_value=0, step=1)
            PR = st.number_input('Blood Pressure (PR)', min_value=0, step=1)
            M11 = st.number_input('M11', min_value=0, step=1)
        with col2:
            PL = st.number_input('1st Bloodwork Result (PL)', min_value=0, step=1)
            SK = st.number_input('2nd Bloodwork Result (SK)', min_value=0, step=1)
            TS = st.number_input('3rd Bloodwork Result (TS)', min_value=0, step=1)
        with col3:
            BD2 = st.number_input('4th Bloodwork Result (BD2)', min_value=0, step=1)
            Age = st.number_input('Age', min_value=21, step=1)
            Insurance = st.number_input('Insurance', min_value=0, max_value=1)
            
        submit_button = st.form_submit_button('Predict')
        
        if submit_button:
            input_data = {
                'PRG': PRG,
                'PL': PL,
                'PR': PR,
                'SK': SK,
                'TS': TS,
                'M11': M11,
                'BD2': BD2,
                'Age': Age,
                'Insurance': Insurance
            }
            
            try:
                response = requests.post(f"{backend_url}/predict_sepsis", json=input_data)
                response.raise_for_status()
                
                if response.status_code == 200:
                    prediction = response.json()['prediction']
                    st.session_state['prediction'] = prediction
                    st.session_state['message'] = f'The patient tested {prediction} for sepsis'
                    st.session_state['status'] = 'success'
                else:
                    st.session_state['message'] = f'Error: {response.json()["detail"]}'
                    st.session_state['status'] = 'error'
            except requests.exceptions.RequestException as e:
                st.session_state['message'] = f'Connection error: {e}'
                st.session_state['status'] = 'error'

if __name__ == '__main__':
    show_form()

    if 'message' in st.session_state:
        if st.session_state['status'] == 'success':
            st.success(st.session_state['message'])
        else:
            st.error(st.session_state['message'])