import pandas as pd
import streamlit as st
import extra_streamlit_components as stx
import tempfile
import numpy as np
import netCDF4
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="[NU CEE440] Lab 1 - Processing a single file",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="auto"
)

def restart():
    if "upfile" in st.session_state.keys():
        del st.session_state.upfile

if "_gist" not in st.session_state.keys():
    st.session_state["_gist"] = [0,0,0,0]

if "_flumeDepth" not in st.session_state.keys():
    st.session_state["_flumeDepth"] = 0.15

"# **Data processing for turbulence analysis**"

r"""
Each file gathered by the instrument consists of two
time series: 
- **Bottom distance** readings
- **Velocity** measurements

Bottom distances are measured once every second whereas 
velocities can be read up to 50 times per second. 
"""

st.info(
"""
🏜️ We will use the bottom distance timeseries to check that the bedforms did
not migrate substantially and will get the location at which
the corresponding velocities were taken.

⏱️ Then, we use the velocity readings to extract their mean over time and the
velocity fluctuation time series.

""")

r"""
****
## Let's start exploring a file:
"""

col1, col2 = st.columns([4,1])

with col1:
    with st.expander("Upload a netCDF4 file from the Vectrino Profiler 👇", expanded=("upfile" not in st.session_state)):
        uploadedFile = st.file_uploader("","nc",False,key="upfile")

with col2:
    if st.button("I don't have a file"):
            with open("./assets/dummyADV.nc","rb") as f:
                st.download_button("Click here to download a dummy file",f.read(),"dummyADV.nc")

"****"

if uploadedFile and ("upfile" in st.session_state.keys()):

    step_int = stx.stepper_bar(steps=["🏜️ Bottom Distance", "⏱️ Velocity Readings", "☀️ Summary"])

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

        #####################################
        # Step 1 - Bottom distance
        #####################################
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
            col1,col2 = st.columns([1,1.5],gap='medium')

            with col1:
                st.info("Adjust according to your lab setup", icon="🎚️")
                
                flumeDepth = st.number_input("Enter Flume depth [m]:",0.00,0.50,0.15,0.01,"%.2f")
                probeDist  = st.number_input("Enter SampleDistance [m]:",0.00,0.10,0.05,0.001,"%.3f")
                filtered_bottom['SamplePositionZ'] = filtered_bottom['BottomDistance'] - probeDist

                st.session_state["_flumeDepth"] = flumeDepth

                "****"

                with st.expander("🍋 Our processed data",expanded=False):

                    st.dataframe(filtered_bottom.style.format(precision=4),height=150)
                    st.download_button("🍋 Click here to download this processed data as CSV",
                        data = filtered_bottom.to_csv().encode('utf-8'),
                        file_name = "Bottom_Processed.csv",
                        disabled=True)
                    
                    meanZ = filtered_bottom['SamplePositionZ'].mean()
                    stdZ  = filtered_bottom['SamplePositionZ'].std()

                    st.metric("Mean  ±  stdev. of SamplePositionZ: ",
                        f"{meanZ:.3f} ± {stdZ:.3f} m")
                    
                    ## Save in session state
                    st.session_state["_gist"][0] = meanZ
            
            with col2:

                fig = go.Figure()
                
                fig.update_layout(
                    showlegend=False,
                    autosize=True,
                    hovermode='closest',
                    height=400,
                    title={
                        'text': "📈 Sample position over time",
                        'y': 0.9,
                        'x': 0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                    xaxis={
                        'title':"Time (s)",
                        'exponentformat' : "power"},
                    yaxis={
                        'title':"Bottom Distance (m)",
                        'exponentformat' : "power",
                        'range':[0,1.1*flumeDepth]},
                    font={
                        'size': 14}
                    )

                fig.add_trace(
                            go.Scatter(
                                x = filtered_bottom['time'],
                                y = filtered_bottom['SamplePositionZ'],
                                name = "Sampling position",
                                mode = 'lines+markers',
                                marker={'size' : 8,
                                        'symbol': "x" }
                                ))

                fig.add_hline(y=flumeDepth,
                                annotation={
                                    'text':"Water surface",
                                    'font_size':12,
                                    'font_color': "#1E90FF"     
                                },
                                annotation_position="top left",
                                line = {
                                    'width':2,
                                    'color':"#1E90FF",
                                    'dash':'dash'
                                }
                            )
                
                st.plotly_chart(fig,use_container_width=True)

        #####################################
        # Step 2 - Velocity Readings
        #####################################
        elif step_int == 1:
            """
            ## ⏱️ Velocity Readings
            """
            col1,col2 = st.columns(2)
            
            with col1:
                r"""
                Each component of the velocity timeseries $u_i(x,t)$ can be decomposed 
                into its mean $\overline{u_i}$ and a series of fluctuations $u'(x,t)$. 
                
                $$
                u_i(x,t) = \overline{u_i}(x) + u'_i(x,t)
                $$
                """
            
            with col2:
                """
                For our ADV data:

                | Component    | Decomposition      | 
                |--------------|--------------------|
                | `VelocityX`  | $u(t) = \overline{u} + u'(t)$ |
                | `VelocityY`  | $v(t) = \overline{v} + v'(t)$ |
                | `VelocityZ1` | $w(t) = \overline{w} + w'(t)$ |
                """

            """
            ****
            Notice that from our dataset we only need a few columns: 
            - `time`
            - `VelocityX`
            - `VelocityY`
            - `VelocityZ1` or `VelocityZ2`
            """

            directions = ['VelocityX','VelocityY','VelocityZ1']
            filtered_vels = vels[['time'] + directions].copy()

            with st.expander("😵‍💫  The entire velocity readings from the ADV",expanded=True):
                st.dataframe(vels.style.format(precision=4),
                            height=200)

                st.download_button("😵‍💫  Click here to download the entire dataset as CSV",
                    data = vels.to_csv().encode('utf-8'),
                    file_name = "Velocity.csv")


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
                    mode = 'lines',
                    line = {
                        "width":0.5}
                    ),
                row = 1, col = i)

                meanVel = filtered_vels[direction].mean()
                
                fig.add_hline(y = meanVel,
                    annotation={
                        'text':"Mean",
                        'font_size':12,
                        'bgcolor':"rgba(0,0,0,0.2)"
                        },
                    annotation_position="top left",
                    line = {
                        'width':2,
                        'dash':'dash'
                        },
                    row = 1, col = i)
                
                ## Save in session state
                st.session_state["_gist"][i] = meanVel

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
        
        #####################################
        # Step 3 - Summary
        #####################################
        elif step_int == 2:
            """
            ## ☀️ Summary

            From this file, you have obtained a the velocities measured at
            a **single position** $x$.
            """

            cols = st.columns(4)

            z,u,v,w = st.session_state['_gist']
            d = st.session_state["_flumeDepth"]

            with cols[0]: 
                    st.metric("Elevation:",f"{z:.3f} m")

            for i,(col,direction) in enumerate(zip(cols[1:],["X","Y","Z"])):
                with col: 
                    st.metric(
                        f"Velocity {direction}:",
                        f"{st.session_state['_gist'][i+1]:.3f} ᵐ/ₛ")

            col1, col2 = st.columns(2)
            
            with col1:
                r"""
                ****
                
                After doing this analysis for all the measured elevations (i.e., all
                the ADV files), you will have the information to start buildind the 
                velocity profile! 

                Check the next page about the other information that can be extracted
                from the velocity measurements at a single point.
                """

            with col2:
                fig = go.Figure()
                    
                fig.update_layout(
                    showlegend=False,
                    autosize=True,
                    hovermode='closest',
                    height=400,
                    title={
                        'text': "📈 My file in the velocity profile",
                            'y': 0.9,
                            'x': 0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'},
                        xaxis={
                            'title':"Velocity (m/s)",
                            'exponentformat' : "power"},
                        yaxis={
                            'title':"Elevation (m)",
                            'exponentformat' : "power",
                            'range':[0,1.1*d]},
                        font={
                            'size': 14}
                )

                fig.add_trace(
                    go.Scatter(
                        x = [u],
                        y = [z],
                        name = "Sampling position",
                        mode = 'markers',
                        marker={'size' : 10,
                                'symbol': "circle-dot" }
                        )
                    )

                fig.add_hline(
                    y=d,
                    annotation={
                        'text':"Water surface",
                        'font_size':12,
                        'font_color': "#1E90FF"     
                    },
                    annotation_position="top left",
                    line = {
                        'width':2,
                        'color':"#1E90FF",
                        'dash':'dash'
                        }
                    )

                st.plotly_chart(fig,use_container_width=True)

            st.button("↻ I have another file",key="restart_btn",help="Click here to restart.",on_click=restart)