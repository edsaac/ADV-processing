import streamlit as st

st.set_page_config(
    page_title="[NU CEE440] - Uniform flow",
    page_icon="🏞️",
    layout="wide",
    initial_sidebar_state="collapsed"
 )

r"""
# **Uniform flow and analysis from macro parameters**

## Flow rate $Q$

This was measured with the flowmeter in the return pipe of the channel.

## Channel dimensions

The **depth** $y$ of the channel was measured in the lab, whereas the width 
is $L_w = 0.29 \, \mathrm{m}$ for the flume used. 

For a rectangular channel, the **cross-sectional** area $A_C$ and the 
**wetted perimeter** $P_W$ are given by

$$
    A_C = L_w \cdot y
$$

$$
    P_W = 2y + L_w
$$

The ratio between these two quantities give the **hydraulic radius** $R_H$

$$
    R_H = \dfrac{A_C}{P_W}
$$

### Slope $S_0$

## Mean velocity $U$

## Reynolds number $\mathcal{R}$

## Shear stress

The **shear stress** $\tau_0$ at the bottom of the channel is given by

$$
    \tau_0 = \rho g R_H S_0
$$

Where \rho is the water density and g is the gravitational acceleration
The shear velocity $u^*$ is:

$$
    u^* = \sqrt{\dfrac{\tau_0}{\rho}}
$$


### Darcy-Weisbach friction factor $f$

### Roughness height $k_s$

### Thickness of the laminar sublayer $\delta$

"""