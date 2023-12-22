# AI ThinkTank
AI ThinkTank can be accessed [here](https://thinktank.streamlit.app/).

AI ThinkTank leverages the power of Large Language Models to simulate expert debates on any topic. Users can insert an image URL and the system automatically generates a topic of debate based on the image, using Gemini Pro Vision. Thereafter the system dynamically generates relevant experts who autonomously engage in a debate. Additionally, users have the option to join the discussion, adding an interactive element to the experience. 

## Getting Started
1. **Install Dependencies**
    Navigate to the cloned repository directory and install the required Python packages in your virtual environment:
    
    `pip install -r requirements.txt`
    
2. **Run the Application**
    To start the application, run:    
    
    `streamlit run main.py`
    
    This will launch the Streamlit web server and AI ThinkTank should be accessible in your web browser.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
- AI ThinkTank was inspired by the [MAD Framework](https://github.com/Skytliang/Multi-Agents-Debate) 
- The project makes use of the [LangChain Framework](https://www.langchain.com/)
- The project uses Gemini Pro Vision and Gemini Pro
