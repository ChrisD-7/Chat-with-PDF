Certainly! Here's how you can incorporate the reference to the video and mention the vector database in your README, along with a note about your GitHub profile:

```markdown
# ChatGPT PDF Chatbot

ChatGPT PDF Chatbot is an innovative Streamlit application designed to make interacting with PDF documents as natural as having a conversation. This tool extracts text from PDFs and leverages a powerful vector database for context-aware conversations using natural language processing.

## Features

- **PDF Text Extraction**: Upload PDF documents to extract text for analysis.
- **Conversational Interface**: Chat with the application to ask questions and receive answers from the PDF contents.
- **Vector Database**: Utilizes a vector database (FAISS) for efficient retrieval of contextually relevant information.
- **Continuous Interaction**: Allows for an ongoing conversation, maintaining context across inquiries.
- **User-Friendly Design**: Aesthetic and responsive interface to enhance user experience.

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- Active internet connection
- Required API keys for external services (e.g., OpenAI API key)

### Installation

Clone the repository and navigate into it:

```sh
git clone https://github.com/ChrisD-7/chatgpt-pdf-chatbot.git
cd chatgpt-pdf-chatbot
```

Install dependencies:

```sh
pip install -r requirements.txt
```

### Running the Application

Execute the Streamlit app:

```sh
streamlit run app.py
```

Visit `http://localhost:8501` in your web browser.

## Built With

- [Streamlit](https://www.streamlit.io/) - The framework for turning data scripts into shareable web apps.
- [FAISS](https://github.com/facebookresearch/faiss) - A library for efficient similarity search and clustering of dense vectors.
- [PyPDF2](https://pypdf2.readthedocs.io/en/latest/) - A PDF file reading library.
- [LangChain](https://github.com/LangChain/langchain) - Your toolkit for building language model applications.

## Acknowledgements

This project was inspired by the tutorial from [TensorWork's YouTube video on building a ChatGPT with PDFs](https://youtu.be/uus5eLz6smA?feature=shared).

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for how to make contributions. We welcome your ideas and collaboration.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For available versions, see the [tags on this repository](https://github.com/ChrisD-7/chatgpt-pdf-chatbot/tags).

## Author

- **Chris D** - *Initial Creator* - [ChrisD-7](https://github.com/ChrisD-7)

Check out also the list of [contributors](https://github.com/ChrisD-7/chatgpt-pdf-chatbot/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Make sure to create the `CONTRIBUTING.md` and `LICENSE` files in your repository if they do not already exist, and provide the actual content for them. The `LICENSE` file should contain the full text of the license under which your project is released. If you are using the MIT License, you can find the standard text for this license online. The `CONTRIBUTING.md` file should contain instructions for how others can contribute to your project.

Additionally, you may want to check that all links are correct, especially those pointing to your GitHub repository and the contributors' page.
