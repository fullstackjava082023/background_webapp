<!-- create a readme to explain that this is simple application which showing background color depends on .env parameter APP_COLOR and create instructions to setup and run it : should contain install from requirements.txt and setup .env -->
## Simple Application

This is a simple application that displays a background color based on the value of the `APP_COLOR` parameter in the `.env` file.

### Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Install the required dependencies from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory of the project and set the `APP_COLOR` parameter to the desired color value. For example:

    ```plaintext
    APP_COLOR=blue
    ```

    You can choose any valid CSS color value.

### Running the Application

To run the application, execute the following command:

```bash
python app.py
```

The application will start on port 5000 and display the background color based on the value of the `APP_COLOR` parameter in the `.env` file.

