import streamlit as st

st.set_page_config(
    page_title="[NU CEE440] - Uniform flow",
    page_icon="🏞️",
    layout="wide",
    initial_sidebar_state="collapsed"
 )

r"""
# 🏞️ **Uniform flow characterization**

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

Finally, the channel slope $S_0$ was measured during the lab.

## Flow parameters

The volumetric **flow rate** $Q$ was measured with the flowmeter in the 
return pipe of the channel. The **bulk velocity** $U$

$$
    U = \dfrac{Q}{A_C}
$$

The Reynolds number $\mathcal{R}$ for a channel is defined as

$$
    \mathcal{R} = \dfrac{4 U R_H}{\nu}
$$

Where \nu is the kinematic viscosity of water

## Shear stress

The **shear stress** $\tau_0$ at the bottom of the channel is given by

$$
    \tau_0 = \rho g R_H S_0
$$

Where $\rho$ is the water density and $g$ is the gravitational acceleration. 
The shear velocity $u^*$ is:

$$
    u^* = \sqrt{\dfrac{\tau_0}{\rho}}
$$

The Darcy-Weisbach equation for open channel flow is 

$$
    S_f = f \dfrac{1}{4R_H}\dfrac{U^2}{2g}
$$

where $f$ is the friction factor and $S_f$ is the energy line slope, which, for
uniform flow is assumed to be equal to the channel slope $S_0$

Semi-empirical relationships exist between the Reynolds number, the friction
factor and the bottom roughness $k_s$, for instance,

$$
    \dfrac{1}{\sqrt{f}} = -2 \log{\left( \dfrac{k_s}{12R_H} + \dfrac{2.5}{\mathcal{R}\sqrt{f}} \right)}
$$

### Boundary layer

The thickness of the laminar sublayer $\delta$

"""