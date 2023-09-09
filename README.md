# Voice Controlled Home Assistant

This is a voice controlled home assistant that can be used to control various home appliances using voice commands. It is built using Python and Flask. It has a frontend with a microphone button that can be used to record voice commands. The voice commands are then sent to the Flask server, which processes them and sends the appropriate commands to the Raspberrypi. The Raspberrypi then controls the home appliances using the appropriate hardware.

## Prerequisites

Before running the Flask server, ensure that you have the following installed on your system:

- Python: Make sure you have Python installed on your machine. You can download it from the official Python website (<https://www.python.org/downloads/>).

## Installation

1. Clone the repository:

   ````bash
   git clone https://github.com/TEAM-ALPHAWAVE/voice_control_home_assistant.git
   ```````

2. Navigate to the project directory:

   ````bash
   cd voice_control_home_assistant
   ```````
   
   

3. Create a virtual environment (optional, but recommended):

   ````bash
   python -m venv venv
   ``````

4. Activate the virtual environment:
   - For Windows:

     ```
     venv\Scripts\activate
     ```

   - For macOS and Linux:

     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ````
   pip install -r requirement.txt
   ``````

## Usage

1. Once the installation is complete, you can start the Flask server by running the following command:

   ````
   python app.py
   ```

2. You should see output similar to the following:

   ````
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```

3. Open your web browser and navigate to `http://127.0.0.1:5000/` or `http://localhost:5000/`. You should see the default Flask page.

4. To stop the server, press `CTRL+C` in the terminal window where the server is running.

## Customization

- **Changing the Port**: By default, the Flask server runs on port `5000`. If you want to use a different port, open the `app.py` file and modify the following line:

   ````python
   app.run(port=5000)
   ```
   Replace `5000` with your desired port number.

- **Modifying the Routes**: The Flask server comes with a default route at the root URL (`/voice`). If you want to add additional routes or modify the existing ones, open the `app.py` file and follow the Flask routing syntax. You can define routes and their corresponding functions using the `@app.route` decorator.

## Conclusion

That's it! You have successfully set up the  Flask server. You can now use this server to run this voice controlled home assistant.
