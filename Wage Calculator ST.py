import streamlit as st

st.title("Basic-ass Wage Calculator 💰")

hourly = st.number_input('Hourly Rate: ', min_value=0.0)

if hourly > 0:
    hourly = float(hourly)
    daily = hourly * 7
    biweekly = daily * 10
    monthly = biweekly * 2
    annually = monthly * 12
    st.write(f"Based on hourly rate of ${hourly:.2f}/h:")
    st.write(f"Daily Rate:     ${daily:,.2f}")
    st.write(f"Biweekly Rate:  ${biweekly:,.2f}")
    st.write(f"Monthly Rate:   ${monthly:,.2f}")
    st.write(f"Annual Rate:    ${annually:,.2f}")
    print()
    hourly = input('Enter another hourly rate, or press enter to end session: ')

    
    
