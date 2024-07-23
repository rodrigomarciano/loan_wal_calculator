import streamlit as st

def calculate_weighted_average_life(maturities):
    total_weighted_sum = 0
    total_principal = sum(maturities)

    for year, principal in enumerate(maturities, start=1):
        total_weighted_sum += year * principal

    if total_principal == 0:
        return 0

    weighted_average_life = total_weighted_sum / total_principal
    return weighted_average_life

st.title("Loan Weighted Average Life Calculator")

st.write("Enter the principal amounts for each year (up to 20 years).")
st.write("Leave a field empty or enter 0 to stop entering data.")

maturities = []
for year in range(1, 21):
    amount = st.number_input(f"Year {year}", min_value=0.0, format="%.2f", key=f"year_{year}")
    if amount > 0:
        maturities.append(amount)
    else:
        break

if st.button("Calculate Weighted Average Life"):
    if maturities:
        wal = calculate_weighted_average_life(maturities)
        st.success(f"Weighted Average Life: {wal:.2f} years")
    else:
        st.error("Please enter at least one non-zero principal amount.")
