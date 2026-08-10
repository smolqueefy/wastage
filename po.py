import streamlit as st
import pandas as pd
from datetime import date

st.title("Daily Wastage Calculator")

outlet = st.text_input("Outlet", "PDH")
report_date = st.date_input("Date", date.today())

items = [
"BUN",
"PUFF & CROISSANT & DANISH",
"DONUT",
"BAGEL",
"SOFT COOKIES",
 "MUFFIN",   
"GERMAN PRETZEL",
"BAGUETTE & SAVOURY BUN",
"BAGUETTE & SOURDOUGH",
"SANDWICH",
"CROISSANT BISCUIT",
"PACKAGING BUN",
"COOKIES",
"PASTRY",
"JAM",
"WHOLE CAKE",
"SLICE CAKE",
"TART",
"DESSERT",
"STRAWBERRY SERIES",
"FESTIVE"
]

data = []

st.subheader("Enter Data")

for item in items:

    col1,col2,col3 = st.columns(3)

    do = col1.number_input(f"{item} D.O",min_value=0,key=item+"do")
    prod = col2.number_input(f"{item} Production Waste",min_value=0,key=item+"prod")
    sale = col3.number_input(f"{item} Sales Waste",min_value=0,key=item+"sale")

    prod_pct = (prod/do*100) if do>0 else 0
    sale_pct = (sale/do*100) if do>0 else 0

    data.append({
        "item":item,
        "do":do,
        "prod":prod,
        "sale":sale,
        "prod_pct":prod_pct,
        "sale_pct":sale_pct
    })

df = pd.DataFrame(data)

total_do = df["do"].sum()
total_prod = df["prod"].sum()
total_sale = df["sale"].sum()

total_prod_pct = (total_prod/total_do*100) if total_do>0 else 0
total_sale_pct = (total_sale/total_do*100) if total_do>0 else 0

st.subheader("Totals")

st.write("D.O:",total_do)
st.write("Production Waste:",total_prod,f"({total_prod_pct:.2f}%)")
st.write("Sales Waste:",total_sale,f"({total_sale_pct:.2f}%)")

if st.button("Generate Report"):

    report = f"""Daily Wastage Report

OUTLET: {outlet}
DATE: {report_date}

*TOTAL*
D.O : {total_do}
Production Wastage : {total_prod} ({total_prod_pct:.2f}%)
Sales Wastage : {total_sale} ({total_sale_pct:.2f}%)

"""

    for row in data:

        report += f"""*{row['item']}*
D.O : {row['do'] if row['do'] else ""}
Production Wastage : {row['prod']} ({row['prod_pct']:.2f}%)
Sales Wastage : {row['sale']} ({row['sale_pct']:.2f}%)

"""

    st.subheader("Report Output")
    st.text_area("Copy Report",report,height=400)
    
