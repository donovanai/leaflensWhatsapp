# leaflensWhatsapp

leaflensWhatsapp is a WhatsApp bot designed to assist with plant identification and health analysis.

## Features
- Send automated responses
- Handle user queries via WhatsApp
- Analyze plant health using GPT-4.0 mini
- Limit users to 3 free messages per day
- Redirect users to a Stripe checkout page for subscriptions
- Use Supabase for user authentication, message tracking, and payment status

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/donovanai/leaflensWhatsapp.git
   ```
2. Navigate to the project directory:
   ```bash
   cd leaflensWhatsapp
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the bot:
```bash
uvicorn src.main:app --reload
```

## Configuration
Update the configuration settings in `src/config.py` as needed.

## Deployment
Deploy the application on Railway.

## Contributing
Contributions are welcome! Please create an issue or submit a pull request.

## License
This project is licensed under the MIT License.