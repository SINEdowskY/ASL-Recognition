# ASL Recognition with OpenCV

Welcome to the ASL Recognition project! This project aims to recognize American Sign Language (ASL) gestures using OpenCV in Python.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

American Sign Language (ASL) is a complete, complex language that employs signs made by moving the hands combined with facial expressions and postures of the body. This project utilizes computer vision techniques to recognize and interpret ASL gestures in real-time.

## Features

- **Real-time Recognition**: Utilize OpenCV to perform real-time ASL gesture recognition.
- **Gesture Detection**: Detect hand gestures from video input.
- **Model Integration**: Integrate machine learning models for gesture classification.
- **Graphical User Interface (GUI)**: Develop a user-friendly interface for interaction.

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:SINEdowskY/ASL-Recognition.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ASL-Recognition
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv env
    ```

4. Activate the virtual environment:

    - On Windows:

    ```bash
    env\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source env/bin/activate
    ```

5. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application**: Execute the main script to start the ASL recognition application.

    ```bash
    python test.py
    ```

2. **Gesture Recognition**: Position your hand in front of the camera and perform ASL gestures. The application will attempt to recognize and display the corresponding ASL alphabet or word.

3. **Customization**: Modify the code to add new gestures, improve recognition accuracy, or integrate additional features.

## Contributing

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, feel free to open an issue or create a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
