import random
import tkinter as tk

# Define the responses

responses = {
    "hello": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
    "oil change": [
        "To change your vehicle's oil, follow these steps:",
        "1. Lift the car using a jack.",
        "2. Locate the oil drain plug and remove it to drain the old oil.",
        "3. Replace the oil filter.",
        "4. Add new oil according to your vehicle's specifications.",
    ],
    "wheel maintenance": [
        "For wheel maintenance, you can follow these steps:",
        "1. Inspect the tire pressure and adjust it to the recommended level.",
        "2. Check the tire tread depth and replace worn-out tires.",
        "3. Ensure that wheel nuts or bolts are properly tightened.",
        "4. Regularly balance and align the wheels for a smoother ride.",
    ],
    "window maintenance": "To maintain your car's windows, keep them clean and lubricate the window tracks regularly.",
    "car paint maintenance": "To maintain your car's paint, wash it regularly, wax to protect the finish, and fix any scratches promptly.",
    "suspension maintenance": [
        "For suspension maintenance, consider the following:",
        "1. Inspect shock absorbers or struts for signs of wear and leakage.",
        "2. Check suspension components for any damage or loose parts.",
        "3. Ensure proper alignment for even tire wear and smooth handling.",
    ],
    "engine maintenance": [
        "To maintain your car's engine, follow these steps:",
        "1. Change the engine oil and oil filter regularly as per the manufacturer's recommendations.",
        "2. Keep the air filter clean or replace it as needed to ensure optimal air intake.",
        "3. Check and maintain the cooling system, including the radiator and coolant levels.",
        "4. Regularly inspect and replace worn-out spark plugs and ignition components.",
    ],
    "tire rotation": [
        "Tire rotation is essential for even tire wear. Here's how to do it:",
        "1. Lift the car using a jack and secure it with jack stands.",
        "2. Remove each tire and wheel and switch their positions according to the recommended rotation pattern.",
        "3. Reinstall the tires and tighten the lug nuts to the manufacturer's specifications.",
        "4. Lower the car and ensure all tires are properly inflated.",
    ],
    "brake maintenance": [
        "Proper brake maintenance is crucial for safety. Here's what to do:",
        "1. Regularly check the brake fluid level and top it off if necessary.",
        "2. Inspect brake pads and rotors for wear and replace them when needed.",
        "3. Check brake lines and hoses for signs of damage or leaks.",
        "4. Bleed the brake system if you notice spongy brake pedal feel or reduced braking performance.",
    ],
    "car speed": [
        "Maintaining the right speed is essential for safety and fuel efficiency.",
        "1. Always obey posted speed limits and adjust your speed to road and weather conditions.",
        "2. Smooth acceleration and deceleration can help improve fuel efficiency.",
        "3. Avoid excessive speeding, as it can lead to accidents and increased wear on your vehicle.",
        "4. Use cruise control on highways to maintain a constant speed and improve fuel economy.",
    ],
    "high-performance tuning": [
        "If you're interested in boosting your car's performance, consider the following:",
        "1. Upgrading your car's air intake and exhaust system for improved airflow.",
        "2. Installing performance chips or tuners to optimize engine parameters.",
        "3. Upgrading suspension components for better handling at high speeds.",
        "4. Choosing high-performance tires and brakes for improved stopping power and traction.",
    ],
    "electric vehicle (EV) maintenance": [
        "EVs require different maintenance compared to traditional cars. Here's what to keep in mind:",
        "1. Regularly charge your EV according to manufacturer recommendations.",
        "2. Check the battery health and plan for replacement if needed in the future.",
        "3. Keep the electric motor and inverter system in good condition for optimal performance.",
        "4. Maintain the regenerative braking system for efficient energy recovery.",
    ],
    "battery maintenance":[
        "Proper battery maintenance is important to ensure reliable starting and electrical system performance. Here's what you can do:",
        "1. Check the battery terminals and cables for corrosion. Clean them with a wire brush and a mixture of baking soda and water.",
        "2. Inspect the battery case for any signs of damage, cracks, or bulging. Replace the battery if you notice any of these issues.",
        "3. Ensure the battery is securely mounted in its tray to prevent vibrations and damage.",
       "4. Test the battery's voltage regularly to make sure it's within the recommended range. If it falls below the specified voltage, consider charging or replacing it.",
       "5. If your vehicle is not in regular use, consider using a battery maintainer or tender to keep the battery charged.",
       "6. Be mindful of extreme temperatures as they can affect battery performance. In cold weather, ensure the battery has enough cranking power, and in hot weather, monitor for overheating.",
    ],
    "help": "I'm here to help you with your vehicle maintenance needs. You can ask about maintenance, service history, or spare parts availability.",
    "default": [
        "I'm sorry, I don't understand.",
        "I didn't quite get that. Could you please rephrase?",
        "I'm here to assist you with vehicle maintenance questions.",
        "Feel free to ask about maintenance, service history, or spare parts availability.",
    ],
}


def generate_response(user_input):
    user_input = user_input.lower()

    maintenance_keywords = {
        "oil": responses["oil change"],
        "wheel": responses["wheel maintenance"],
        "window": responses["window maintenance"],
        "paint": responses["car paint maintenance"],
        "suspension": responses["suspension maintenance"],
        "engine": responses["engine maintenance"],
        "tire": responses["tire rotation"],
        "brake": responses["brake maintenance"],
        "speed": responses["car speed"],
        "performance": responses["high-performance tuning"],
        "electric": responses["electric vehicle (EV) maintenance"],
        "battery": responses["battery maintenance"],
    }

    for keyword, response in maintenance_keywords.items():
        if keyword in user_input:
            if isinstance(response, list):
                return random.choice(response)
            else:
                return response

    return random.choice(responses["default"])


def send_message():
    user_input = entry.get()
    bot_response = generate_response(user_input)
    display_message("You: " + user_input)
    display_message("Bot: " + bot_response)
    entry.delete(0, tk.END)  # Clear the input field after sending

def display_message(message):
    text_display.insert(tk.END, message + "\n")
    text_display.see(tk.END)

top = tk.Tk()
top.title("Chatbot UI")
top.geometry("600x400")
top.config(bg="sky blue")

entry = tk.Entry(top, width=40)
entry.pack(pady=10)

send_button = tk.Button(top, text="Send", command=send_message)
send_button.pack()

text_display = tk.Text(top, height=10, width=60)
text_display.pack()

# Initialize the chat with a greeting message
display_message("Bot: Hello! How can I assist you today?")

top.mainloop()