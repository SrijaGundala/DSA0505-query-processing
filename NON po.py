import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import base64
import os
import matplotlib.pyplot as plt

# Define allowed file extensions
ALLOWED_EXTENSIONS = {'xlsx'}
st.set_page_config(layout="wide")

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Function to perform analysis on Excel file
def analyze_excel(file):
    df = pd.read_excel(file)
    df1 = pd.read_excel(r"C:\Users\srija\OneDrive\Desktop\nonPO\costctr.xlsx", header=1)
    df2 = pd.read_excel(r"C:\Users\srija\OneDrive\Desktop\nonPO\GLNAME.xlsx", header=1)
    df1.rename(columns={'Costct': 'Costctr'}, inplace=True)
    df2.rename(columns={'Glaccount': 'GLs'}, inplace=True)
    df_gl = df2[['GLs', 'Gname']]
    df_ctr = df1[['Costctr', 'Cname']]
    costctr_to_cname = dict(zip(df_ctr['Costctr'], df_ctr['Cname']))
    df['Cname'] = df['Costctr'].map(costctr_to_cname)
    costctr_to_cname = dict(zip(df_gl['GLs'], df_gl['Gname']))
    df['Gname'] = df['GLs'].map(costctr_to_cname)
    df['On'] = pd.to_datetime(df['On'])
    df['year'] = df['On'].dt.year
    df['On'] = df['On'].dt.date
    df['Cummulative_transactions'] = len(df)
    df['Cummulative_transactions/category'] = df.groupby('category')['category'].transform('count')
    df['overall_transactions/year'] = df.groupby('year')['year'].transform('count')
    df['overall_transactions/category/year'] = df.groupby(['category', 'year'])['category'].transform('count')
    df['cumulative_Alloted_Amount'] = df['Amount'].sum()
    df['cumulative_Alloted_Amount/Category'] = df.groupby('category')['Amount'].transform('sum')
    df['Yearly_Alloted_Amount/Category'] = df.groupby(['category', 'year'])['Amount'].transform('sum')
    yearly_total = df.groupby('year')['Amount'].sum().reset_index()
    yearly_total.rename(columns={'Amount': 'Total_Alloted_Amount/year'}, inplace=True)
    df = pd.merge(df, yearly_total, on='year', how='left')
    df['cumulative_Transations/Vendor'] = df.groupby('Vendor')['Vendor'].transform('count')
    df['Transations/year/Vendor'] = df.groupby(['year', 'Vendor'])['Vendor'].transform('count')
    df['Cumulative_Amount_used'] = df.groupby(['Vendor', 'category'])['Amount'].transform('sum')
    df['Amount_used/Year'] = df.groupby(['Vendor', 'year', 'category'])['Amount'].transform('sum')
    df['Cumulative_percentageamount_used'] = (df['Cumulative_Amount_used'] / df['cumulative_Alloted_Amount']) * 100
    df['percentage_amount_used_per_year'] = (df['Amount_used/Year'] / df['Total_Alloted_Amount/year']) * 100
    df['total_percentage_of_amount/category_used'] = (df['Cumulative_Amount_used'] / df[
        'cumulative_Alloted_Amount/Category']) * 100
    df['percentage_of_amount/category_used/year'] = (df['Amount_used/Year'] / df[
        'Yearly_Alloted_Amount/Category']) * 100
    df['Cumulative_percentransations_made'] = (df['cumulative_Transations/Vendor'] / df[
        'Cummulative_transactions']) * 100
    df['Cumulative_percentransations_made/category'] = (df['cumulative_Transations/Vendor'] / df[
        'Cummulative_transactions/category']) * 100
    df['percentransations_made/category/year'] = (df['Transations/year/Vendor'] / df[
        'overall_transactions/category/year']) * 100
    df['percentransations_made/year'] = (df['Transations/year/Vendor'] / df['overall_transactions/year']) * 100
    df = df.drop_duplicates(subset=['Vendor', 'year'])
    df.reset_index(drop=True, inplace=True)
    df['Vendor'] = df['Vendor'].astype(str)
    df_sorted = df.sort_values(by='Vendor', ascending=False)  # Showing only the first 25 rows
    df_sorted.reset_index(drop=True, inplace=True)

    # Storing the resultant DataFrame to an Excel file
    df_sorted.to_excel("analysis_result.xlsx", index=False)

    return df_sorted

def main():
# Main Streamlit app
    # Divide the page into 6 columns for dropdowns
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    # Placeholder for file uploader
    with col1:
        upload_placeholder = st.empty()

    # Placeholder for analyze button
    with col2:
        analyze_placeholder = st.empty()

    # File uploader
    uploaded_file = upload_placeholder.file_uploader("Upload Excel file", type=["xlsx"])

    if uploaded_file is not None:
        if allowed_file(uploaded_file.name):
            df = analyze_excel(uploaded_file)
            analyze_placeholder.empty()  # Hide analyze button

            # Dropdown for selecting year
            with col1:
                selected_year = st.selectbox("Select Year", ['All'] + list(df['year'].unique()))

            # Dropdown for selecting category
            with col2:
                selected_category = st.selectbox("Select Category", ['All'] + list(df['category'].unique()))

            # Dropdown for selecting graph type
            with col3:
                selected_graph = st.selectbox("Select Graph Type", ['Payment Trend', 'Transaction Trend'])

            # Filtering the DataFrame based on selected options
            filtered_df = df.copy()
            if selected_year != 'All':
                filtered_df = filtered_df[filtered_df['year'] == selected_year]
            if selected_category != 'All':
                filtered_df = filtered_df[filtered_df['category'] == selected_category]

            # Divide the page into 2 columns for DataFrame and graph
            col_df, col_graph = st.columns([3, 2])

            # Display DataFrame
            with col_df:
                st.write("### Filtered DataFrame")
                st.write(filtered_df)

            # Plotting

            with col_graph:
                if selected_graph == 'Payment Trend':
                    st.write("### Payment Trend")
                    vendor_options = ['All'] + list(filtered_df['Vendor'].unique())

                    # Divide the graph section into 3 columns for dropdowns
                    col_vendor, col_x_axis, col_y_axis = st.columns(3)

                    # Dropdown for selecting vendor
                    with col_vendor:
                        selected_vendor = st.selectbox("Select Vendor", vendor_options)

                    if selected_vendor != 'All':
                        filtered_df = filtered_df[filtered_df['Vendor'] == selected_vendor]

                    # Dropdown for selecting X-axis
                    with col_x_axis:
                        x_axis = st.selectbox("Select X-Axis", ['Vendor'])

                    # Dropdown for selecting Y-axis
                    with col_y_axis:
                        y_axis = st.selectbox("Select Y-Axis", ['percentage_amount_used_per_year'])

                    if x_axis == 'Vendor':
                        fig, ax = plt.subplots(figsize=(10, 6))
                        years = filtered_df['year'].unique()  # Unique years in the data
                        colors = plt.cm.viridis(np.linspace(0, 1, len(years)))  # Generate colors for each year

                        for year, color in zip(years, colors):
                            year_data = filtered_df[filtered_df['year'] == year]
                            ax.plot(year_data[x_axis], year_data[y_axis], marker='o', label=year, color=color)

                        ax.set_xlabel(x_axis)
                        ax.set_ylabel(y_axis)
                        ax.set_title(f"{y_axis} vs {x_axis}")
                        ax.legend()  # Show legend with year labels
                        st.pyplot(fig)

                elif selected_graph == 'Transaction Trend':
                    st.write("### Transaction Trend")
                    vendor_options = ['All'] + list(filtered_df['Vendor'].unique())
                    selected_vendor = st.selectbox("Select Vendor", vendor_options)

                    if selected_vendor != 'All':
                        filtered_df = filtered_df[filtered_df['Vendor'] == selected_vendor]

                    x_axis = st.selectbox("Select X-Axis", ['Vendor'])
                    y_axis = st.selectbox("Select Y-Axis", ['Cummulative_transactions'])

                    if x_axis == 'Vendor':
                        fig, ax = plt.subplots(figsize=(10, 6))
                        years = filtered_df['year'].unique()  # Unique years in the data
                        colors = plt.cm.viridis(np.linspace(0, 1, len(years)))  # Generate colors for each year

                        for year, color in zip(years, colors):
                            year_data = filtered_df[filtered_df['year'] == year]
                            ax.plot(year_data[x_axis], year_data[y_axis], marker='o', label=year, color=color)

                        ax.set_xlabel(x_axis)
                        ax.set_ylabel(y_axis)
                        ax.set_title(f"{y_axis} vs {x_axis}")
                        ax.legend()  # Show legend with year labels
                        st.pyplot(fig)

            upload_placeholder.empty()  # Hide file uploader
        else:
            st.write("Invalid file type. Please upload a .xlsx file.")

if __name__ == "__main__":
    main()