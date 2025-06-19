import streamlit as st
import pandas as pd
import altair as alt

# Load data
df = pd.read_csv("listings_sample.csv", parse_dates=["date_listed"])

# Title
st.title("🏠 Ottawa Listing Pulse")
st.markdown("Live dashboard showing listing trends across Ottawa neighborhoods.")

# KPI summary
active_listings = df[df['status'].str.lower() == 'active']
total_active = active_listings.shape[0]
new_this_month = df[df['date_listed'] >= pd.to_datetime("2025-06-01")].shape[0]

# Safe average price calculation
active_listings["price"] = pd.to_numeric(active_listings["price"], errors="coerce")
avg_price_float = active_listings["price"].mean()
avg_price = int(avg_price_float) if pd.notna(avg_price_float) else 0

# KPI display
col1, col2, col3 = st.columns(3)
col1.metric("Active Listings", total_active)
col2.metric("New This Month", new_this_month)
col3.metric("Avg Price (Active)", f"${avg_price:,.0f}")

# Listings by neighborhood
st.subheader("📍 Listings by Neighborhood")
neigh_counts = active_listings["neighborhood"].value_counts().reset_index()
neigh_counts.columns = ["Neighborhood", "Active Listings"]
st.bar_chart(neigh_counts.set_index("Neighborhood"))

# Price trend by neighborhood
st.subheader("📈 Average Price by Neighborhood")
price_by_neigh = active_listings.groupby("neighborhood")["price"].mean().reset_index()
price_chart = alt.Chart(price_by_neigh).mark_bar().encode(
    x=alt.X('neighborhood:N', title='Neighborhood'),
    y=alt.Y('price:Q', title='Avg Price'),
    tooltip=['neighborhood', 'price']
).properties(width=600, height=400)
st.altair_chart(price_chart)

# Download option
st.subheader("⬇️ Download Full Dataset")
st.download_button("Download CSV", data=df.to_csv(index=False), file_name="ottawa_listings.csv", mime="text/csv")

# Footer
st.markdown("---")
st.caption("Built with 💻 by your solo data analyst.")

