# -*- coding: utf-8 -*-
"""assignment5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17sxDnSdsqs6bd9KcnoPnsekwTIv8wGIY
"""

import streamlit as st
import pandas as pd

st.title('Daily Rainfall')
data = {
    'Days' : [1, 2, 3, 4, 5, 6, 7],
    'Rainfall(mm)' : [20, 10, 0, 100, 50, 0, 30]
}
df = pd.DataFrame(data)

# Display the dataset
st.write("Rainfall Data:")
st.write(df)

x_axis = 'Days'
y_axis = 'Rainfall(mm)'

# Choose chart type: Bar Chart or Line Chart
chart_type = st.selectbox('Select chart type', ['Bar Chart', 'Line Chart'])

# Display chart based on user selections
if chart_type == 'Bar Chart':
    st.bar_chart(df[[x_axis, y_axis]].set_index(x_axis))
elif chart_type == 'Line Chart':
    st.line_chart(df[[x_axis, y_axis]].set_index(x_axis))