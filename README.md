# School Dropout Prevention Multi-Agent System

## 1. The School Dropout Scenario (Problem Statement)
School dropout remains a critical issue in education systems worldwide, leading to reduced economic opportunities for individuals and significant societal costs. The primary challenge lies in **early detection**. Often, the signs of a student struggling—whether academic, emotional, or financial—appear in siloed systems (LMS, SIS, counseling logs) long before the student actually drops out. Human counselors are often overwhelmed by caseloads and cannot manually synthesize this disparate data for every student in real-time. By the time a student is flagged, it is often too late for effective intervention.

## 2. How Agents Can Help (Solution)
A Multi-Agent System (MAS) offers a powerful solution to this problem by mimicking a team of specialized experts working together 24/7.
*   **Holistic Analysis**: Unlike simple rule-based alerts, agents can synthesize unstructured data (counseling notes, survey sentiment) with structured data (grades, attendance).
*   **Specialization**: Different agents can adopt specific personas (e.g., a "Psychologist" agent vs. a "Financial Aid" agent), allowing for deep, nuanced analysis of specific risk factors.
*   **Scalability**: Agents can monitor thousands of students simultaneously, flagging only those who need human attention.
*   **Coordination**: An orchestrator agent can manage the workflow, ensuring that finding a risk leads to concrete actions (interventions, notifications) without human administrative overhead.

## 3. The School Dropout Multi-Agent System (Architecture)
This project implements a sophisticated multi-agent system using the **Google Agent Development Kit (ADK)**. It follows **Clean Architecture** principles to ensure modularity and testability.

### Architecture Diagram
```mermaid
graph TD
    User[User / System Trigger] -->|Prompt| Router[Router Agent (Orchestrator)]
    
    Router -->|1. New Analysis| Pipeline[Full Analysis Pipeline]
    Router -->|2. Summary Request| Summary[Final Summary Agent]
    
    subgraph "Full Analysis Pipeline (Sequential)"
        Pipeline --> Risk[Risk Prediction Agent]
        Risk -->|Save| DB[(Database)]
        Risk -->|Pass Data| Shared[Shared State Store]
        
        Shared --> Emo[Emotional & Behavioral Agent]
        Shared --> Acad[Academic Support Agent]
        Acad -->|Search Videos| YouTube[YouTube MCP Server]
        
        Shared --> Interv[Intervention Coordinator]
        Interv -->|Save| DB
        
        Shared --> Family[Family Engagement Agent]
        Family -->|Pass Data| Summary
    end
    
    Summary -->|Fetch Results| Shared
    Summary -->|Fallback (If Empty)| DB
    Summary -->|Final Report| Router
```

### Agent Roles & Functionality
The system is composed of a **Router Agent**, a **Sequential Pipeline**, and specialized **Sub-Agents**.

1.  **Dropout Prevention Orchestrator (Router)** (`orchestrator/agent.py`):
    *   **Role**: The intelligent router.
    *   **Functionality**: Decides whether to trigger a full analysis or provide a summary of past results.

2.  **Full Analysis Pipeline** (`orchestrator/pipeline.py`):
    *   **Role**: The workflow manager.
    *   **Functionality**: Executes the 6-step analysis process sequentially, ensuring data flows between agents via the Shared State.

3.  **Risk Prediction Agent** (`risk_prediction/agent.py`):
    *   **Role**: The data analyst.
    *   **Functionality**: Calculates risk scores based on grades, attendance, and financial data. Persists results to the database.

4.  **Emotional & Behavioral Agent** (`emotional/agent.py`):
    *   **Role**: The school psychologist.
    *   **Functionality**: Analyzes sentiment in counseling notes and surveys.

5.  **Academic Support Agent** (`academic_support/agent.py`):
    *   **Role**: The academic tutor.
    *   **Functionality**: Creates study plans and **searches for real YouTube video tutorials** using the YouTube MCP Server.

6.  **Intervention Coordinator Agent** (`intervention/agent.py`):
    *   **Role**: The case worker.
    *   **Functionality**: Creates and saves formal intervention records.

7.  **Family Engagement Agent** (`family/agent.py`):
    *   **Role**: The parent liaison.
    *   **Functionality**: Drafts empathetic communication for parents.

8.  **Final Summary Agent** (`summary/agent.py`):
    *   **Role**: The reporter.
    *   **Functionality**: Aggregates all agent results into a comprehensive markdown report.
    *   **Database Fallback**: If the shared state is empty (e.g., after a restart), it automatically retrieves historical data from the database.

## 4. Setup & Installation

### Prerequisites
*   Python 3.10 or higher
*   Node.js & npm (for MCP Server)
*   Google Cloud Project (Vertex AI) or Google AI Studio API Key
*   YouTube Data API v3 Key

### Installation
1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd school_dropout_agent
    ```

2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables**:
    Create a `.env` file or export variables:
    ```bash
    export GOOGLE_API_KEY="your-google-api-key"
    export YOUTUBE_API_KEY="your-youtube-api-key"
    ```

### Running the System
To verify the full end-to-end workflow, run the verification script:
```bash
python verify_orchestrator.py
```
This script tests:
1.  **Full Analysis**: Complete pipeline execution.
2.  **Summary Request**: Routing to the summary agent.
3.  **Database Fallback**: Retrieving history after clearing memory.

To verify the YouTube integration:
```bash
python verify_youtube_mcp.py
```

## 5. Key Features

### Shared State Management
Agents communicate via a singleton `SharedStateStore`. This allows them to pass detailed JSON data (like full study plans) to the next agent without cluttering the main conversation history with the user.

### Database Fallback
The system is resilient to restarts. If you ask for a summary of a student analyzed in a previous session, the `FinalSummaryAgent` detects the empty shared state and seamlessly retrieves the student's history from the SQLite database.

### MCP Integration (Model Context Protocol)
The system uses the **Model Context Protocol** to connect to external tools. The `AcademicSupportAgent` connects to a **YouTube MCP Server** to find real, relevant educational videos for students, rather than hallucinating links.

