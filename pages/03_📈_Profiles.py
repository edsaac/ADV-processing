import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="[NU CEE440] - Profiles and fitting",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed")

###########################################3
# Plots 
###########################################3

def shearStressPlot():
    x = np.geomspace(1.0E-20,1.0,127)
    tau = 1.0 - x
    tauViscosity = 1.0 - np.power(x,0.1)
    tauReynolds = tau - tauViscosity

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x = x,
            y = tau,
            mode = 'lines',
            name = 'Total shear stress',
            line = {
                'width' : 5
                }
        )
    )

    fig.add_trace(
        go.Scatter(
            x = x,
            y = tauViscosity,
            mode = 'lines',
            name = 'Viscous shear stress',
            line = {
                'width' : 5
                }
        )
    )

    fig.add_trace(
        go.Scatter(
            x = x,
            y = tauReynolds,
            mode = 'lines',
            name = 'Reynolds shear stress',
            line = {
                'width' : 5
                }
        )
    )

    fig.update_layout(
        showlegend=True,
        autosize=True,
        hovermode='closest',
        height=500,
        title={
            'text': "Shear stress components",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        xaxis={
            'title':r"Normalized shear stress  <i>τ(y)</i>",
            'exponentformat' : "power",
            'range':[-0.01,1.05]},
        yaxis={
            'title':r"Distance to bottom   <i>y/d</i>",
            'exponentformat' : "power",
            'range':[-0.01,1.05]},
        font={
            'size': 14}
        )
    return fig

def velocityProfilePlot(controlContainer):
    y = np.linspace(1.0E-10,0.11,11)
    u = np.array([0,0.04,0.06,0.09,0.10,0.11,0.105,0.11,0.11])
    
    yfit = np.linspace(1.0E-10,0.15,111)
    
    with controlContainer:
        st.markdown("<br>"*3,unsafe_allow_html=True)
        with st.expander("Fitting parameters:",expanded=True):
            a = st.slider("A",0.0,0.15,0.10,0.001)
            b = st.slider("B",0.0,0.10,0.03,0.001)
        
    ufit = a + b*(1 + np.log(yfit/0.15))

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x = u,
            y = y,
            mode = 'markers+lines',
            name = 'Velocity profile',
            line = {
                'width' : 0.4
                },
            marker = {
                'size' : 10,
                'symbol' : 'star',
                'color' : "#00008B"
            }
        )
    )

    fig.add_trace(
        go.Scatter(
            x = ufit,
            y = yfit,
            mode = 'lines',
            name = 'Fitted curve',
            line = {
                'width' : 1
                }
        )
    )

    fig.add_vline(
        x=0.09,
        annotation={
            'text':"Bulk velocity  U",
            'font_size':12,
            'font_color': "#00008B"     
            },
            annotation_position="top left",
            line = {
                'width':2,
                'color':"#00008B",
                'dash':'dot'
            }
        )

    fig.add_hline(
        y=0.15,
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

    fig.update_layout(
        showlegend=False,
        autosize=True,
        hovermode='closest',
        height=500,
        title={
            'text': "Velocity profile",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        xaxis={
            'title':r'Time-averaged velocity  <i><span style="text-decoration:overline">u</span>(y)<i>',
            'exponentformat' : "power",
            'range':[-0.01,0.16]},
        yaxis={
            'title':r"Distance to bottom   <i>y</i>",
            'exponentformat' : "power",
            'range':[-0.01,0.18]},
        font={
            'size': 14}
        )
    return fig

"# 📈 **Profiles and fitting data**"


###########################################3
# Section 1: Data 
###########################################3

r"""

## From data

### Velocity profiles

Having processed all the ADV files, you must have obtained a series of 
(temporal) mean velocities over depth $\overline{u}(y)$. 
This profile should look  something like the sketched plot below.

Try to fit a curve to your profile data. The curve should be of the form 

$$
    u_{\textsf{fit}}(y) = A + B \left( 1 + \ln{\left(\dfrac{y}{d}\right)} \right)
$$

Where $A$ and $B$ are fitting parameters and $d$ is the flume depth.

"""

col1,col2 = st.columns([1,2.5])

with col2:
    st.plotly_chart(velocityProfilePlot(col1),use_container_width=True)

r"""
An important feature of the velocity profile $\overline{u}(t)$ is its **derivative 
with respect of** $y$. From the fitted function, you could find that:

$$
    \dfrac{d u_{\textsf{fit}}(y)}{d y} = \dfrac{B}{y} 
$$

""" 

st.error(
    r"""
    But $B/y$ is undefined at $y=0$
    What other way could you estimate this derivative?
    """,icon="♾️")

r"""
### Reynolds stress profiles
Similarly, you must have obtained the six components that make 
up the Reynolds stress tensor, each as a function of depth $\tau'_{ij}(y)$

"""

###########################################3
# Section 2: Theory
###########################################3


r"""
****

## From theory

### Dimensionless depth

The **viscous lenghtscale** $\delta_v$ is defined as,

$$
    \delta_v = \dfrac{\nu}{u^*}
$$

This lenghtscale is used tto obtain a **dimensionless depth** $y^+$

$$
    y^+ = \dfrac{y}{\delta_v} = \dfrac{u^* y}{\nu}
$$
"""

st.warning(
    """
    Notice that $y^+$ does not depend on the depth of the flow! 

    However, velocity profiles can be plotted with the normalized 
    depth $y/d$. Make sure to not mix them up.

    """, icon="⚠️")

r"""
### Shear stress over depth

The total shear stress $\tau(y)$ is the sum of the Reynolds and the 
viscous stress

$$
    \tau(y) = \underbrace{\rho\nu \dfrac{d\overline{u}}{dy}}_{\textsf{Viscous stress}} 
        - \underbrace{\rho\overline{u'v'}}_{\textsf{Reynolds stress}}
$$

The viscous stress is the derivative over depth of the mean velocity, which corresponds
to the velocity profile! 

"""

r"""
The maximum shear stress $\tau_0$ is located at the bottom $y=0$. At this point, the 
**no-slip** condition of the flow ensure us that the velocity $u = 0$, thus, the Reynolds
stress is also zero. Therefore,

$$
    \begin{array}{rl}

    \tau_0 =& \tau(y=0) \\
        \\
        =& \rho \nu \left(\dfrac{d \overline{u}}{dy}\right)\Big|_{y=0} - \cancel{\rho\overline{u'v'}} \\
        \\
        =& \rho \nu \left(\dfrac{d \overline{u}}{dy}\right)\Big|_{y=0}
\end{array}
    
$$
"""

st.info(
    """
    :balloon: Since this derivative was already calculated,
    you already found the **shear velocity** at the bottom!""")

"""

### Wall zones

In a wall-bounded flow such as the channel from our lab, three zones
can be identified depending on which component of the shear stress
is most important

| Zone | Limits | Shear stress |
|:-----|:------:|:----------|
| Viscous sublayer |$y^+ < 5$| Viscous mostly |
| Buffer layer     |$5 < y^+ < 30$| Viscous and turbulence |
| log-law region   |$30 < y^+$ and $y/d < 0.3$| Turbulence mostly|

"""

st.plotly_chart(shearStressPlot(),use_container_width=True)

st.warning("Which is the vertical component of our velocity readings?")


r"""

### The log-law

For the **log-law** region of a channel flow, the velocity distribution
is given by:

$$
    u^+ = \dfrac{1}{\kappa} \ln{y^+} + B
$$

Where $\kappa = 0.41$ is the von Kármán constant and $B = 5.2$ 
is a fitting constant.
"""

st.info(
    r"""
    How can you connect the log-law with the curve $u_{\textsf{fit}}(y)$ 
    that you used to fit to your data?""")

r"""
## Other velocity profiles

:Notice how water goes up and downwards?:

## Reynolds stresses profiles

### Shear stress $\tau_0$ and shear velocity $u^*$

### Friction factor $f$

## Turbulent kinetic energy profile

## Eddy viscosity profile
"""