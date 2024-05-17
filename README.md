# My First LLM Chatbot
 An example LLM chatbot created with Cohere API and Streamlit

## Quick Start
1. [Fork and then clone this repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#about-forks) to a folder on your computer.
  
1. Open Visual Studio Code and then choose **File > Open Folder...** to open and edit the code.
  
1. Open the terminal window inside Visual Studio Code and type the following command to install the required Python packages.

   > pip install -r requirements.txt

4. Run the app by typing the following command in the terminal window. 
   > streamlit run chatbot.py
   
   A new browser window will open where you can interact with the chatbot.

> [!NOTE]
> You will need to enter your Cohere API key in the sidebar for the chatbot to work.

5. Make minor changes to the code, save and then run your app again to see what happens.

## Challenges
- Apply what you discovered working on your first LLM app to enhance the behaviour of the chatbot.
- [Complete 'Module 4: Deployment' of the LLMU course on Cohere.com](https://docs.cohere.com/docs/intro-deployment) to create a different kind of LLM powered app with Cohere and Streamlit.
- Read the [Streamlit Basics guide](https://docs.streamlit.io/get-started/fundamentals/main-concepts) for clues to help you extend the UI of this app further.

### Advanced Challenges
- Turn it into a [Retrieval Augmented Generation (RAG) app](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) by connecting it to your own data [using Langchain](https://docs.cohere.com/docs/cohere-and-langchain)
- Use [Streamlit secrets](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) to securely pass your API key to the app without having to type it into the sidebar.
> [!CAUTION]
> You should never include your API key in any code that you publish online, especially on GitHub. If someone copies your key they can access Cohere using your account without your permission. Creating a secret on Streamlit is the only way to publish your app to automatically use your API key without exposing it for the world to see.


