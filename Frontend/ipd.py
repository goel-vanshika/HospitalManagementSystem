import mysql.connector
import streamlit as st
import pandas as pd

mydb = mysql.connector.connect(
host="localhost", user="root", password="vanshika")
c = mydb.cursor()
c.execute("USE HOSPITAL_MANAGEMENT_484")

# def add_data_patient(train_no, train_name, train_type, source, dest, available):
#     c.execute('INSERT INTO Train (Train_No, Name, Train_Type, Source, Destination, Availability) VALUES (%s,%s,%s,%s,%s,%s);',
#               (train_no, train_name, train_type, source, dest, available))
#     mydb.commit()

def ipd():
    tab1, tab2, tab3 = st.tabs(["Patient ID", "Department", "Doctor ID"])

    with tab1:
        with st.form(key='IPD_ID'):
            patient_id = st.text_input(label='Enter Patient ID')
            submit_button = st.form_submit_button(label='Submit')
        result = view_all_data_patient(patient_id)
        df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Doctor_id', 'Room_no', 'Medication', 'Procedure_done', 'Date_of_admission', 'Date_of_discharge', 'Mode_of_payment', ' Department'])
        st.dataframe(df)

    with tab2:
        with st.form(key='IPD_Dept'):
            department = st.text_input(label='Enter Department Name')
            submit_button = st.form_submit_button(label='Submit')
        result = view_all_data_department(department)
        df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Doctor_id', 'Room_no', 'Medication', 'Procedure_done', 'Date_of_admission', 'Date_of_discharge', 'Mode_of_payment', ' Department'])
        st.dataframe(df)
    
    with tab3:
        with st.form(key='IPD_DID'):
            doctor_id = st.text_input(label='Enter Doctor ID')
            submit_button = st.form_submit_button(label='Submit')
        result = view_all_data_doctor(doctor_id)
        df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Doctor_id', 'Room_no', 'Medication', 'Procedure_done', 'Date_of_admission', 'Date_of_discharge', 'Mode_of_payment', ' Department'])
        st.dataframe(df)


    st.subheader("Update Details")
    list_of_patients = [i[0] for i in view_only_patient_names()]
    selected_patient = st.selectbox("Patient Details to Edit", list_of_patients)
    result = get_details(selected_patient)
    st.text("Orginal Details of Patient: {}".format(selected_patient))
    df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Doctor_id', 'Room_no', 'Medication', 'Procedure_done', 'Date_of_admission', 'Date_of_discharge', 'Mode_of_payment', ' Department'])
    st.dataframe(df)

    if result:
        Department = result[0][9]
        new_Department = st.text_input("Department:", Department)

    if st.button("Update Patient Details"):
        edit_details_ipd(new_Department, selected_patient)
        st.success("Successfully updated: {}".format(selected_patient))
    

def view_all_data_patient(patient_id):
    c.execute('SELECT * FROM Inpatient_dept WHERE Patient_id="{}"'.format(patient_id))
    data = c.fetchall()
    return data

def view_all_data_doctor(doctor_id):
    c.execute('SELECT * FROM Inpatient_dept WHERE Doctor_id="{}"'.format(doctor_id))
    data = c.fetchall()
    return data

def view_all_data_department(department):
    c.execute('SELECT * FROM Inpatient_dept WHERE Department="{}"'.format(department))
    data = c.fetchall()
    return data

def edit_details_ipd(new_Department, selected_patient):
    query= "UPDATE Inpatient_dept SET Department=%s WHERE Patient_name=%s"
    c.execute(query,(new_Department,selected_patient))
    mydb.commit()
    data = c.fetchall()
    return data

def view_only_patient_names():
    c.execute('SELECT Patient_name FROM Inpatient_dept')
    data = c.fetchall()
    return data

def get_details(Patient_name):
     c.execute('SELECT * FROM Inpatient_dept WHERE Patient_name="{}"'.format(Patient_name))
     data = c.fetchall()
     return data


if __name__ == '__ipd__':
    ipd()


# def view_only_train_names():
#     c.execute('SELECT Name FROM Train')
#     data = c.fetchall()
#     return data


# def get_details(train_name):
#     c.execute('SELECT * FROM Train WHERE Name="{}"'.format(train_name))
#     data = c.fetchall()
#     return data


# def edit_details(new_train_no, new_train_name, new_train_type, new_source, new_dest, new_available, train_no, train_name, train_type, source, dest, available):
#     c.execute("UPDATE Train SET Train_No=%s, Name=%s, Train_Type=%s, Source=%s, Destination=%s, Availability=%s WHERE "
#               "Train_No=%s and Name=%s and Train_Type=%s and Source=%s and Destination=%s and Availability=%s", (new_train_no, new_train_name, new_train_type, new_source, new_dest, new_available, train_no, train_name, train_type, source, dest, available))
#     mydb.commit()
#     data = c.fetchall()
#     return data


# def delete_data(train_name):
#     c.execute('DELETE FROM Train WHERE Name="{}"'.format(train_name))
#     mydb.commit()