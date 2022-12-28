import mysql.connector
import streamlit as st
import pandas as pd

mydb = mysql.connector.connect(
host="localhost", user="root", password="vanshika")
c = mydb.cursor()
c.execute("USE HOSPITAL_MANAGEMENT_484")

def sql_queries():
    with st.form(key='query_form'):
        raw_code = st.text_area(" Write SQL Queries Here")
        submit_code = st.form_submit_button("Execute")

    with st.expander("All Tables From HOSPITAL_MANAGEMENT_484"):

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["IPD","OPD","Medical Records", "Doctor", "Patient", "Appointments"])

        with tab1:
            result = view_all_data_ipd()
            df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Doctor_id', 'Room_no', 'Medication', 'Procedure_done', 'Date_of_admission', 'Date_of_discharge', 'Mode_of_payment', ' Department'])
            st.dataframe(df)
        
        with tab2:
            result = view_all_data_opd()
            df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Doctor_id', 'Department', 'Medication', 'Procedure_done', 'Appointment_date'])
            st.dataframe(df)
        
        with tab3:
            result = view_all_data_mr()
            df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Doctor_id', 'Medication', 'Investigations', 'Treatment_plan', 'Department', 'Cross_consulation_department'])
            st.dataframe(df)
            
        with tab4:
            result = view_all_data_doc()
            df = pd.DataFrame(result, columns=['Doctor_id', 'Doctor_name', 'Department', 'Designation', 'Age', 'Gender', 'House_address', 'Pincode', 'Phone_no', 'Email', 'Alternate_phone_number', 'Blood_group'])
            st.dataframe(df)
        
        with tab5:
            result = view_all_data_pat()
            df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Guardian_name', 'Age', 'Gender', 'Phone_no', 'House_address', 'Pincode', 'Blood_group', 'Emergency_contact', 'Aadhar_card_no', 'Email'])
            st.dataframe(df)
        
        with tab6:
            result = view_all_data_appt()
            df = pd.DataFrame(result, columns=['Appointment_date', 'Patient_name', 'Next_appt_date', 'Department', 'Patient_id'])
            st.dataframe(df)

    if submit_code:
        st.info("Query Submitted")
        st.code(raw_code)
        st.subheader("Results:")
        query_results=sql_executor(raw_code)
        query_df = pd.DataFrame(query_results)
        st.dataframe(query_df)

def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data    

def view_all_data_ipd():
    c.execute('SELECT * FROM Inpatient_dept;')
    data = c.fetchall()
    return data

def view_all_data_opd():
    c.execute('SELECT * FROM Outpatient_dept;')
    data = c.fetchall()
    return data

def view_all_data_mr():
    c.execute('SELECT * FROM Medical_records;')
    data = c.fetchall()
    return data

def view_all_data_appt():
    c.execute('SELECT * FROM Appointments;')
    data = c.fetchall()
    return data

def view_all_data_doc():
    c.execute('SELECT * FROM Doctor;')
    data = c.fetchall()
    return data

def view_all_data_pat():
    c.execute('SELECT * FROM Patient;')
    data = c.fetchall()
    return data
if __name__ == '__sql_queries__':
    sql_queries()