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
"""

cols = st.columns([2,1,1])

with cols[0]:
    r"""

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
    """

    """
    The ratio between these two quantities give the **hydraulic radius** $R_H$

    $$
        R_H = \dfrac{A_C}{P_W}
    $$

    Finally, the channel slope $S_f$ was measured during the lab. 
    """

    st.warning("How is $S_f$ calculated from those readings?")

with cols[1]:
    st.image("./assets/widthchannel.jpg",
        use_column_width=True,
        caption="Channel width")

with cols[2]:
    st.image("./assets/slopemeter.jpg",
        use_column_width=True,
        caption="Measuring the slope of the channel.")

"""
****
## Flow parameters
"""

col1, col2 = st.columns([2,1])

with col1:
    r"""
    The volumetric **flow rate** $Q$ was measured with the flowmeter in the 
    return pipe of the channel. Use these readings to calculate the 
    **bulk velocity** $U$:

    $$
        U = \dfrac{Q}{A_C}
    $$

    The Reynolds number $\mathcal{R}$ for a channel is defined as

    $$
        \mathcal{R} = \dfrac{4 U R_H}{\nu}
    $$

    Where $\nu$ is the kinematic viscosity of water
    """

    st.info(
        """
        Was the flow in the channel *turbulent*? 
        Confirm this with the Reynolds number
        """ )

with col2:
    st.image("./assets/flowmeter.jpg",use_column_width=True,
        caption="Volumetric flowmeter.")

r"""
****
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
"""

st.info(r"What are the units of $\tau_0$ and $u^*$?")

r"""
The thickness of the viscous (a.k.a. laminar) sublayer $\delta_v$ can be 
approximated to

$$
    \delta_v = 
$$

"""

r"""
****

## Friction factor

The Darcy-Weisbach equation for open channel flow is 

$$
    S_f = f \dfrac{1}{4R_H}\dfrac{U^2}{2g}
$$

where $f$ is the friction factor and $S_f$ is the energy line slope, which, for
uniform flow is assumed to be equal to the bottom slope $S_0$
"""

st.info("Solve for $f$ to obtain the friction factor. What are the units of $f$?")

r"""
Semi-empirical relationships exist between the Reynolds number, the friction
factor and the bottom roughness $k_s$, for instance,

$$
    \dfrac{1}{\sqrt{f}} = -2 \log{\left( \dfrac{k_s}{12R_H} + \dfrac{2.5}{\mathcal{R}\sqrt{f}} \right)}
$$

"""

st.info(
    """
    - Check that the units on this equation are consistent
    - Solve for $k_s$.
    - Is the result close to your roughness measurement?"""
    )
