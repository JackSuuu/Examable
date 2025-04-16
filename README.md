# Examable

**Examable** is a prototype application designed to assist students in locating past exam questions and answers through Optical Character Recognition (OCR) and Natural Language Processing (NLP) techniques. It processes scanned exam papers, extracts textual content, and enables semantic search to find relevant questions and answers.

![alt text](Assets/app.png)

## Features

- **OCR Integration**: Converts scanned PDF exam papers into machine-readable text.
- **Semantic Search**: Utilizes NLP to perform similarity-based searches, retrieving questions and answers that closely match user queries.
- **Subject Categorization**: Organizes papers by subjects such as Mathematics and Computer Science for targeted searching.
- **GUI Interface**: Provides a user-friendly interface built with PyQt5 for easy interaction.

---

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/JackSuuu/Examable.git
   cd Examable
   ```

2. **Install Dependencies**:

   Ensure you have Python 3.x installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

   *Note*: The `requirements.txt` file should list all necessary dependencies. If it's missing, you'll need to manually install packages such as `PyQt5`, `pytesseract`, `pdf2image`, and `spacy`.

3. **Set Up OCR Engine**:

   Install Tesseract OCR engine:

   - **Windows**: Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) and follow the installation instructions.
   - **macOS**: Use Homebrew:

     ```bash
     brew install tesseract
     ```

   - **Linux**: Use your distribution's package manager, e.g., for Debian/Ubuntu:

     ```bash
     sudo apt-get install tesseract-ocr
     ```

4. **Download NLP Model**:

   Download the SpaCy English language model:

   ```bash
   python -m spacy download en_core_web_lg
   ```

---

## Usage

1. **Launch the Application**:

   Run the main GUI script:

   ```bash
   python pyqt5_Examable_new.py
   ```

2. **Search for Questions**:

   - Use the GUI to select the subject area.
   - Input your query into the search bar.
   - The application will process the query, perform OCR on relevant documents, and display matching questions and answers.

---

## Project Structure


```plaintext
Examable/
├── pyqt5_Examable_new.py        # Main GUI application
├── Examable_source_code.py      # Core logic for processing and searching
├── OCR_img.py                   # Handles OCR processing of images
├── Get_PDF_text.py              # Extracts text from PDF files
├── Similarity.py                # Computes similarity between queries and document content
├── OutPut_Pdf_page.py           # Outputs processed PDF pages
├── Replace_to_answer.py         # Replaces placeholders with actual answers
├── go_thorugh_folder.py         # Traverses directories to locate files
├── open_certain_file.py         # Opens specified files
├── requirements.txt             # Lists project dependencies
├── en_core_web_lg/              # SpaCy language model directory
├── icon.icns                    # Application icon
└── README.md                    # Project documentation
```

---

## Limitations

- **Performance**: The current implementation indexes each page individually, leading to slower search times.
- **Prototype Status**: As a prototype, the application may have unresolved issues and lacks comprehensive error handling.
- **OCR Accuracy**: The accuracy of OCR depends on the quality of scanned documents; poor scans may lead to incorrect text extraction.

---

## Contributing

Contributions are welcome! If you'd like to improve Examable, please fork the repository and submit a pull request. For major changes, open an issue first to discuss what you'd like to change.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**Jack Suuuu**

- GitHub: [JackSuuu](https://github.com/JackSuuu)
- University of Edinburgh, BSc Computer Science Student

---

Feel free to customize this `README.md` further to match any additional details or specific instructions related to your project. 
