import streamlit as st

st.set_page_config(
    page_title="CE440 Laboratory #1",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

r"""
# CE440 Laboratory #1 - Turbulence and Open-Channel Flow
"""

st.image("./assets/complete_setup.jpg",use_column_width=True)

"""
## Objectives 

> The primary objective of this lab is for you to increase your 
> understanding of the hydrodynamic processes we have been studying 
> in class by directly observing them. You will measure the detailed 
> flow structure in an open channel flow and compare the observations 
> against theory presented in class for both turbulent velocity 
> profiles and overall flow resistance in uniform flow. 
"""

r"""
## Instruments

> You will use an Acoustic Doppler Velocimeter (ADV) to measure the 
> velocity distribution over the depth of the open channel flow with 
> a sediment bed, and collect additional observations of discharge, 
> depth, slope and roughness so that you can compare local velocity 
> profiles with predictions based on uniform flow assumptions. 

> The ADV is a research-grade instrument that is commonly used to study 
> turbulence in laboratory systems. It can sample velocity in 3D at a 
> high frequency (~30 Hz) in a cube of roughly 1 cm3. Essentially this 
> means that the ADV measures the instantaneous velocity within a sampling 
> volume of 1 cm3. Measurement of a large number of data points will allow 
> you to perform a temporal average of the instantaneous data in order 
> to analyze the turbulent flow behavior.  The ADV is automated and writes 
> the data directly to a computer, generating large files with all three 
> velocity components as a high-frequency time series, u(t), v(t), w(t). 
> Typically, each time series contains several thousand individual 
> measurements of the instantaneous velocity in order to yield good estimates 
> of the time-averaged velocity in the turbulent flow field.
"""

r"""
## Data to be acquired

> You will obtain data to build velocity profiles at both the trough and 
> crest of a dune. At each location, velocity data will be collected at 
> several elevations spanning the depth of the flow, yielding vertical 
> profiles of all three velocity components, u(x,t), v(x,t), w(x,t). 
> As the bedforms are moving, these measurements must be made in a timely 
> manner before the trough or crest moves from beneath the ADV. You will be 
> given electronic copies of all velocity data. In addition, the stream 
> hydraulic conditions (flow rate, depth, slope, etc.) will be obtained 
> as well. The flow rate is reported by an in-line flow meter.  Depth is 
> measured directly through the side walls of the flume, measuring at 
> several locations in order to obtain an average. To calculate the slope, 
> the system is set up in uniform flow (no changes in depth along the length 
> of the channel), and then the water surface elevation is measured at many
> locations along the length of the flume via a probe attached to an LDVT,
> which is mounted on a plexiglass board that rest on rails parallel to 
> the flume. You can estimate the elevation profile and hydraulic gradient 
> (slope) from these measurements. Finally, the boundary roughness height 
> is obtained by measuring and averaging the heights of many dunes. 
"""


