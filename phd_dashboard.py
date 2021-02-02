import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

st.sidebar.title('Kiomed Sales Analysis')
select_data = ["Positive Sales Data", "Negative Sales Data"]
type_of_data = st.sidebar.selectbox("Select the type of data to load", select_data)

city_dict = {4: 'Mumbai', 5: 'Delhi', 7: 'Bangalore', 1: 'Kolkata', 6: 'Chennai', 8: 'Hyderabad', 9: 'Ahmedabad', 3: 'Jaipur', 10: 'Lucknow', 2: 'Other'}

@st.cache
def load_positive_data():
    data = pd.read_csv("train_data.csv")
    data["city"]=data["city"].map(city_dict)
    data.drop(data[data["sales"]<0].index,axis=0,inplace=True)
    return data

@st.cache
def load_negative_data():
    data = pd.read_csv("train_data.csv")
    data = data[data["sales"]<0]
    data["city"]=data["city"].map(city_dict)
    return data

@st.cache
def get_data():
    if type_of_data == 'Positive Sales Data':
        data = load_positive_data()
    if type_of_data == 'Negative Sales Data':
        data = load_negative_data()
    return data

city_list = ['Mumbai','Delhi', 'Bangalore', 'Kolkata', 'Chennai', 'Hyderabad', 'Ahmedabad', 'Jaipur', 'Lucknow', 'Other']
city_selected = st.sidebar.selectbox("Select the City", city_list)

observation_dict = {
    "Positive Sales Data": {
        "Kolkata": {
        "yearly" : "2017 shows highest sales for kolkata and 2015 shows lowest sales for kolkata",
        "monthly": "For kolkata March has the highest sales followed by january and july and august has the lowest sales",
        "daily" : "In Kolkata third day of the month has the most sales followed by second and the fifth day. 31st day has the lowest sales"
     },
    "Jaipur": {
        "yearly" : "For Jaipur 2017 has the highest sales followed by 2016 and 2015 has the lowest sales",
        "monthly": "For Jaipur march has most sales followed by january and June. August has the least sales",
        "daily" : "For Jaipur Day 3 has the highest sales followed by day 20 and 5. Day 31 has the least sales"  
    },
    "Mumbai":{
        "yearly": "For Mumbai 2017 has most sales followed by 2016 and 2018 has the least sales",
        "monthly": "For Mumbai March has most sales followed by january, June and December. August has the least sales",
        "daily" : "For Mumbai day 3 has the highest sales followed by day 2 and 1. Day 31 has the least sales"
    },
    "Delhi":{
        "yearly": "For Delhi 2017 has most sales followed by 2016 and 2015 has the least sales",
        "monthly": "March has the most sales followed by jan, june and Dec. Aug has the least sales",
        "daily": "For Delhi Day 2 has the most no of sales followed by day 3 and 1. Day 31 has the least sales"
    },
    "Chennai": {
        "yearly": "For Chennai 2017 has most sale followed by 2016 and 2018 has least no of sales",
        "monthly": "For Chennai March has the most no of sales followed by dec, jan and may. Aug has the least sales",
        "daily": "for Chennai day 2 has most of the sales followed by day 3, 1 and 5"
    },
    "Bangalore": {
        "yearly": "For Bangalore 2017 has most sale followed by 2016 and 2018 has least sales",
        "monthly": "For Bangalore March had most no of sales followed by jan, Dec and June. Aug has least no of sales",
        "daily": "For Bangalore Day 3 has most no of sale followed by day 2, 1 and 5. This implies most sales happen during the first week of the month"
    },
    "Hyderabad": {
        "yearly": "For Hyderabad 2017 show most sales followed by 2016 and 2018 has least sales",
        "monthly": "For Hyderbad Dec has most no of sales followed by march, jan and May. Aug has least sales",
        "daily": "For Hyderabad Day 1 has the most sale followed by day 3 and 2 and day 31 has the least sales"
    },
    "Ahmedabad": {
        "yearly": "For Ahemdabad 2017 had most sales followed by 2016 and 2015 had least sales",
        "monthly": "For Ahemdabad December has most sales followed by March, June and Jan. Aug has the least sale",
        "daily": "For Ahemdabad day 3 had most sales followed by day 2, 1 and 6 and day 31 has least sales"
    },
    "Lucknow": {
        "yearly": "For lucknow 2017 had most sales followed by 2016 and 2018 had least sale",
        "monthly": "For Lucknow December has the most negative sales and July had the least negative sale",
        "daily": "For Lucknow day 2 has most sales followed by day 3, 5, 1 and Day 31 has the least sales"
    },
    "Other":{
        "yearly": "For other cities 2017 has most sales followed by 2016 and 2018 has the least sales",
        "monthly": "For Other cities March had the most sale followed by Jan , june and May. Aug had the least sales",
        "daily": "For Other cities day 3 has most number of sales followed by day 2, 6 and 1. Day 31 has least number of sale"
    }
    },
    "Negative Sales Data": {
        "Kolkata": {
        "yearly" : "2015 shows least negative sales for kolkata and 2018 shows most negative sales for kolkata",
        "monthly": "For kolkata May has the least negative sales and February has the lowest sales",
        "daily" : "In Kolkata seventh day has the least negative sales and 2nd day has the most negative sales"
     },
    "Jaipur": {
        "yearly" : "For Jaipur 2018 has the highest negative sales and 2015 has the lowest negative sales",
        "monthly": "For Jaipur April has most negative sales and October has the least negative sales",
        "daily" : "For Jaipur Day 30 has the highest negative sales and Day 26 has the least sales"  
    },
    "Mumbai":{
        "yearly": "For Mumbai 2017 has most negative sales and 2016 has the least sales",
        "monthly": "For Mumbai December has most negative sales followed by january, June and December. August has the least negative sales",
        "daily" : "For Mumbai day 15 has the highest negative sales and Day 27 has the least negative sales"
    },
    "Delhi":{
        "yearly": "For Delhi 2016 has most negative sales and 2018 has the least negative sales",
        "monthly": "July has the most negative sales followed by jan, june and Dec. November has the least negative sales",
        "daily": "For Delhi Day 7 has the most negative sales and Day 10 has the least sales"
    },
    "Chennai": {
        "yearly": "For Chennai 2018 has most negative sale and 2015 has least no of sales",
        "monthly": "For Chennai April has the most negative sales and Aug has the least negative sales",
        "daily": "For Chennai day 24 has most negative sales and day 28 has the least Negative sales"
    },
    "Bangalore": {
        "yearly": "For Bangalore 2017 has most negative sales and 2015 has least negative sales",
        "monthly": "For Bengaluru August has most negative sales and October has least no of sales",
        "daily": "For Bengaluru Day 7 has most negative sales and day 23 has the least sales"
    },
    "Hyderabad": {
        "yearly": "For Hyderabad 2017 show most negative sales and 2015 has least sales",
        "monthly": "For Hyderabad May has most negative sales July has least negative sales",
        "daily": "For Hyderabad Day 30 has the most negative sale and day 17, 23, 9 has the least sales"
    },
    "Ahmedabad": {
        "yearly": "for Ahemdabad 2017 had most negative sales and 2016 had least negative sales",
        "monthly": "For Ahemdabad July has most negative sales followed by March, June and Jan. sept has the least negative sales",
        "daily": "For Ahemdabad day 20 had most negative sales and day 20 has least sales"
    },
    "Lucknow": {
        "yearly": "For lucknow 2016 had most negative sales and 2018 had least negative sales",
        "monthly": "For Lucknow December has the most negative sales and July had the least negative sale",
        "daily": "For Lucknow day 18 has most negative sales and Day 3 has the least negaive sales"
    },
    "Other":{
        "yearly": "For other cities 2018 has most negative sales and 2015 has the least sales",
        "monthly": "For Other cities April had the most negative. Aug had the least negative sales",
        "daily": "For Other cities day 23 has most number of negative sales Day 3 has least negative sale"
    }

    }
}

@st.cache
def get_city_data():
    data = get_data()
    city_data = data[data["city"] == city_selected]
    return city_data

@st.cache
def get_analysis_type_data(data, set_analysis_type):
    analysis_type_data = data.groupby([set_analysis_type]).agg({"sales":sum})
    analysis_type_data = analysis_type_data.sort_values(by="sales", ascending=False)
    return analysis_type_data

@st.cache
def get_city_medicine_data(select_medicine):
    city_medicine_data = get_city_data()
    city_medicine_data = city_medicine_data[city_medicine_data["medicine"] == select_medicine]
    return city_medicine_data

def show_observation(data,city,analysis):
    st.header("Observation")
    observation = observation_dict[type_of_data][city_selected][analysis_type_selected]
    st.subheader(observation)

def show_analysis_type_viz():
    city_data = get_city_data()
    if analysis_type_selected == "yearly":
        yearly_data = get_analysis_type_data(data= city_data, set_analysis_type="year")
        st.bar_chart(yearly_data[['sales']])
        show_observation(data=select_data, city=city_selected, analysis=analysis_type_selected)

    if analysis_type_selected == "monthly":
        monthly_data = get_analysis_type_data(data= city_data, set_analysis_type="month")
        st.bar_chart(monthly_data[['sales']])
        show_observation(data=select_data, city=city_selected, analysis=analysis_type_selected)

    if analysis_type_selected == "daily":
        daily_data = get_analysis_type_data(data= city_data, set_analysis_type= "day")
        st.bar_chart(daily_data[['sales']])
        show_observation(data=select_data, city=city_selected, analysis=analysis_type_selected)


def show_med_analysis():
    med_data = get_city_medicine_data(select_medicine)
    if len(med_data) == 0:
        st.markdown("Sorry No Records Available")
    if analysis_type_selected == "yearly":
        medicine_data_yearly = med_data.groupby(["year"]).agg({"sales":sum})
        medicine_data_yearly = medicine_data_yearly.sort_values(by="sales", ascending=False)
        st.bar_chart(medicine_data_yearly[["sales"]])

    if analysis_type_selected == "monthly":
        medicine_data_monthly = med_data.groupby(["month"]).agg({"sales":sum})
        medicine_data_monthly = medicine_data_monthly.sort_values(by="sales", ascending=False)
        st.bar_chart(medicine_data_monthly[["sales"]])

    if analysis_type_selected == "daily":
        medicine_data_daily = med_data.groupby(["day"]).agg({"sales":sum})
        medicine_data_daily = medicine_data_daily.sort_values(by="sales", ascending=False)
        st.bar_chart(medicine_data_daily[["sales"]])
    
def get_category_order_sales_for(df, col, ascending=True):
    temp=df.groupby([col])["sales"].sum().sort_values().reset_index()
    temp["sales"]=np.round(temp["sales"])
    category_orders = list(temp[col])
    return category_orders

def plot_agg_sales(df, aggby, x, color):
    temp=df.groupby(aggby)["sales"].sum().reset_index()
    temp["sales"]=np.round(temp["sales"])
    # title = f"aggregated sales for {x}"
    cat_orders = get_category_order_sales_for(df, x)
    fig5 = px.bar(temp, x=x, y="sales", barmode='group',color = color, category_orders={x:cat_orders})
    st.plotly_chart(fig5)

def show_agg_viz(data):
    if analysis_type_selected == "yearly":
        st.header("Per City Yearly Aggeregated Sales Analysis")
        plot_agg_sales(df=data, aggby=["year", "city"], x="city", color="year")
    if analysis_type_selected == "monthly":
        st.header("Per City Monthly Aggeregated Sales Analysis")
        plot_agg_sales(df=data, aggby=["month", "city"], x="city", color="month")
    if analysis_type_selected == "daily":
        st.header("Per City Daily Aggeregated Sales Analysis")
        plot_agg_sales(df=data, aggby=["day", "city"], x="city", color="day")


analysis_type = ["yearly", "monthly", "daily"]
analysis_type_selected = st.sidebar.radio("Type of Analysis you're looking for",analysis_type)
viz_checkbox = st.sidebar.checkbox("Show Overall Sales Analysis")
agg_city_sales_checkbox = st.sidebar.checkbox("Show Aggregated Sales")
st.sidebar.subheader("Medicine Analysis")
select_medicine = st.sidebar.text_input("Select Medicine type")
medicine_viz_checkbox = st.sidebar.checkbox("Show Medicine Analysis")

if analysis_type_selected and viz_checkbox:
    st.title("Overall "+ analysis_type_selected + " Sales Analysis in "+ city_selected)
    show_analysis_type_viz()
if select_medicine and medicine_viz_checkbox:
    select_medicine = int(select_medicine)
    st.title("Overall "+ analysis_type_selected + " Sales Analysis In "+ city_selected + " For Medicine "+str(select_medicine))
    show_med_analysis()
if agg_city_sales_checkbox:
    complete_data = get_data()
    show_agg_viz(data=complete_data)




    







