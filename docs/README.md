# 🧠 Self-Evolving Agent Memory System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Ollama](https://img.shields.io/badge/Ollama-0.1.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**An AI assistant that learns from mistakes using RAG, vector databases, and self-evolution.**

</div>

---

## 📌 Overview

The **Self-Evolving Agent Memory System** is a Generative AI application that combines **long-term memory, Retrieval-Augmented Generation (RAG), vector databases, and self-evolution** to create an AI assistant that can learn from previous interactions.

Unlike a basic chatbot, the system can:

* 🧠 Remember previous conversations
* 🔎 Retrieve relevant memories using semantic search
* 🤖 Generate responses using a local LLM
* 📚 Store structured and vector-based memories
* ⚡ Detect and learn from mistakes
* 🔄 Improve future responses using learned information
* 📊 Track memory and evolution statistics in real time

The project is designed as a practical implementation of a **self-improving AI agent architecture**.

---

## ✨ Key Features

| Feature                   | Description                                                |
| ------------------------- | ---------------------------------------------------------- |
| 🧠 **Hybrid Memory**      | Uses SQLite and ChromaDB for persistent memory             |
| 🔎 **Semantic Retrieval** | Retrieves relevant past conversations using embeddings     |
| 📚 **RAG Pipeline**       | Provides previous knowledge as context to the LLM          |
| ⚡ **Self-Evolution**      | Learns from incorrect or failed responses                  |
| 🤖 **Local LLM**          | Uses Ollama for local AI inference                         |
| 🎨 **Premium UI**         | Professional Streamlit interface with real-time statistics |
| 📊 **Real-Time Metrics**  | Tracks memories, vectors, and evolution events             |
| 🔄 **Audit Trail**        | Maintains a history of learning and evolution events       |
| 🔐 **Local Processing**   | Core AI processing can run locally without external APIs   |

---

## 🛠️ Tech Stack

| Category                   | Technology                 |
| -------------------------- | -------------------------- |
| **Language**               | Python 3.10+               |
| **Frontend / UI**          | Streamlit                  |
| **LLM**                    | Ollama                     |
| **LLM Model**              | llama3.2:1b                |
| **Embeddings**             | nomic-embed-text           |
| **Vector Database**        | ChromaDB                   |
| **Structured Database**    | SQLite                     |
| **Agent Framework**        | LangGraph                  |
| **Testing**                | Pytest                     |
| **Environment Management** | Python Virtual Environment |

---

## 🧠 System Architecture

The system follows a continuous **Retrieve → Generate → Store → Evaluate → Evolve** workflow.

```text
                 ┌───────────────────┐
                 │       User        │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │    AI Agent       │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Memory Retrieval  │
                 │    ChromaDB       │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │   RAG Context     │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │   Ollama LLM      │
                 │    llama3.2:1b    │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │     Response      │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │  Memory Storage   │
                 ├───────────────────┤
                 │ SQLite + ChromaDB │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Self-Evolution    │
                 │     Engine        │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Learned Knowledge │
                 └───────────────────┘
```

---

## 🔄 How It Works

### 1. User Query

The user enters a question or instruction through the Streamlit interface.

### 2. Memory Retrieval

The system searches previous conversations stored in **ChromaDB** using semantic similarity.

### 3. Context Generation

Relevant memories are retrieved and added to the current prompt as contextual information.

### 4. Response Generation

The **Ollama LLM** generates a response using the current query and retrieved memory.

### 5. Memory Storage

The interaction is stored in:

* **SQLite** for structured information
* **ChromaDB** for vector-based semantic retrieval

### 6. Self-Evolution

When an incorrect or failed response is identified, the evolution engine analyzes the failure and creates a learning record.

### 7. Future Improvement

The learned information becomes part of the system's memory and can be retrieved during future conversations.

### 8. Statistics Update

The dashboard updates system metrics such as:

* Total Memories
* Vector Memories
* Evolution Events

---

## 🧠 Hybrid Memory System

The project uses two complementary storage systems.

### SQLite

SQLite stores structured information such as:

* Conversations
* User queries
* AI responses
* Timestamps
* Learning events
* Evolution records

### ChromaDB

ChromaDB stores vector embeddings that allow the system to perform **semantic similarity search**.

This means the system can find conceptually related conversations even when the exact words are different.

### Why Hybrid Memory?

Using both databases provides the advantages of:

**SQLite**

* Structured storage
* Easy querying
* Reliable persistence

**ChromaDB**

* Semantic search
* Vector similarity
* Efficient contextual retrieval

---

## 🔎 Retrieval-Augmented Generation

The system implements **RAG (Retrieval-Augmented Generation)** to improve response quality.

Instead of relying only on the LLM's pretrained knowledge, the system:

```text
User Query
    ↓
Generate Embedding
    ↓
Search ChromaDB
    ↓
Retrieve Relevant Memories
    ↓
Build Context
    ↓
Send Context + Query to LLM
    ↓
Generate Response
```

This allows the agent to use information from previous interactions when generating new responses.

---

## ⚡ Self-Evolution Engine

The **Self-Evolution Engine** is one of the main components of the project.

When a response is identified as incorrect or unsuccessful, the system can:

1. Detect the failure
2. Analyze the problem
3. Identify what went wrong
4. Generate a learning record
5. Store the lesson
6. Make the information available for future retrieval

This creates a feedback loop:

```text
Interaction
     ↓
Response
     ↓
Evaluation
     ↓
Mistake Detected
     ↓
Failure Analysis
     ↓
Learning
     ↓
Memory Storage
     ↓
Future Retrieval
     ↓
Improved Response
```

---

## 📊 System Metrics

The dashboard provides real-time information about the system.

| Metric               | Description                                  |
| -------------------- | -------------------------------------------- |
| **Total Memories**   | Total number of stored conversations         |
| **Vector Memories**  | Number of memories stored as embeddings      |
| **Evolution Events** | Number of recorded learning/evolution events |

These metrics make it easier to monitor how the agent's memory and learning system grows over time.

---

## 🎨 User Interface

The application uses **Streamlit** to provide a professional interactive interface.

The interface includes:

* 💬 AI conversation interface
* 🧠 Memory statistics
* 📊 System metrics
* ⚡ Evolution information
* 🔄 Learning history
* ✨ Clean and responsive design

The UI is designed with a modern light theme and premium visual elements.

---

## 📂 Project Structure

```text
self-evolving-agent-memory/
│
├── app/
│   ├── main.py          # Application entry point
│   ├── agent.py         # Core AI agent
│   ├── memory.py        # Memory storage and retrieval
│   ├── evolution.py     # Self-evolution engine
│   └── ui.py            # Streamlit user interface
│
├── tools/
│   └── functions.py     # Agent tools and functions
│
├── data/
│   └──                 # Databases and generated data
│
├── tests/
│   └──                 # Unit tests
│
├── requirements.txt     # Python dependencies
├── .env.example        # Environment configuration template
└── README.md            # Project documentation
```

---

## 🚀 Quick Start

### Prerequisites

Make sure the following are installed:

* Python 3.10 or higher
* Ollama
* Git

### 1. Clone the Repository

```bash
git clone https://github.com/krishnapopat130324-art/self-evolving-agent-memory.git
cd self-evolving-agent-memory
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Ollama Models

Install Ollama and pull the required models:

```bash
ollama pull llama3.2:1b
ollama pull nomic-embed-text
```

### 5. Configure Environment Variables

Create the `.env` file from the example configuration:

#### Windows

```bash
copy .env.example .env
```

#### Linux / macOS

```bash
cp .env.example .env
```

Update the `.env` file if any configuration changes are required.

### 6. Run the Application

```bash
streamlit run app/main.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

## 🧪 Testing

Run the project's tests using:

```bash
python -m pytest tests/
```

To check the number of stored memories:

```bash
python -c "import sqlite3; conn=sqlite3.connect('data/memory.db'); print('Memories:', conn.cursor().execute('SELECT COUNT(*) FROM memories').fetchone()[0])"
```

---

## 📈 Use Cases

### 🤖 Personal AI Assistant

Creates an assistant that remembers previous interactions and user-specific information.

### 🎧 Customer Support

Can maintain conversation history and use previous cases to improve future responses.

### 🏢 Knowledge Management

Can build a searchable institutional memory from previous interactions and stored knowledge.

### 🎓 Education

Can remember previous questions and adapt future explanations based on past interactions.

### 🧑‍💻 Developer Assistant

Can store previous debugging experiences and retrieve similar solutions when related problems occur.

---


## 📞 Author

**Krishna Popat**

---

<div align="center">

⭐ **If you found this project useful, consider giving it a star!** ⭐

**Built with Python • Streamlit • Ollama • ChromaDB • SQLite • LangGraph**

</div>
