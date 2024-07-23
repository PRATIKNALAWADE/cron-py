## PyMotivator

Sure, here's a README file for your GitHub repository:

---

# Motivational Quotes WhatsApp Bot

This project sends daily inspirational quotes to a specified WhatsApp number using the Twilio API and the Quotes API. The quote is sent at a specified time each day using a cron job.

## Table of Contents

- [Motivational Quotes WhatsApp Bot](#motivational-quotes-whatsapp-bot)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Setup](#setup)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Files](#files)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

## Features

- Fetches daily inspirational quotes from the Quotes API.
- Sends the quote via WhatsApp using Twilio API.
- Uses a cron job to schedule daily messages.

## Setup

### Prerequisites

- Python 3.x
- A Twilio account with WhatsApp Sandbox configured
- Quotes API key
- `.env` file with the following variables:
  ```
  TWILIO_ACCOUNT_SID=your_account_sid_here
  TWILIO_AUTH_TOKEN=your_auth_token_here
  ```

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/motivational-quotes-whatsapp-bot.git
    cd motivational-quotes-whatsapp-bot
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your Twilio credentials:
    ```env
    TWILIO_ACCOUNT_SID=your_account_sid_here
    TWILIO_AUTH_TOKEN=your_auth_token_here
    ```

## Usage

1. Update the phone numbers in `twilio_connection.py`:
    - `from_='whatsapp:+14155238886'`: Replace with your Twilio WhatsApp number.
    - `to='whatsapp:+91123456780'`: Replace with the recipient's WhatsApp number.

2. Run the script:
    ```bash
    python cron.py
    ```

This will start the scheduler, and the quote will be sent daily at the specified time.

## Files

- `motivator.py`: Contains functions to fetch the quote and send it via WhatsApp.
- `twilio_connection.py`: Handles Twilio API connections and message sending.
- `cron.py`: Schedules the daily sending of the quote.
- `requirements.txt`: Lists the dependencies needed for the project.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Twilio](https://www.twilio.com) for the messaging API.
- [Quotes API](https://quotes.rest/) for the daily inspirational quotes.

---

### System Features and Requirements
	Functional Requirements
Python 3.10-dev / 3.8 (For heroku Deployment)
Requests
Twilio
APScheduler
	External Interface Requirements
Quotes of the Day API
Twilio Dashboard for WhatsApp
Visual Studio Code
GitHub
Heroku

	System Features
get_quote_of _the_day
	- takes category as parameter and returns the quote of the day

      -    set_twilio_connection
		- takes account_sid and account_token as parameter and returns client object

      - 	send_whatsapp_text
      		- takes quote and twilio client connection as parameters and returns message ID      

#### background_cron_job
	- takes send_whatsapp_text as a job to execute everyday in background
####  Assumptions and Dependencies
As the service for sending and receiving Quotes depends on Third party applications, it is assumed that they are always Up and Running.
The Project initially aims for learning Python by its latest version i.e 3.10-dev but this version is not available for Heroku hence we would need to downgrade the python version to 3.8 for supporting heroku deployment.
Other Non Functional Requirements
Security - All the keys and passwords to be stored as Environment variables
Quality - Code quality and PEP8 Standards
Performance - Deployment on Heroku for scaling, newer Python version with updated Libraries

