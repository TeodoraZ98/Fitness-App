import bcrypt
import streamlit as st

# --- PASSWORD UTILS ---
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

# --- MOCK GPT MEAL PLAN GENERATOR ---
def generate_meal_plan(prompt_text):
    # Simulated response for testing layout without using OpenAI API
    return f"""
🧪 [TEST MODE] Here’s a sample meal plan for: **{prompt_text}**

🍳 **Meal 1**: Scrambled eggs with spinach and avocado  
🥗 **Meal 2**: Grilled chicken salad with olive oil and almonds  
🍛 **Meal 3**: Baked salmon with quinoa and steamed broccoli  
🍓 **Snack**: Greek yogurt with chia seeds

🛒 **Grocery List**:  
- Eggs  
- Spinach  
- Avocado  
- Chicken breast  
- Mixed greens  
- Olive oil  
- Almonds  
- Salmon  
- Quinoa  
- Broccoli  
- Greek yogurt  
- Chia seeds
"""
