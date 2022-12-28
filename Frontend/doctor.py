import mysql.connector
import streamlit as st
import pandas as pd

mydb = mysql.connector.connect(
host="localhost", user="root", password="vanshika")
c = mydb.cursor()
c.execute("USE HOSPITAL_MANAGEMENT_484")


def doctor():
    tab1, tab2, tab3, tab4 = st.tabs(["Create","Read","Update", "Delete"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            new_doctor_id = st.text_input("Doctor ID:")
            new_doctor_name = st.text_input("Doctor Name:")
            new_department = st.text_input("Department:")
        with col2:
            new_designation = st.text_input("Designation:")
            new_age = st.text_input("Age")
            new_gender = st.selectbox("Gender", ["Male", "Female"])

        col3, col4 = st.columns(2)
        with col3:
            new_house_address = st.text_input("House Address:")
            new_pincode = st.text_input("Pincode:")
            new_phone_no = st.text_input("Phone Number:")
        with col4:
            new_email = st.text_input("Email:")
            new_alternate_no = st.text_input("Alternate Phone Number:")
            new_bloodgroup = st.selectbox("Blood Group", ["A+", "B+", "O+", "AB+","A-", "B-", "O-", "AB-"])


        if st.button("Add Doctor Details"):
            add_details(new_doctor_id, new_doctor_name, new_department, new_designation, new_age, new_gender, new_house_address, new_pincode, new_phone_no, new_email, new_alternate_no, new_bloodgroup)
            st.success("Successfully added: {}".format(new_doctor_name))

    
    with tab2:
        with st.form(key='D_ID'):
            doctor_id = st.text_input(label='Enter Doctor ID')
            submit_button = st.form_submit_button(label='Submit')
        result = view_all_data_doctor(doctor_id)
        df = pd.DataFrame(result, columns=['Doctor_id', 'Doctor_name', 'Department', 'Designation', 'Age', 'Gender', 'House_address', 'Pincode', 'Phone_no', 'Email', 'Alternate_phone_number', 'Blood_group'])
        st.dataframe(df)


 
    with tab3:
        st.subheader("Update Details")
        list_of_patients = [i[0] for i in view_only_doctor_names()]
        selected_patient = st.selectbox("Patient Details to Edit", list_of_patients)
        result = get_details(selected_patient)
        st.text("Orginal Details of Patient: {}".format(selected_patient))
        df = pd.DataFrame(result, columns=['Doctor_id', 'Doctor_name', 'Department', 'Designation', 'Age', 'Gender', 'House_address', 'Pincode', 'Phone_no', 'Email', 'Alternate_phone_number', 'Blood_group'])
        st.dataframe(df)

        if result:
            Designation = result[0][3]
            new_Designation = st.text_input("Designation:", Designation)

        if st.button("Update Doctor Details"):
            edit_details_doctor(new_Designation, selected_patient)
            st.success("Successfully updated: {}".format(selected_patient))

    with tab4:
        with st.form(key='ID'):
            doctor_id = st.text_input(label='Enter Doctor ID')
            submit_button = st.form_submit_button(label='Submit')
        result = view_all_data_doctor(doctor_id)
        df = pd.DataFrame(result, columns=['Doctor_id', 'Doctor_name', 'Department', 'Designation', 'Age', 'Gender', 'House_address', 'Pincode', 'Phone_no', 'Email', 'Alternate_phone_number', 'Blood_group'])
        st.dataframe(df)

        list_of_doctors = [i[0] for i in view_only_doctor_names()]
        selected_doctor = st.selectbox("Doctor Details to Delete", list_of_doctors)
        st.warning("Do you want to delete {} ?".format(selected_doctor))
        if st.button("Delete Doctor Details"):
            delete_data(selected_doctor)
            st.success("Doctor details have been deleted successfully.")



def view_all_data_doctor(doctor_id):
    c.execute('SELECT * FROM Doctor WHERE Doctor_id="{}"'.format(doctor_id))
    data = c.fetchall()
    return data

def view_all_data(doctor_id):
    c.execute('SELECT * FROM Doctor;')
    data = c.fetchall()
    return data


def get_details(selected_doctor):
     c.execute('SELECT * FROM Doctor WHERE Doctor_name="{}"'.format(selected_doctor))
     data = c.fetchall()
     return data

def get_details_id(selected_doctor):
     c.execute('SELECT Doctor_id FROM Doctor WHERE Doctor_name="{}"'.format(selected_doctor))
     data = c.fetchall()
     return data

def view_only_doctor_names():
    c.execute('SELECT Doctor_name FROM Doctor')
    data = c.fetchall()
    return data

def delete_data(selected_doctor):
     c.execute('DELETE FROM Doctor WHERE Doctor_name="{}"'.format(selected_doctor))
     mydb.commit()
    
def edit_details_doctor(new_Designation, selected_doctor):
    query= "UPDATE Doctor SET Designation=%s WHERE Doctor_name=%s"
    c.execute(query,(new_Designation,selected_doctor))
    mydb.commit()
    data = c.fetchall()
    return data

def add_details(new_doctor_id, new_doctor_name, new_department, new_designation, new_age, new_gender, new_house_address, new_pincode, new_phone_no, new_email, new_alternate_no, new_bloodgroup):
    c.execute("INSERT INTO Doctor(Doctor_id,Doctor_name,Department,Designation,Age,Gender,House_address,Pincode,Phone_no,Email,Alternate_phone_number,Blood_group) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(new_doctor_id, new_doctor_name, new_department, new_designation, new_age, new_gender, new_house_address, new_pincode, new_phone_no, new_email, new_alternate_no, new_bloodgroup))
    mydb.commit()
    data = c.fetchall()
    return data

if __name__ == '__doctor__':
    doctor()