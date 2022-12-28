import mysql.connector
import streamlit as st
import pandas as pd

mydb = mysql.connector.connect(
host="localhost", user="root", password="vanshika")
c = mydb.cursor()
c.execute("USE HOSPITAL_MANAGEMENT_484")


def patient():
    tab1, tab2, tab3, tab4 = st.tabs(["Create","Read","Update", "Delete"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            new_patient_id = st.text_input("Patient ID:")
            new_patient_name = st.text_input("Patient Name:")
            new_guardian = st.text_input("Guardian Name:")
        with col2:
            new_age = st.text_input("Age:")
            new_gender = st.selectbox("Gender", ["Male", "Female"])
            new_phone_no = st.text_input("Phone Number:")

        col3, col4 = st.columns(2)
        with col3:
            new_house_address = st.text_input("House Address:")
            new_pincode = st.text_input("Pincode:")
            new_bloodgroup = st.selectbox("Blood Group", ["A+", "B+", "O+", "AB+","A-", "B-", "O-", "AB-"])
        with col4:
            new_emergency = st.text_input("Emergency Phone Number:")
            new_aadhar = st.text_input("Aadhar Card Number:")
            new_email = st.text_input("Email:")


        if st.button("Add Patient Details"):
            add_details(new_patient_id, new_patient_name, new_guardian, new_age, new_gender, new_phone_no, new_house_address, new_pincode, new_bloodgroup, new_emergency, new_aadhar, new_email)
            st.success("Successfully added: {}".format(new_patient_name))

    
    with tab2:
        with st.form(key='P_ID'):
            patient_id = st.text_input(label='Enter Patient ID')
            submit_button = st.form_submit_button(label='Submit')
        result = view_all_data_patient(patient_id)
        df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Guardian_name', 'Age', 'Gender', 'Phone_no', 'House_address', 'Pincode', 'Blood_group', 'Emergency_contact', 'Aadhar_card_no', 'Email'])
        st.dataframe(df)


 
    with tab3:
        with st.form(key='Patient_ID'):
            patient_id = st.text_input(label='Enter Patient ID')
            submit_button = st.form_submit_button(label='Submit')
        result = view_all_data_patient(patient_id)
        df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Guardian_name', 'Age', 'Gender', 'Phone_no', 'House_address', 'Pincode', 'Blood_group', 'Emergency_contact', 'Aadhar_card_no', 'Email'])
        st.dataframe(df)

        list = [i[0] for i in view_only_patient_names()]
        selected = st.selectbox("Patient Details to Update", list)
        change = get_details(selected)
        st.text("Details of Patient")
        df2 = pd.DataFrame(change, columns=['Patient_id', 'Patient_name', 'Guardian_name', 'Age', 'Gender', 'Phone_no', 'House_address', 'Pincode', 'Blood_group', 'Emergency_contact', 'Aadhar_card_no', 'Email'])
        st.dataframe(df2)

        if result:
            House_address = result[0][6]
            new_House_address = st.text_input("House Address:", House_address)

        if st.button("Update Patient"):
            edit_details_patient(new_House_address, selected)
            st.success("Successfully updated: {}".format(selected))

    with tab4:
        with st.form(key='ID'):
            patient_id = st.text_input(label='Enter Patient ID')
            submit_button = st.form_submit_button(label='Submit')
        result = view_all_data_patient(patient_id)
        df = pd.DataFrame(result, columns=['Patient_id', 'Patient_name', 'Guardian_name', 'Age', 'Gender', 'Phone_no', 'House_address', 'Pincode', 'Blood_group', 'Emergency_contact', 'Aadhar_card_no', 'Email'])
        st.dataframe(df)

        list_of_patients = [i[0] for i in view_only_patient_names()]
        selected_patient = st.selectbox("Patient Details to Delete", list_of_patients)
        st.warning("Do you want to delete :{}".format(selected_patient))
        if st.button("Delete Patient Details"):
            delete_data(selected_patient)
            st.success("Patient details have been deleted successfully")



def view_all_data_patient(patient_id):
    c.execute('SELECT * FROM Patient WHERE Patient_id="{}"'.format(patient_id))
    data = c.fetchall()
    return data

def view_all_data(patient_id):
    c.execute('SELECT * FROM Patient;')
    data = c.fetchall()
    return data


def get_details(selected_patient):
     c.execute('SELECT * FROM Patient WHERE Patient_name="{}"'.format(selected_patient))
     data = c.fetchall()
     return data

def get_details_id(selected_patient):
     c.execute('SELECT Patient_id FROM Patient WHERE Patient_name="{}"'.format(selected_patient))
     data = c.fetchall()
     return data

def view_only_patient_names():
    c.execute('SELECT Patient_name FROM Patient')
    data = c.fetchall()
    return data

def delete_data(selected_patient):
     c.execute('DELETE FROM Patient WHERE Patient_name="{}"'.format(selected_patient))
     mydb.commit()
    
def edit_details_patient(new_House_address, selected_patient):
    query= "UPDATE Patient SET House_address=%s WHERE Patient_name=%s"
    c.execute(query,(new_House_address,selected_patient))
    mydb.commit()
    data = c.fetchall()
    return data

def add_details(new_patient_id, new_patient_name, new_guardian, new_age, new_gender, new_phone_no, new_house_address, new_pincode, new_bloodgroup, new_emergency, new_aadhar, new_email):
    c.execute("INSERT INTO Patient(Patient_id,Patient_name,Guardian_name,Age,Gender,Phone_no,House_address,Pincode,Blood_group,Emergency_contact,Aadhar_card_no,Email) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(new_patient_id, new_patient_name, new_guardian, new_age, new_gender, new_phone_no, new_house_address, new_pincode, new_bloodgroup, new_emergency, new_aadhar, new_email))
    mydb.commit()
    data = c.fetchall()
    return data

if __name__ == '__patient__':
    patient()