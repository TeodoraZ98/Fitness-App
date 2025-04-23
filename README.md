# Transform Zone – Fitness Web App

**Transform Zone** is a professional-grade fitness web application designed to help users optimize their health through smart nutrition, personalized meal planning, and evidence-based supplement guidance. Built with Streamlit, the app delivers a seamless user experience and includes premium features, real-time calculations, and user account functionality.

## Features

- **Macro & Calorie Calculators**  
  Input personal data and fitness goals to calculate your Total Daily Energy Expenditure (TDEE) and macronutrient needs.

- **Personalized Meal Plans**  
  Generate meal plans tailored to your calorie and macro targets, powered by the Spoonacular API.

- **Supplement Recommendations**  
  Access science-backed supplement suggestions based on your goals (e.g., muscle gain, fat loss, recovery).

- **Premium Membership**  
  Unlock advanced features, including progress tracking, downloadable meal plans, and expert support.

- **User Authentication**  
  Secure login and registration system using `streamlit-authenticator` with bcrypt hashing.

- **Responsive Design**  
  Customized CSS for a modern, dark-themed UI across all pages.

- **Multipage Navigation**  
  Built with Streamlit's multipage architecture, allowing smooth transitions between pages such as Home, Calculator, Meals, Supplements, Login, Premium, and more.

## Tech Stack

- **Frontend/UI:** Streamlit with custom HTML/CSS
- **Authentication:** streamlit-authenticator, bcrypt
- **Meal Data:** Spoonacular API
- **Routing Enhancements:** streamlit-extras
- **PDF Export (Premium):** fpdf or reportlab (if implemented)

## Folder Structure

```
fitness-app/
│
├── Home.py
├── Pages/
│   ├── 1_Calculator.py
│   ├── 2_Meals.py
│   ├── 3_Premium.py
│   ├── 4_Supplements.py
│   ├── 5_Login.py
│   ├── 6_Privacy.py
│   └── 7_Terms.py
├── theme.py
├── logo.png
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fitness-app.git
cd fitness-app
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run Home.py
```

## Deployment

The app is deployed on [Streamlit Cloud](https://transform-zone.streamlit.app) and updates automatically with each push to the `main` branch.

## Future Improvements

- Mobile responsiveness
- AI-generated meal suggestions
- Subscription-based payment system
- Integrated workout tracker

## License

This project is open-source and available under the MIT License.

## Author

Teodora Zlatanovic  
Computer Science graduate specializing in software development, based in Serbia.  
GitHub: [github.com/TeodoraZ98](https://github.com/TeodoraZ98)
