import streamlit as st;
from ipd import ipd;
from opd import opd;
from appointments import appointments;
from patient import patient; 
from doctor import doctor;
from medical_records import medical_records;
import mysql.connector;
from sql_queries import sql_queries;

st.set_page_config(layout='wide',initial_sidebar_state="expanded")
mydb = mysql.connector.connect(
host="localhost", user="root", password="vanshika")
c = mydb.cursor()
c.execute("USE HOSPITAL_MANAGEMENT_484")

def main():
    
    menu = ["About this Project", "Inpatient Department", "Outpatient Department", "Medical Records", "Appointment Details", "Doctor", "Patient", "Run SQL Queries"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice=="About this Project":
        st.title("Hospital Management System")
        st.header("About this Project")
        st.subheader('Vanshika Goel (PES1UG20CS484)')
        st.markdown('Hospital Management System has today become an indispensable part of any hospital/clinic/healthcare facility. This HMS is built from the perspective of a medical employee, for eg. doctor or a medical officer. This database has been built by connecting all the tables through foreign key constraints with the parent tables, Doctor and Patient. This ensures easier access to patient data, like Inpatient Department or Appointments. This can be expanded to all departments like Radiology and Pathology and also allow for easy access to reports or scans, without having to always switch between these tabs.')
        st.markdown("This was built after careful discussion with my parents, who are doctors by profession, keeping in mind, the expected functionalities, like Patient ID, a patient’s allergies, emergency contact details, etc.")
    
    elif choice == "Inpatient Department":
        st.title("Hospital Management System")
        st.subheader("Inpatient Department")
        ipd()

    elif choice == "Outpatient Department":
        st.title("Hospital Management System")
        st.subheader("Outpatient Department")
        opd()

    elif choice == "Medical Records":
        st.title("Hospital Management System")
        st.subheader("Medical Records")
        medical_records()

    elif choice == "Appointment Details":
        st.title("Hospital Management System")
        st.subheader("Appointment Details")
        appointments()
    
    elif choice == "Doctor":
        st.title("Hospital Management System")
        st.subheader("Doctor")
        doctor()

    elif choice == "Patient":
        st.title("Hospital Management System")
        st.subheader("Patient")
        patient()
    
    elif choice == "Run SQL Queries":
        st.title("Hospital Management System")
        st.subheader("Run SQL Queries")
        sql_queries()

    else:
        st.subheader("About tasks")

if __name__ == '__main__':
    main()
