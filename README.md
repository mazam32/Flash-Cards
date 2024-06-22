# Flashy: Flash Card Learning Application

## Description

Flashy is a simple flash card application designed to help users learn German vocabulary. The application displays a German word, waits for a few seconds, and then flips the card to show the English translation. Users can navigate through the flashcards using the provided buttons to indicate whether they know the word or not.

## Features

- Displays a German word on the flash card.
- Flips the card after a set time to reveal the English translation.
- Buttons to navigate to the next word, indicating whether the user knew the word or not.
- Attractive UI with front and back images for the flash cards.

## Requirements

- Python 3.x
- Tkinter
- pandas

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   ```
2. **Navigate to the project directory:**
   ```sh
   cd flash-card-project
   ```
3. **Install the required libraries:**
   ```sh
   pip install pandas
   ```

## Usage

1. **Run the application:**
   ```sh
   python main.py
   ```
2. **Start the flash card session:**
   - Click the "Start" button to begin.
   - A German word will be displayed on the card.
   - After 3 seconds, the card will flip to show the English translation.
   - Use the right and wrong buttons to navigate to the next word based on your knowledge.

## File Structure

```
flash-card-project/
│
├── data/
│   └── german_words.csv
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
│
├── main.py
└── README.md
```

## Code Explanation

### main.py

- **Importing Libraries:**
  ```python
  from tkinter import *
  import pandas as pd
  import random
  ```

- **Load Data:**
  ```python
  all_words = pd.read_csv("/path/to/german_words.csv")
  ```

- **Generate Word Function:**
  Displays a random German word and sets a timer to flip the card.
  ```python
  def generate_word(correct):
      ...
  ```

- **Flip Card Function:**
  Flips the card to show the English translation.
  ```python
  def flip_card(random_index):
      ...
  ```

- **Start Function:**
  Starts the flash card session.
  ```python
  def start():
      ...
  ```

- **UI Setup:**
  Configures the main window, canvas, and buttons.
  ```python
  window = Tk()
  window.title("Flashy")
  ...
  ```

## Customization

- **Change Background Color:**
  Modify the `BACKGROUND_COLOR` variable at the top of the `main.py` file.
  ```python
  BACKGROUND_COLOR = "#B1DDC6"
  ```

- **Change Flash Card Images:**
  Replace the images in the `images` directory with your custom images.

- **Change CSV File:**
  Replace `german_words.csv` with your custom CSV file containing words you want to learn.

## Contributing

Feel free to fork the project and submit pull requests. Any contributions are welcome!

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to all contributors and users who provided feedback and suggestions.

---

For any issues or feature requests, please open an issue on GitHub.