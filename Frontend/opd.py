import mysql.connector
import streamlit as st
import pandas as pd

mydb = mysql.connector.connect(
host="localhost", user="root", password="vanshika")
c = mydb.cursor()
c.execute("USE HOSPITAL_MANAGEMENT_484")


def opd():
    tab1, tab2, tab3 = st.tabs(["Patient ID", "Department", "Doctor ID"])
    with tab1:
        with st.form(key='OPD_ID'):
            patient_id = st.text_input(label='Enter Patient ID')
            submit_button = st.form_submit_button(label='Submit')
        result = view_all_data_patient(patient_id)
        df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Doctor_id', 'Department', 'Medication', 'Procedure_done', 'Appointment_date'])
        st.dataframe(df)

    with tab3:
        with st.form(key='OPD_DID'):
            doctor_id = st.text_input(label='Enter Doctor ID')
            submit_button = st.form_submit_button(label='Submit')
        result = view_all_data_doctor(doctor_id)
        df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Doctor_id', 'Department', 'Medication', 'Procedure_done', 'Appointment_date'])
        st.dataframe(df)

    with tab2:
        with st.form(key='OPD_Dept'):
            department = st.text_input(label='Enter Department Name')
            submit_button = st.form_submit_button(label='Submit')
        result = view_all_data_department(department)
        df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Doctor_id', 'Department', 'Medication', 'Procedure_done', 'Appointment_date'])
        st.dataframe(df)

    st.subheader("Update Details")
    list_of_patients = [i[0] for i in view_only_patient_names()]
    selected_patient = st.selectbox("Patient Details to Edit", list_of_patients)
    result = get_details(selected_patient)
    st.text("Orginal Details of Patient: {}".format(selected_patient))
    df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Doctor_id', 'Department', 'Medication', 'Procedure_done', 'Appointment_date'])
    st.dataframe(df)

    if result:
        Department = result[0][3]
        new_Department = st.text_input("Department:", Department)

    if st.button("Update Patient Details"):
        edit_details_opd(new_Department, selected_patient)
        st.success("Successfully updated: {}".format(selected_patient))


def view_all_data_patient(patient_id):
    c.execute('SELECT * FROM Outpatient_dept WHERE Patient_id="{}"'.format(patient_id))
    data = c.fetchall()
    return data

def view_all_data_department(department):
    c.execute('SELECT * FROM Outpatient_dept WHERE Department="{}"'.format(department))
    data = c.fetchall()
    return data

def view_all_data_doctor(doctor_id):
    c.execute('SELECT * FROM Outpatient_dept WHERE Doctor_id="{}"'.format(doctor_id))
    data = c.fetchall()
    return data

def edit_details_opd(new_Department, selected_patient):
    query= "UPDATE Outpatient_dept SET Department=%s WHERE Patient_name=%s"
    c.execute(query,(new_Department,selected_patient))
    mydb.commit()
    data = c.fetchall()
    return data

def view_only_patient_names():
    c.execute('SELECT Patient_name FROM Outpatient_dept')
    data = c.fetchall()
    return data

def get_details(Patient_name):
     c.execute('SELECT * FROM Outpatient_dept WHERE Patient_name="{}"'.format(Patient_name))
     data = c.fetchall()
     return data


if __name__ == '__opd__':
    opd()