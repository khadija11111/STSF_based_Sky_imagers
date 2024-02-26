#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:55:43 2024

@author: Barhm001
"""

# import streamlit as st
# import subprocess
# import os

# # Function to run a Python script and return its output
# def run_script(script_path):
#     result = subprocess.run(['python', script_path], capture_output=True, text=True)
#     return result.stdout

# # Set up the Streamlit page
# st.title('Short-term solar forecasting based All sky imagers for congestion management in Business parks')

# # Display Sun Mask
# st.header('Sun Mask Results')
# sun_mask_script = '/path/to/ApplySunMask.py'  # Update this path
# run_script(sun_mask_script)
# st.image('path/to/sun_mask_result.png')  # Update this path

# # Display Cloud Motion
# st.header('Cloud Motion Results')
# cloud_motion_script = '/path/to/CloudMotion.py'  # Update this path
# run_script(cloud_motion_script)
# st.image('path/to/cloud_motion_result.png')  # Update this path

# # Display GHI Forecasting
# st.header('GHI Forecasting Results')
# ghi_forecasting_script = '/path/to/IrradianceMap.py'  # Update this path
# run_script(ghi_forecasting_script)
# st.image('path/to/ghi_forecasting_result.png')  # Update this path

#%% this is only for GHi
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from datetime import datetime
# import os


# # Function to convert 'TIME' to seconds since midnight
# def time_to_seconds(t):
#     return (t.hour * 3600) + (t.minute * 60) + t.second

# # Function to load and process data
# def load_and_process_data(file_path):
#     data = pd.read_excel(file_path)

#     # Convert 'TIME' to datetime.time and then to seconds since midnight
#     data['TIME'] = pd.to_datetime(data['TIME'], format='%H:%M:%S').dt.time
#     data['TimeInSeconds'] = data['TIME'].apply(time_to_seconds)

#     # Sort the data by 'TimeInSeconds'
#     return data.sort_values(by='TimeInSeconds').reset_index(drop=True)

# # Streamlit application starts here
# st.title('Short-term solar forecasting based All sky imagers for congestion management in Business parks')

# # Assuming you have only one cleaned file or you're interested in the last modified one
# output_dir = '/Users/Barhm001/Desktop/CNN/Cleaned_final'  # Adjust this path to your output folder
# excel_files = [file for file in os.listdir(output_dir) if file.endswith('.xlsx')]

# if excel_files:
#     # Load and process data from the last modified Excel file
#     latest_file = max(excel_files, key=lambda x: os.path.getmtime(os.path.join(output_dir, x)))
#     data_sorted = load_and_process_data(os.path.join(output_dir, latest_file))

#     # Plotting
#     fig, ax = plt.subplots()
#     ax.plot(data_sorted['TimeInSeconds'], data_sorted['PIRA'], label='GHI (w/m^2)', color='green')
#     ax.set_title('GHI (w/m^2)')
#     ax.set_xlabel('Time (Seconds from Midnight)')
#     ax.set_ylabel('GHI (w/m^2)')

#     # Display the plot in Streamlit
#     st.pyplot(fig)

# else:
#     st.write("No Excel files found in the output directory for plotting.")

#%% This presnets text and shows plot:
    
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, time
import os

# Function to convert 'TIME' to seconds since midnight
def time_to_seconds(t):
    return (t.hour * 3600) + (t.minute * 60) + t.second

# Function to load and process data
def load_and_process_data(file_path):
    data = pd.read_excel(file_path)

    # Convert 'TIME' to datetime.time and then to seconds since midnight
    data['TIME'] = pd.to_datetime(data['TIME'], format='%H:%M:%S').dt.time
    data['TimeInSeconds'] = data['TIME'].apply(time_to_seconds)

    # Sort the data by 'TimeInSeconds'
    return data.sort_values(by='TimeInSeconds').reset_index(drop=True)

# Streamlit application starts here
st.title('Short-term solar forecasting based on All Sky Imagers for congestion management in Business Parks')

# Introduction text
intro_text = """
Sky imagers are sophisticated devices equipped with cameras and sensors designed to capture high-resolution images of the sky and analyze cloud movements and formations. In the context of solar forecasting for congestion management in business parks, these imagers play a crucial role in predicting solar irradiance, which is the power per unit area received from the sun in the form of electromagnetic radiation.

The use of sky imagers allows for more accurate and localized solar energy forecasts. By analyzing the patterns and speed of cloud cover, these devices can predict fluctuations in solar power generation. This is particularly important for business parks that rely on solar panels for their energy needs, as it enables them to anticipate periods of low solar generation and manage their energy consumption and storage strategies accordingly.

In terms of congestion management, accurate solar forecasts help in optimizing the operation of microgrids within business parks. They assist in balancing supply and demand, reducing the risk of overloads or energy shortages. This ensures a stable and efficient energy supply, minimizing the need for drawing power from the main grid, which can be both costly and less environmentally friendly.

Furthermore, in business parks where electricity consumption is higher also electric vehicle (EV) charging stations are powered by solar energy, sky imagers can aid in managing these charging loads. By forecasting solar energy availability, operators can schedule EV charging during times of high solar generation, thus avoiding congestion and maximizing the use of renewable energy.

In summary, sky imagers enhance the reliability and efficiency of solar energy systems in business parks, leading to improved energy management, reduced operational costs, and a lower carbon footprint.
"""

st.markdown(intro_text)

# Displaying sky images after the text
images_dir = '/Users/Barhm001/Desktop/DT/images'  # Update this path to your images directory
image_files = [os.path.join(images_dir, file) for file in sorted(os.listdir(images_dir)) if file.endswith('.jpg') or file.endswith('.png')][:8]

if image_files:
    st.write("Sky Images Sequence:")
    # Extracting datetime part from filenames for captions
    captions = [os.path.splitext(os.path.basename(file))[0].split('_')[0] for file in image_files]
    # Display all images on the same line with appropriate sizing
    st.image(image_files, caption=captions, width=150, use_column_width=False, clamp=True)
else:
    st.write("No sky images found.")

# Create a time slider for selecting the time range
time_range = st.slider(
    "Select a time range",
    value=(time(0, 0, 0), time(23, 59, 59)),  # Default time range for the whole day
    format="HH:mm:ss"
)

# Assuming you have only one cleaned file or you're interested in the last modified one
output_dir = '/Users/Barhm001/Desktop/CNN/Cleaned_final'  # Adjust this path to your output folder
excel_files = [file for file in os.listdir(output_dir) if file.endswith('.xlsx')]

if excel_files:
    # Load and process data from the last modified Excel file
    latest_file = max(excel_files, key=lambda x: os.path.getmtime(os.path.join(output_dir, x)))
    data_sorted = load_and_process_data(os.path.join(output_dir, latest_file))

    # Convert the selected time range to seconds
    start_time_seconds = time_to_seconds(time_range[0])
    end_time_seconds = time_to_seconds(time_range[1])

    # Filter the DataFrame based on the selected time range
    filtered_data = data_sorted[(data_sorted['TimeInSeconds'] >= start_time_seconds) & (data_sorted['TimeInSeconds'] <= end_time_seconds)]

    # Plotting
    fig, ax = plt.subplots()
    ax.plot(filtered_data['TimeInSeconds'], filtered_data['PIRA'], label='GHI (w/m^2)', color='green')
    ax.set_title('GHI (w/m^2) within Selected Time Range')
    ax.set_xlabel('Time (Seconds from Midnight)')
    ax.set_ylabel('GHI (w/m^2)')

    # Display the plot in Streamlit
    st.pyplot(fig)

else:
    st.write("No Excel files found in the output directory for plotting.")


# AI in Solar Prediction Text
ai_solar_prediction_text = """
The advent of AI in solar irradiance prediction, particularly through sky imagers, has significantly advanced the accuracy and reliability of photovoltaic power forecasts. A pivotal tool in this domain is the Support Vector Machine (SVM), a powerful machine learning algorithm known for its efficacy in regression and classification tasks. In the context of GHI prediction, SVM models the relationship between atmospheric conditions, captured by sky imagers, and solar power output, through a process known as regression analysis.

By analyzing patterns in cloud cover and atmospheric dynamics, SVM can predict fluctuations in GHI with remarkable precision. This mathematical modeling considers various factors, including the angle of the sun, cloud opacity, and movement, translating complex atmospheric data into accurate power generation forecasts. The ability to predict solar power generation enhances the management of energy loads within business parks, facilitating the efficient use of solar energy and mitigating congestion in microgrids.

Accurate solar predictions allow for proactive energy management, ensuring that the supply from photovoltaic systems aligns with demand patterns. This not only optimizes the use of renewable resources but also alleviates the strain on the grid, addressing the critical issue of congestion management. Thus, AI and machine learning, through techniques like SVM, play a crucial role in enhancing the sustainability and efficiency of solar energy systems in business parks.
"""

st.markdown(ai_solar_prediction_text)


# After displaying the GHI plot or wherever you see fit in your Streamlit application

# Optimization Problem
st.markdown("### SVR Optimization Problem")
st.latex(r'''
\min_{w, b, \xi, \xi^*} \frac{1}{2} ||w||^2 + C \sum_{i=1}^{n} (\xi_i + \xi_i^*)
''')
st.markdown('''
subject to
''')
st.latex(r'''
\begin{align*}
y_i - \langle w, x_i \rangle - b &\leq \epsilon + \xi_i, \\
\langle w, x_i \rangle + b - y_i &\leq \epsilon + \xi_i^*, \\
\xi_i, \xi_i^* &\geq 0, \text{ for all } i = 1, ..., n.
\end{align*}
''')

# Epsilon-Insensitive Loss Function
st.markdown("### \( \epsilon \)-Insensitive Loss Function")
st.latex(r'''
L_\epsilon (y, f(x)) = 
\begin{cases} 
0 & \text{if } |y - f(x)| \leq \epsilon \\
|y - f(x)| - \epsilon & \text{otherwise}
\end{cases}
''')

# Kernel Trick
st.markdown("### Kernel Trick")
st.latex(r'''
f(x) = \sum_{i=1}^{n} (\alpha_i - \alpha_i^*) K(x_i, x) + b
''')
st.markdown('''
Where \( K(x_i, x) \) is the kernel function that maps input features into a higher-dimensional space.
''')

# Continue with the rest of the ov production
