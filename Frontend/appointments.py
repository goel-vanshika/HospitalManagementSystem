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

def appointments():
    tab1, tab2= st.tabs(["Patient ID", "Department"])

    with tab1:
        with st.form(key='A_ID'):
            patient_id = st.text_input(label='Enter Patient ID')
            submit_button = st.form_submit_button(label='Submit')
        result = view_all_data_patient(patient_id)
        df = pd.DataFrame(result, columns=['Appointment_date', 'Patient_name', 'Next_appt_date', 'Department', 'Patient_id'])
        st.dataframe(df)

    with tab2:
        with st.form(key='A_Dept'):
            department = st.text_input(label='Enter Department Name')
            submit_button = st.form_submit_button(label='Submit')
        result = view_all_data_department(department)
        df = pd.DataFrame(result, columns=['Appointment_date', 'Patient_name', 'Next_appt_date', 'Department', 'Patient_id'])
        st.dataframe(df)


    st.subheader("Delete Appointments")
    result = get_details()
    st.text("Appointment Details of all Patients")
    df = pd.DataFrame(result, columns=['Appointment_date', 'Patient_name', 'Next_appt_date', 'Department', 'Patient_id'])
    st.dataframe(df)
    list_of_patients = [i[0] for i in view_only_patient_names()]
    selected_patient = st.selectbox("Appointment to Delete", list_of_patients)

    if st.button("Delete Appointment"):
        st.warning("Do you want to delete :{}".format(selected_patient))
        delete_data(selected_patient)
        st.success("Appointment has been deleted.")
    

def view_all_data_patient(patient_id):
    c.execute('SELECT * FROM Appointments WHERE Patient_id="{}"'.format(patient_id))
    data = c.fetchall()
    return data

def view_all_data_department(department):
    c.execute('SELECT * FROM Appointments WHERE Department="{}"'.format(department))
    data = c.fetchall()
    return data

def delete_data(selected_patient):
     c.execute('DELETE FROM Appointments WHERE Patient_id="{}"'.format(selected_patient))
     mydb.commit()

def view_only_patient_names():
    c.execute('SELECT Patient_id, Appointment_date FROM Appointments')
    data = c.fetchall()
    return data

def get_details():
     c.execute('SELECT * FROM Appointments')
     data = c.fetchall()
     return data


if __name__ == '__appointments__':
    appointments()


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