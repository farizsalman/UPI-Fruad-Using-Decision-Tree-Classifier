import joblib
import streamlit as st


device_oe=joblib.load("device_oe.joblib")
m_category=joblib.load("m_category.joblib")
network_oe=joblib.load("network_oe.joblib")
oe_day=joblib.load("oe_day.joblib")
oe_state=joblib.load("oe_state.joblib")
receive_age=joblib.load("receive_age.joblib")
send_age=joblib.load("send_age.joblib")
receive_bank=joblib.load("receive_bank.joblib")
send_bank=joblib.load("send_bank.joblib")
t_status=joblib.load("t_status.joblib")
t_type=joblib.load("t_type.joblib")

model=joblib.load("Decision_Tree_Classifier.pk1")

st.title('UPI FRAUD DETECTION')
st.image("intro pic.png")

st.text("Unified Payments Interface(UPI) has revolutionised digital transactions in India, enabling fast and seamless money transfers" \
" between bank accounts. However, the rapid growth pf UPI has also led to a rise in fraudulant activities," \
" posing a significant risks to users and financial institutions. Detecting fraudulant transactions in real time is crucial in ensuring " \
"the security and trustworthiness of digital payment systems"
        )



st.header('Detect Fraud in your transaction  :')


transaction_type = st.selectbox("Payment Type: ",
                     ['P2M','P2P','Recharge','Bill Payment'])


Month=st.number_input('Transaction month')
Year=st.number_input('Transaction Year')
Date=st.number_input('Transaction Date')
day_of_week = st.selectbox("Day Of The Week: ",
                     ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])


Amount=st.number_input('Transaction Amount (INR)')


transaction_status = st.selectbox("Payment Status: ",
                     ['SUCCESS','FAILED'])



merchant_category = st.selectbox("Merchant Category: ",
                     ['Grocery','Food','Shopping','Fuel','Other','Utilities','Transport','Entertainment','Healthcare','Education'])



sender_state = st.selectbox("State : ",
                     ['Maharashtra','Uttar Pradesh','Karnataka','Tamil Nadu','Delhi','Telangana','Gujarat','Andhra Pradesh','Rajasthan','West Bengal'])





sender_age_group = st.selectbox("Sender Age Group: ",
                     ['18-25','26-35','36-45','46-55','56+'])



receiver_age_group = st.selectbox("Receiver Age Group: ",
                     ['18-25','26-35','36-45','46-55','56+'])



sender_bank = st.selectbox("Sender Bank: ",
                     ['SBI','HDFC','ICICI','IndusInd','Axis','PNB','Yes Bank','Kotak'])



receiver_bank = st.selectbox("Receiver Bank: ",
                     ['SBI','HDFC','ICICI','IndusInd','Axis','PNB','Yes Bank','Kotak'])


network_type = st.selectbox("Network Type: ",
                     ['3G','4G','5G','WiFi'])



device_type = st.selectbox("Device Type: ",
                     ['Android','iOS','Web'])




if st.button ("Detect Fraud"):
    transaction_type_enc=t_type.transform([[transaction_type]])[0][0]
    transaction_status_enc=t_status.transform([transaction_status])[0]
    merchant_category_enc=m_category.transform([[merchant_category]])[0][0]
    sender_state_enc=oe_state.transform([[sender_state]])[0][0]
    day_of_week_enc=oe_day.transform([[day_of_week]])[0][0]
    sender_age_group_enc=send_age.transform([[sender_age_group]])[0][0]
    receiver_age_group_enc=receive_age.transform([[receiver_age_group]])[0][0]
    sender_bank_enc=send_bank.transform([[sender_bank]])[0][0]
    receiver_bank_enc=receive_bank.transform([[receiver_bank]])[0][0]
    network_type_enc=network_oe.transform([[network_type]])[0][0]
    device_type_enc=device_oe.transform([[device_type]])[0][0]

    detection=model.predict([[transaction_type_enc,Amount,Month,Year,Date,transaction_status_enc,merchant_category_enc,
                              sender_state_enc,day_of_week_enc,sender_age_group_enc,receiver_age_group_enc,
                              sender_bank_enc,receiver_bank_enc,network_type_enc,device_type_enc]])
    
    if detection==1:
        st.error('Fraud activity detected')
        st.image("fraud transaction pic.png")
    else:
        st.success('Genuine Transaction')
        st.image("genuine transaction pic.png")
