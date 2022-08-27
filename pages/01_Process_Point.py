import pandas as pd
import streamlit as st
import extra_streamlit_components as stx
import tempfile
import numpy as np
import netCDF4
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
     page_title="(1/3) Processing a single point",
     page_icon="✨",
     layout="wide",
     initial_sidebar_state="collapsed"
 )

"# **Data processing for turbulence analysis (1/3)**"

st.info(
"""
Each file gathered by the instrument consists of two
timeseries: 
- **Bottom distance** readings
- **Velocity** measurements

Both occur at different frequencies, for example, bottom distances 
are measured once every second whereas velocities can be read up to 
50 times per second. 
""")

st.info(
"""
🏜️ We will use the bottom distance timeseries to check that the bedforms did
not migrate substantially and will get the location at which
the corresponding velocities were taken.

⏱️ Then, we use the velocity readings to extract their mean over time and the
fluctuation timeseries.

☀️ Finally, a (mean velocity, depth) pair is obtained from each file. 
""")

st.info("Let's start exploring a file:")

with st.expander("Upload a netCDF4 file from the Vectrino Profiler 👇",
                 expanded=("upfile" not in st.session_state)):
    uploadedFile = st.file_uploader("","nc",False,key="upfile")

"****"

step_int = stx.stepper_bar(steps=["🏜️ Bottom Distance", "⏱️ Velocity Readings", "☀️ Summary"])

if uploadedFile:

    with tempfile.NamedTemporaryFile() as ncFile:
        
        # Read file and parse as pandas dataframe
        f = netCDF4.Dataset(ncFile,memory=uploadedFile.getvalue())
        data = f['Data']['Profiles']
        shapeTime = data['time'].shape
            
        vels = pd.DataFrame({k:np.array(data[k]) \
                            for k in list(data.variables.keys()) \
                            if data[k].shape == shapeTime})
    
        # Organize bottom check in a separate pandas dataframe
        data = f['Data']['BottomCheck']
        shapeTime = data['time'].shape
        bott = pd.DataFrame({k:np.array(data[k]) \
                            for k in list(data.variables.keys()) \
                            if data[k].shape == shapeTime})

        if step_int == 0:
        
            """
            ## 🏜️ Bottom distance over time
            """

            col1,col2 = st.columns([1,1.5],gap='medium')
            
            with col1:
                st.image("assets/ADV_Distances.png",
                    caption="Distances in the ADV setup")
                
            with col2:
                with st.expander("😵‍💫  The entire dataset from the ADV",expanded=True):
                    st.dataframe(bott.style.format(precision=4,subset=["time","BottomDistance"]),
                                height=300)

                    st.download_button("😵‍💫  Click here to download the entire dataset as CSV",
                        data = bott.to_csv().encode('utf-8'),
                        file_name = "Bottom.csv")
                
                """
                Notice that we only need two columns from this dataset: 
                - `time`
                - `BottomDistance`
                """
                
                filtered_bottom = bott[['time','BottomDistance']].copy()
                
                """
                `BottomDistance` measures the lenght between the instrument and the 
                channel bottom. However, we need the distance between the sample
                and the bottom (`SamplePositionZ` in the sketch below) to properly 
                locate the corresponding velocity readings.
                """


            "****"
            
            "#### Extract useful information:"
            col1,col2,col3 = st.columns([1,1.5,1.5],gap='medium')

            with col1:
                st.info("Adjust according to your lab setup", icon="🎚️")
                
                flumeDepth = st.number_input("Enter Flume depth [m]:",0.00,0.50,0.15,0.01,"%.2f")
                probeDist  = st.number_input("Enter SampleDistance [m]:",0.00,0.10,0.05,0.001,"%.3f")
                filtered_bottom['SamplePositionZ'] = filtered_bottom['BottomDistance'] - probeDist

            with col2:
                with st.expander("🍋 Our processed data",expanded=True):

                    st.dataframe(filtered_bottom.style.format(precision=4),height=150)
                    st.download_button("🍋 Click here to download this processed data as CSV",
                        data = filtered_bottom.to_csv().encode('utf-8'),
                        file_name = "Bottom_Processed.csv",
                        disabled=True)
                    
                    meanZ = filtered_bottom['SamplePositionZ'].mean()
                    stdZ  = filtered_bottom['SamplePositionZ'].std()

                    st.metric("Mean  ±  stdev. of SamplePositionZ: ",
                        f"{meanZ:.3f} ± {stdZ:.3f} m")

            
            with col3:

                fig = go.Figure()
                
                fig.update_layout(
                    autosize=False,
                    hovermode='closest',
                    height=400,
                    title={
                        'text': "📈 Sample position z over time",
                        'y': 0.9,
                        'x': 0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                    xaxis={
                        'title':"Time (s)",
                        'exponentformat' : "power",
                        'gridwidth':1,
                        'gridcolor':"CadetBlue"},
                    yaxis={
                        'title':"Bottom Distance (m)",
                        'exponentformat' : "power",
                        'gridwidth':0.2,
                        'range':[0,flumeDepth],
                        'gridcolor':"CadetBlue"},
                    legend={
                        'orientation':"h",
                        'yanchor':"top",
                        'y':-0.1,
                        'xanchor':"left",
                        'x':0.01,
                        'title':None,
                        'groupclick':"toggleitem"},
                    font={
                        'size': 14}
                    )

                fig.add_trace(
                            go.Scatter(
                                x = filtered_bottom['time'],
                                y = filtered_bottom['SamplePositionZ'],
                                name = "Readings",
                                mode = 'lines+markers',
                                legendgroup = "experiments",
                                legendgrouptitle_text = "Experimental data",
                                marker={'size' : 8,
                                        'symbol': "x" 
                                        }
                                ))
                
                st.plotly_chart(fig,use_container_width=True)


        elif step_int == 1:
            """
            ## ⏱️ Velocity Readings
            """

            col1,col2 = st.columns([1,2],gap='medium')
            
            with col1:
                r"""
                Notice that in this case we only need a few columns from the dataset: 
                - `time`
                - `VelocityX`
                - `VelocityY`
                - `VelocityZ1` or `VelocityZ2`
                
                **** 

                Each component of the velocity timeseries $\vec{u}(t)$ can be decomposed 
                into its mean $U$ and a fluctuation series $u'(t)$. For instance:

                | Component    | Decomposition      | 
                |--------------|--------------------|
                | `VelocityX`  | $u(t) = U + u'(t)$ |
                | `VelocityY`  | $v(t) = V + v'(t)$ |
                | `VelocityZ1` | $w(t) = W + w'(t)$ |

                """

            directions = ['VelocityX','VelocityY','VelocityZ1']
            filtered_vels = vels[['time'] + directions].copy()

            with col2:
                with st.expander("😵‍💫  The entire velocity readings from the ADV",expanded=True):
                    st.dataframe(vels.style.format(precision=4),
                                height=200)

                    st.download_button("😵‍💫  Click here to download the entire dataset as CSV",
                        data = vels.to_csv().encode('utf-8'),
                        file_name = "Velocity.csv")

            "****"

            fig = make_subplots(rows=1, cols=3,
                                shared_yaxes=True,
                                horizontal_spacing=0.02,
                                subplot_titles = [rf'<em>{i}(t)</em>' for i in ['u','v','w']],
                                x_title="Time (s)")
            
            for i,direction in enumerate(directions,start=1):
                fig.add_trace(
                    go.Scatter(
                        x = filtered_vels['time'],
                        y = filtered_vels[direction],
                    name = direction,
                    mode = 'lines'),
                row = 1, col = i)

            st.plotly_chart(fig,use_container_width=True,include_mathjax='cdn')

            # "*****"
            col1,col2 = st.columns([1,1],gap='medium')

            with col1:
                with st.expander("🍋 Our filtered data",expanded=True):
                    st.dataframe(filtered_vels.style.format(precision=4),height=150)
                    st.download_button("🍋 Click here to download this processed data as CSV",
                        data = filtered_vels.to_csv().encode('utf-8'),
                        file_name = "Bottom_Processed.csv",
                        disabled=True)
            
            with col2:
                for direction in directions:
                    mean = filtered_vels[direction].mean()
                    stdv = filtered_vels[direction].std()
                    st.metric(f"Mean  ±  stdev. of  {direction}",
                                f"{mean:.3f} ± {stdv:.3f} m/s")

        elif step_int == 2:
            """
            ## ☀️ Summary

            From this file, you have obtained a (Velocity - Elevation) pair to plot in your 
            velocity profile.
            """