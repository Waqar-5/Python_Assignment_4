import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Set up Streamlit page
st.set_page_config(page_title="Virtual Plant Growth Simulator", page_icon="🌱")

# Title and description
st.title("🌱 Virtual Plant Growth Simulator 🌞")
st.markdown("""
    Welcome to the **Virtual Plant Growth Simulator**! 🌿  
    In this interactive simulation, you can control various factors such as sunlight and water to grow your virtual plant.  
    Watch it grow and thrive as you make choices in real-time! 🌻  
    Let's start gardening! 🌼
""")

# Plant growth simulation logic
class Plant:
    def __init__(self):
        self.height = 1  # Initial height of the plant
        self.water = 50  # Water level
        self.sunlight = 50  # Sunlight level
        self.growth_rate = 0.1  # Growth rate per interaction

    def water_plant(self):
        self.water += 10
        self.height += self.growth_rate

    def give_sunlight(self):
        self.sunlight += 10
        self.height += self.growth_rate

    def status(self):
        return f"Height: {self.height:.2f} cm, Water Level: {self.water}, Sunlight Level: {self.sunlight}"

# Initialize plant object
plant = Plant()

# Streamlit sliders for user interaction
water_amount = st.slider("Water your plant (1-100):", 1, 100, 50)
sunlight_amount = st.slider("Provide sunlight to your plant (1-100):", 1, 100, 50)

# Simulate growth
if st.button("Water the Plant"):
    plant.water_plant()
    st.success(f"You watered the plant! {plant.status()}")

if st.button("Provide Sunlight"):
    plant.give_sunlight()
    st.success(f"You provided sunlight! {plant.status()}")

# Generate plant growth plot
fig, ax = plt.subplots()
growth_data = np.linspace(1, plant.height, 100)
ax.plot(growth_data, label="Plant Growth", color='green', linewidth=3)
ax.set_title("Plant Growth Over Time")
ax.set_xlabel("Time")
ax.set_ylabel("Height (cm)")
ax.grid(True)
ax.legend()

# Display plot in Streamlit
st.pyplot(fig)

# Real-time feedback and fun facts
if plant.height > 10:
    st.balloons()
    st.markdown("""
        🎉 Wow! Your plant has grown quite tall! 🌿
        Keep going and it may reach new heights!
    """)

# Add a timer to simulate real-time growth
for i in range(5):
    time.sleep(1)
    plant.height += plant.growth_rate
    st.write(f"🌱 Growing... Current Height: {plant.height:.2f} cm")
