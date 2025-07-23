# Sustainable AI: Carbon Aware Computing

## ⚙️ Project Overview

As demand for generative AI grows, so does its environmental cost. Training and serving generative AI models can be carbon-intensive, but these processes don't have to be environmentally costly. 

In this repo, we'll walk through how to build a practical framework for low-emission generative AI deployment in the cloud. With carbon awareness, developers can significantly reduce the environmental impact of AI models for a more sustainable future in AI.  
**This project’s carbon-aware workflow includes the following key steps:**

- **Analyze Historical Emissions**: Query Google Cloud Platform's carbon footprint data using BigQuery to understand past emissions patterns across services, projects, and regions  
- **Monitor Real-Time Carbon Intensity**: Access live electrical grid data via Electricity Maps API to identify the cleanest energy sources globally  
- **Optimize Training Deployment**: Automatically select cloud regions with the lowest carbon footprint for ML model training using Google Cloud Vertex AI  
- **Track Environmental Impact**: Measure and compare carbon savings across different deployment strategies

The workflow integrates real-time electricity grid data from the [Electricity Maps API](https://www.electricitymaps.com/api) and scalable cloud services from [Google Cloud Platform (GCP)](https://cloud.google.com/) to help developers make smarter, lower-emission decisions about where and when to run machine learning workloads. By combining live carbon intensity metrics with tools like [BigQuery](https://cloud.google.com/bigquery), [Vertex AI](https://cloud.google.com/vertex-ai), and [Cloud Storage](https://cloud.google.com/storage), **developers can**:

- **Reduce Carbon Footprint**: Achieve up to 50-80% reduction in training emissions by selecting optimal regions and timing
- **Maintain Performance**: No compromise on model quality or training speed
- **Enable Sustainable Scaling**: Build environmentally conscious practices into ML workflows from the start
- **Support Climate Goals**: Contribute to global decarbonization efforts through intelligent computing choices

## ⚙️ Electricity Maps 

**Electricity Maps** provides live and historical data on carbon emissions for electrical grids worldwide. The [Electricity Maps API](https://api.electricitymaps.com) enables developers to integrate regional carbon intensity directly into software workflows, making it easier to make data-informed decisions about when and where to run compute-intensive operations. By aggregating data from grid operators and energy providers, it breaks down the energy mix—showing how much comes from low-carbon sources like wind, solar, or hydro versus fossil fuels like coal or natural gas. 

| Key Features |
|------------------------------|
| Regional carbon intensity tracking with both live and historical data |
| Detailed energy mix breakdown by source (e.g. wind, solar, coal, nuclear) |
| RESTful API for seamless integration into data pipelines and cloud workflows |
| Supports real-time decision-making for energy-aware scheduling and infrastructure |
| Global coverage with granularity down to individual grid zones in many regions |

> # 🛠️ Learn More
> - [Electricity Maps Docs](https://www.electricitymaps.com/api)  
> - [Electricity Maps API Reference](https://api.electricitymaps.com)  
> - [API Quickstart Guide](https://www.electricitymaps.com/api#getting-started)  
> - [Authentication & Tokens](https://www.electricitymaps.com/api#authentication)  
> - [Data Fields & Parameters](https://www.electricitymaps.com/api#response-fields)  

## ⚙️ Google Cloud

The [Google Cloud Platform (GCP)](https://cloud.google.com/) is a comprehensive cloud computing platform that provides global network infrastructure, data analytics, artificial intelligence, and machine learning service. From **virtual machines, container orchestration with Kubernetes, serverless computing, and fully managed databases,** Google Cloud enables businesses to **build, deploy, and manage applications efficiently in the cloud**. It also offers advanced tools for data warehousing, real-time analytics, and AI model training and inference. Google Cloud is widely recognized for its sustainability efforts and leadership in clean energy-powered data centers.

| Key Features |
|---------------------------------------------|
| Scalable compute infrastructure with global availability zones |
| Managed services for AI/ML model training, deployment, and monitoring |
| Native support for Kubernetes and containerized workloads |
| Built-in tools for real-time analytics and petabyte-scale querying |
| Integration with sustainability tools like the Google Cloud Carbon Footprint |

> # 🛠️ Learn More
> - [Google Cloud Documentation Hub](https://cloud.google.com/docs)
> - [Google Cloud Console](https://console.cloud.google.com/)  
> - [Google Cloud SDK (gcloud) Documentation](https://cloud.google.com/sdk/docs)  
> - [Google Cloud Free Tier Overview](https://cloud.google.com/free) 
> - [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator)

## ⚙️ Carbon Aware Workflows

### 1. Carbon Intensity Across Regions  
[`explore_carbon_intensity.ipynb`](../explore_carbon_intensity.ipynb)  
Explore global carbon intensity using the [Electricity Maps API](https://api.electricitymaps.com). **Monitor emissions in real-time**, **compare grid regions**, and **optimize workload location decisions** based on geographic and temporal differences in energy sourcing.

### 2. Google Cloud Footprint  
[`calculate_google_cloud_footprint.ipynb`](../calculate_google_cloud_footprint.ipynb)  
Use [BigQuery](https://cloud.google.com/bigquery) to examine project-level emissions on GCP. **Analyze Scope 1, 2, and 3 emissions**, broken down by service, project, and time. Understand how cloud resource consumption translates to measurable environmental impact.

### 3. Low Carbon Training with Live Data  
[`train_models_with_energy_data.ipynb`](../train_models_with_energy_data.ipynb)  
Automatically identify GCP regions with the lowest carbon footprint using real-time API data. **Deploy training pipelines dynamically** to regions with the cleanest energy at runtime. **Quantify and compare CO₂e impact** across region choices.

### 4. Training in Low Carbon Regions  
[`train_models_with_carbon_data.ipynb`](../train_models_with_carbon_data.ipynb)  
Train a neural network locally, then migrate to [Vertex AI](https://cloud.google.com/vertex-ai) in a pre-selected low-carbon region. **Showcases how to reduce emissions without changing the model architecture** by modifying deployment strategy.

## ⚙️ Dependencies  
**Dependencies are listed in [`requirements.txt`](./requirements.txt).**

| **Package**                | **Function / Use Case**                                       | **Link**                                                                 |
|---------------------------|---------------------------------------------------------------|--------------------------------------------------------------------------|
| **`tensorflow`**          | Neural network creation and training                          | [tensorflow.org](https://www.tensorflow.org/install)                     |
| **`scikit-learn`**        | Dataset creation and transformations                          | [scikit-learn.org](https://scikit-learn.org/stable/install.html)        |
| **`pandas`**              | Tabular data analysis and emission breakdowns                 | [pandas.pydata.org](https://pandas.pydata.org/docs/getting_started.html)|
| **`matplotlib`**          | Visualizing emission comparisons and results                  | [matplotlib.org](https://matplotlib.org/stable/users/installing.html)   |
| **`numpy`**               | Numerical operations and array handling                       | [numpy.org](https://numpy.org/install/)                                  |
| **`requests`**            | API communication (e.g., with Electricity Maps)               | [requests.readthedocs.io](https://requests.readthedocs.io/en/latest/)   |
| **`google-cloud-aiplatform`** | Train and deploy models on Vertex AI                     | [cloud.google.com](https://cloud.google.com/python/docs/aiplatform)     |
| **`google-cloud-storage`**    | Manage cloud-based artifacts and checkpoints            | [cloud.google.com](https://cloud.google.com/python/docs/storage)        |
| **`google-cloud-bigquery`**   | Analyze GCP usage and emissions via SQL                | [cloud.google.com](https://cloud.google.com/python/docs/bigquery)       |
| **`google-auth`**         | Authentication for Google Cloud APIs                          | [cloud.google.com](https://cloud.google.com/python/docs/authentication) |
| **`jupyter`**             | Jupyter notebook interface                                    | [jupyter.org](https://jupyter.org/install)                              |
| **`notebook`**            | Web-based notebook server                                     | [jupyter.org](https://jupyter.org/install)                              |

## ⚙️ Google Cloud Account Setup

To run this project using Google Cloud infrastructure (Vertex AI, BigQuery, and Cloud Storage), follow the setup steps outlined in the [`google_cloud_setup.ipynb`](../google_cloud_setup.ipynb) notebook.

### Prerequisites
**Before running the main notebooks, ensure the following:**
- You have a Google Cloud account with billing enabled.
- You have created or selected a [Google Cloud Project](https://console.cloud.google.com/).
- You have enabled the necessary APIs:
  - [Vertex AI API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com)
  - [BigQuery API](https://console.cloud.google.com/flows/enableapi?apiid=bigquery.googleapis.com)
  - [Cloud Storage API](https://console.cloud.google.com/flows/enableapi?apiid=storage.googleapis.com)
> 💡 You can start with [Google Cloud Free Tier](https://cloud.google.com/free/docs/gcp-free-tier), which includes a 90-day $300 credit.

### Authentication

**Run the setup notebook locally to configure authentication. Options include:**
- Authenticating via `gcloud auth login`
- Using a downloaded service account key (`.json`)
- Verifying permissions and access to the chosen project

For detailed instructions, refer to [`google_cloud_setup.ipynb`](../google_cloud_setup.ipynb).

> 📚 Learn more about managing GCP projects [here](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

## ⚙️ Getting Started 

### 1. Clone the Repository
```bash
git clone https://github.com/milanimcgraw/Carbon-Aware-Computing-for-Gen-AI.git
cd Carbon-Aware-Computing-for-Gen-AI
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Your Environment
Create a `.env` file in the root of your project directory and define the following keys:
```ini
SERVICE_ACCOUNT_KEY=<your_base64_encoded_service_account_json>
PROJECT_ID=<your_google_cloud_project_id>
ELECTRICITY_MAPS_API_KEY=<your_electricity_maps_api_key>
```

### 4. Run Google Cloud Setup Notebook
Before running any training or analysis notebooks, run the setup notebook.

### 5. Open the `google_cloud_setup.ipynb` notebook in Jupyter, VS Code, or Colab

> **Note:** Ensure `helper.py` and/or `task.py` is available in the root or referenced directory.

## ⚙️ License
This project is released under the MIT license. 

---
> ## 📌 Credits
> 📦 This project builds on concepts and starter code introduced in the [Carbon Aware Computing for GenAI Developers](https://learn.deeplearning.ai/courses/carbon-aware-computing-for-genai-developers) course offered through [DeepLearning.AI](https://www.deeplearning.ai/short-courses/), in collaboration with [Google Cloud](https://cloud.google.com/) and taught by [Nikita Namjoshi](https://nikitanamjoshi.substack.com/), Developer Advocate at Google Cloud and Google Fellow on the Permafrost Discovery Gateway.  
> While the original instructional materials provided foundational examples, this implementation has been customized and extended.
