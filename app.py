
# app.py
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Influencer ROI Predictor", page_icon="📊", layout="wide")

st.markdown("""
<style>
.block-container{padding-top:2rem;padding-bottom:2rem;}
.stButton>button{width:100%;height:50px;border-radius:10px;background:#1f77b4;color:white;font-weight:bold;}
div[data-testid="stMetric"]{background:#eef5ff;padding:15px;border-radius:10px;}
</style>
""", unsafe_allow_html=True)

model = joblib.load("roi_prediction_model.pkl")
platform_encoder = joblib.load("platform_encoder.pkl")
category_encoder = joblib.load("category_encoder.pkl")
campaign_encoder = joblib.load("campaign_encoder.pkl")

st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Navigation",
    [
        "🤖 ROI Prediction",
        "📊 Dashboard",
        "ℹ️ About"
    ]
)
if page == "📊 Dashboard":

    st.title("📊 Business Analytics Dashboard")

    st.markdown("""
    This dashboard was developed in **Power BI** to analyze influencer marketing campaign performance.
    """)

    # Create tabs FIRST
    tab1, tab2, tab3 = st.tabs([
        "📈 Dashboard 1",
        "📊 Dashboard 2",
        "📉 Dashboard 3"
    ])

    # Dashboard 1
    with tab1:
        st.image("dashboard1.png", use_container_width=True)

    # Dashboard 2
    with tab2:
        st.image("dashboard2.png", use_container_width=True)

    # Dashboard 3
    with tab3:
        st.image("dashboard3.png", use_container_width=True)

    st.stop()

if page == "ℹ️ About":

    st.title("ℹ️ About This Project")

    st.markdown("""
## AI-Powered Influencer Marketing ROI Prediction System

### Objective

Predict the Return on Investment (ROI) of influencer marketing campaigns using Machine Learning.

### Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Power BI

### Machine Learning Model

Random Forest Regressor

### Features

- ROI Prediction
- Interactive Dashboard
- Business Recommendation
- Campaign Summary
- Power BI Analytics Dashboard

""")

    st.stop()

st.title("🤖 AI-Powered Influencer Marketing ROI Prediction System")
st.write("Predict campaign ROI using Machine Learning.")
st.divider()

c1,c2,c3=st.columns(3)
c1.metric("Model","Random Forest")
c2.metric("Algorithm","Regression")
c3.metric("Target","ROI")

left,right=st.columns([2,1])

with left:
    st.subheader("📋 Campaign Details")
    platform=st.selectbox("Platform",["Instagram","TikTok","YouTube","Twitter"])
    category=st.selectbox("Influencer Category",["Fashion","Food","Fitness","Gaming","Travel","Beauty","Tech"])
    campaign=st.selectbox("Campaign Type",["Brand Awareness","Giveaway","Product Launch"])
    engagements=st.number_input("Engagements",0,1000000,50000)
    reach=st.number_input("Estimated Reach",0,5000000,200000)
    duration=st.number_input("Campaign Duration (Days)",1,365,15)
    spend=st.number_input("Spend (₹)",0,10000000,30000)

    summary=pd.DataFrame({
        "Feature":["Platform","Category","Campaign","Engagements","Reach","Duration","Spend"],
        "Value":[platform,category,campaign,engagements,reach,duration,spend]
    })
    st.subheader("Campaign Summary")
    st.dataframe(summary,use_container_width=True)

    predict=st.button("🔮 Predict ROI")

with right:
    st.subheader("📊 Prediction Result")
    if predict:
        p=platform_encoder.transform([platform])[0]
        cat=category_encoder.transform([category])[0]
        camp=campaign_encoder.transform([campaign])[0]
        sample=pd.DataFrame({
            "platform":[p],
            "influencer_category":[cat],
            "campaign_type":[camp],
            "engagements":[engagements],
            "estimated_reach":[reach],
            "campaign_duration_days":[duration],
            "Spend":[spend]
        })
        prediction=model.predict(sample)[0]
        st.metric("Predicted ROI",f"{prediction:.2f}%")
        if prediction>=2000:
            st.success("🟢 Excellent ROI")
            st.info("Recommendation: Campaign is expected to perform very well.")
        elif prediction>=1000:
            st.warning("🟡 Good ROI")
            st.info("Recommendation: Optimize campaign for even better results.")
        else:
            st.error("🔴 Low ROI")
            st.info("Recommendation: Review campaign strategy.")
    else:
        st.info("Enter campaign details and click Predict ROI.")

with st.expander("How does this work?"):
    st.write("""
1. User enters campaign details.
2. Categories are label encoded.
3. Random Forest predicts ROI.
4. Result and recommendation are displayed.
""")

st.divider()
st.caption("Machine Learning Model: Random Forest Regressor | Streamlit + Scikit-learn")
