# 🌸 AI Anime Recommender (LLMOps) 🎌

Welcome to the **AI Anime Recommender** project! This is an end-to-end LLMOps project that provides personalized anime recommendations using large language models, deployed on a robust Kubernetes cluster with real-time monitoring.

> **Note:** There is a detailed documentation (`FULL_DOCUMENTATION.md`) which contains comprehensive steps for the complete deployment pipeline, including:
> 1. Initial Setup
> 2. Configure VM Instance
> 3. Configure Minikube inside VM
> 4. Interlink your Github on VSCode and on VM
> 5. Build and Deploy your APP on VM
> 6. GRAFANA CLOUD MONITORING

## 🏗️ Architecture

![AI Anime Recommender Workflow](Architecture/AI+Anime+Recommender+Workflow.png)

## 📊 Dataset

The system relies on a rich dataset located in the `data/` directory, containing comprehensive anime metadata:
- 📁 `data/anime_updated.csv`
- 📁 `data/anime_with_synopsis.csv`

## ✨ Features

- 🧠 **AI-Powered Recommendations:** Utilizes LangChain, Groq, and HuggingFace for intelligent, context-aware anime suggestions.
- 🗄️ **Vector Database:** Integrates ChromaDB for blazingly fast similarity search and efficient context retrieval.
- 💻 **Interactive UI:** Built with Streamlit for a sleek, responsive, and seamless user experience.
- 🐳 **Containerized:** Fully Dockerized application ensuring consistent and reliable deployments anywhere.
- ☸️ **Kubernetes Orchestration:** Managed using Kubernetes (Minikube) for robust scaling and orchestration.
- ☁️ **Cloud Deployment:** Hosted seamlessly on Google Cloud Platform (GCP) VM instances.
- 📈 **Observability:** Real-time metrics and monitoring powered by Grafana Cloud and Helm charts.

## 🛠️ Technology Stack

- 🐍 **Language:** Python 3.14
- 🎨 **Framework:** Streamlit
- 🦜 **LLM Orchestration:** LangChain
- 🤖 **Models & Embeddings:** Groq API, HuggingFace, Sentence Transformers
- 🗃️ **Vector Database:** ChromaDB
- 📦 **Containerization:** Docker
- ⚓ **Orchestration:** Kubernetes (K8s), Minikube
- 👁️ **Monitoring:** Grafana Cloud, Helm
- ☁️ **Cloud Provider:** Google Cloud Platform (GCP)

## 📁 Project Structure

```text
.
├── app/                  # Streamlit application files (app.py)
├── Architecture/         # Project architecture diagrams and design docs
├── chroma_db/            # Local vector database storage
├── config/               # Configuration settings and environment variables
├── data/                 # Raw dataset files (CSV)
├── Outputs/              # Generated outputs and logs
├── pipeline/             # Data ingestion and processing pipelines
├── src/                  # Core source code and business logic
├── utils/                # Helper functions and utilities
├── Dockerfile            # Instructions to containerize the application
├── llmops-k8s.yaml       # Kubernetes deployment configuration
├── requirements.txt      # Python dependencies
├── setup.py              # Packaging script
└── FULL_DOCUMENTATION.md # Detailed deployment documentation
```

## ⚙️ Local Development Setup

### 1. Prerequisites
Ensure you have the following installed:
- Python 3.14
- Docker
- Git

### 2. Clone the Repository
```bash
git clone https://github.com/pamuarun/ANIME-RECOMMENDER-LLMOPS.git
cd ANIME-RECOMMENDER-LLMOPS
```

### 3. Install Dependencies
Create a virtual environment and install the required packages:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Environment Variables
Create a `.env` file in the root directory and add your API keys:
```env
GROQ_API_KEY="your_groq_api_key"
HUGGINGFACEHUB_API_TOKEN="your_huggingface_token"
```

### 5. Run the Application
```bash
streamlit run app/app.py
```
The app will be accessible at `http://localhost:8501`.

## ☁️ Cloud Deployment (GCP & Kubernetes)

The application is designed to be deployed on a Google Cloud VM running Ubuntu 24.04 LTS with Minikube. 

### Quick Deployment Steps:

1. **Build the Docker Image:**
   Point Docker to Minikube's internal daemon and build the image:
   ```bash
   eval $(minikube docker-env)
   docker build -t llmops-app:latest .
   ```

2. **Configure Kubernetes Secrets:**
   ```bash
   kubectl create secret generic llmops-secrets \
     --from-literal=GROQ_API_KEY="your_groq_key" \
     --from-literal=HUGGINGFACEHUB_API_TOKEN="your_hf_token"
   ```

3. **Deploy to Minikube:**
   ```bash
   kubectl apply -f llmops-k8s.yaml
   ```

4. **Expose the Service:**
   Open a terminal for tunneling:
   ```bash
   minikube tunnel
   ```
   Open another terminal to port-forward the Streamlit app:
   ```bash
   kubectl port-forward svc/llmops-service 8501:80 --address 0.0.0.0
   ```
   Access the app via your VM's external IP on port `8501`.

## 📊 Monitoring with Grafana Cloud

To enable observability for the Kubernetes cluster:
1. Create a `monitoring` namespace:
   ```bash
   kubectl create ns monitoring
   ```
2. Install Helm and connect to your Grafana Cloud account.
3. Deploy the Grafana Kubernetes Monitoring Helm chart using your custom `values.yaml` as described in `FULL_DOCUMENTATION.md`.
4. View metrics in real-time on your Grafana dashboard.

## 🤝 Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your enhancements.

## 📝 License
This project is licensed under the MIT License.
