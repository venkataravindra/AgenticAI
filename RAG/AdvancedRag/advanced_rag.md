# 🏗️ **Advanced RAG System Architecture Analysis**

## 📊 **High-Level System Architecture**

```mermaid
graph TB
    subgraph "Client Layer"
        A[User Interface] --> B[FastAPI Endpoints]
    end
    
    subgraph "API Layer"
        B --> C[Upload Endpoint /upload]
        B --> D[Query Endpoint /ask]
        B --> E[Root Endpoint /]
    end
    
    subgraph "Document Processing Pipeline"
        C --> F[File Validation]
        F --> G[Document Loading]
        G --> H[Text Splitting]
        H --> I[Embedding Generation]
        I --> J[FAISS Vector Store]
    end
    
    subgraph "Query Processing Pipeline"
        D --> K[Query Expansion]
        K --> L[Multi-Query Retrieval]
        L --> M[Document Deduplication]
        M --> N[Cross-Encoder Re-ranking]
        N --> O[Context Building]
        O --> P[Claude Answer Generation]
    end
    
    subgraph "Storage Layer"
        Q[Local File System]
        R[FAISS Index Files]
        J --> R
        G --> Q
    end
    
    subgraph "External Services"
        S[Anthropic Claude API]
        T[HuggingFace Models]
        P --> S
        I --> T
        N --> T
    end
```

## 🔄 **Detailed Flow Diagrams**

### **1. Document Upload Flow**

```mermaid
sequenceDiagram
    participant U as User
    participant API as FastAPI
    participant V as Validator
    participant L as Document Loader
    participant S as Text Splitter
    participant E as Embeddings
    participant F as FAISS Store
    participant D as Disk Storage

    U->>API: POST /upload (PDF/TXT file)
    API->>V: Validate file extension
    
    alt Valid File
        V->>D: Save file to data/ directory
        API->>L: Load document content
        
        alt PDF File
            L->>L: Use PyPDFLoader
        else TXT File
            L->>L: Use text file reader
        end
        
        L->>S: Split into chunks (800 chars, 150 overlap)
        S->>E: Generate embeddings (HuggingFace)
        
        alt First Document
            E->>F: Create new FAISS index
        else Existing Documents
            E->>F: Add to existing FAISS index
        end
        
        F->>D: Save FAISS index to disk
        API->>U: Return success response
    else Invalid File
        V->>API: Raise HTTPException
        API->>U: Return error (400)
    end
```

### **2. Query Processing Flow**

```mermaid
sequenceDiagram
    participant U as User
    participant API as FastAPI
    participant QE as Query Expander
    participant C as Claude API
    participant R as Retriever
    participant F as FAISS
    participant RE as Re-ranker
    participant CB as Context Builder
    participant AG as Answer Generator

    U->>API: POST /ask {"question": "..."}
    API->>QE: Expand original query
    QE->>C: Generate 3 alternative queries
    C->>QE: Return expanded queries
    
    QE->>R: Multi-query retrieval
    loop For each query
        R->>F: Similarity search (k=5)
        F->>R: Return candidate documents
    end
    
    R->>R: Deduplicate documents
    R->>RE: Re-rank candidates
    RE->>RE: Calculate relevance scores
    RE->>CB: Top 5 documents + scores
    
    CB->>CB: Build context string
    CB->>AG: Context + original question
    AG->>C: Generate final answer
    C->>AG: Return grounded answer
    
    AG->>API: Complete response
    API->>U: Return answer + metadata
```

## 🏛️ **Component Architecture**

### **Core Components Breakdown**

```mermaid
graph LR
    subgraph "Document Processing Components"
        A[PyPDFLoader] --> B[RecursiveCharacterTextSplitter]
        B --> C[HuggingFaceEmbeddings]
        C --> D[FAISS VectorStore]
    end
    
    subgraph "Query Processing Components"
        E[Query Expander] --> F[Multi-Query Retriever]
        F --> G[CrossEncoder Re-ranker]
        G --> H[Context Builder]
        H --> I[Claude Answer Generator]
    end
    
    subgraph "External Dependencies"
        J[Anthropic Claude API]
        K[HuggingFace Models]
        L[Sentence Transformers]
    end
    
    E --> J
    I --> J
    C --> K
    G --> L
```

## 📋 **Detailed Code Analysis**

### **1. Key Configuration & Setup**

```python
# Core Models and Services
llm = ChatAnthropic(model="claude-sonnet-4-6")  # Main LLM
embeddings = HuggingFaceEmbeddings(model="all-MiniLM-L6-v2")  # Embeddings
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")  # Re-ranking
vector_store = None  # FAISS (initialized dynamically)
```

### **2. Document Processing Pipeline**

```mermaid
flowchart TD
    A[Upload File] --> B{File Type?}
    B -->|PDF| C[PyPDFLoader]
    B -->|TXT| D[Text File Reader]
    C --> E[Add Metadata]
    D --> E
    E --> F[RecursiveCharacterTextSplitter<br/>chunk_size=800<br/>overlap=150]
    F --> G[Add Chunk IDs]
    G --> H{FAISS Exists?}
    H -->|No| I[Create New FAISS Index]
    H -->|Yes| J[Add to Existing Index]
    I --> K[Save to Disk]
    J --> K
```

### **3. Advanced Query Processing**

```mermaid
flowchart TD
    A[User Question] --> B[Query Expansion via Claude]
    B --> C[Generate 3 Alternative Queries]
    C --> D[Multi-Query Retrieval]
    
    subgraph "Retrieval Process"
        D --> E[Query 1 → FAISS Search]
        D --> F[Query 2 → FAISS Search]
        D --> G[Query 3 → FAISS Search]
        D --> H[Query 4 → FAISS Search]
    end
    
    E --> I[Combine Results]
    F --> I
    G --> I
    H --> I
    
    I --> J[Remove Duplicates by source_chunk_id]
    J --> K[Cross-Encoder Re-ranking]
    K --> L[Top 5 Documents]
    L --> M[Build Context String]
    M --> N[Claude Final Answer]
```

## 🔧 **Technical Implementation Details**

### **FAISS Vector Store Management**

```python
# Dynamic FAISS initialization
if vector_store is None:
    # First document: Create new index
    vector_store = FAISS.from_documents(documents=chunks, embedding=embeddings)
else:
    # Subsequent documents: Add to existing index
    vector_store.add_documents(documents=chunks)

# Persistence
vector_store.save_local(folder_path=FAISS_INDEX_PATH)
```

### **Query Expansion Strategy**

```python
def expand_query(question: str) -> List[str]:
    """
    Original: "What is Advanced RAG?"
    Expanded: [
        "What is Advanced RAG?",
        "Advanced Retrieval Augmented Generation",
        "Advanced RAG architecture", 
        "Advanced RAG retrieval techniques"
    ]
    """
```

### **Multi-Query Retrieval with Deduplication**

```python
def retrieve_candidates(queries: List[str], k: int = 5):
    """
    For each query:
    1. Search FAISS (k=5 results each)
    2. Combine all results
    3. Remove duplicates by unique key: f"{source}_{chunk_id}"
    """
```

## 📊 **Data Flow Architecture**

### **Document Ingestion Data Flow**

```mermaid
graph TD
    A[Raw Document] --> B[Document Object]
    B --> C[Text Chunks]
    C --> D[Embeddings Vector]
    D --> E[FAISS Index]
    E --> F[Disk Storage]
    
    subgraph "Metadata Flow"
        G[Source Filename] --> H[Chunk ID]
        H --> I[Page Number]
        I --> J[Combined Metadata]
    end
    
    C --> J
    J --> E
```

### **Query Response Data Flow**

```mermaid
graph TD
    A[User Question] --> B[Expanded Queries Array]
    B --> C[Candidate Documents]
    C --> D[Ranked Documents + Scores]
    D --> E[Context String]
    E --> F[Claude Response]
    
    subgraph "Response Object"
        F --> G[Final Answer]
        B --> H[Generated Queries]
        C --> I[Candidate Count]
        D --> J[Selected Documents]
        D --> K[Source Information]
    end
```

## 🎯 **API Endpoint Architecture**

### **Endpoint Structure**

```mermaid
graph TB
    subgraph "FastAPI Application"
        A[Root Endpoint /]
        B[Upload Endpoint /upload]
        C[Query Endpoint /ask]
    end
    
    subgraph "Request/Response Models"
        D[UploadFile]
        E[QuestionRequest]
        F[Upload Response]
        G[Query Response]
    end
    
    subgraph "Business Logic"
        H[ingest_document]
        I[ask_question]
    end
    
    B --> D
    C --> E
    B --> F
    C --> G
    B --> H
    C --> I
```

## 🔍 **Advanced Features Analysis**

### **1. Cross-Encoder Re-ranking**

```mermaid
flowchart LR
    A[Question + Document Pairs] --> B[CrossEncoder Model]
    B --> C[Relevance Scores]
    C --> D[Sort by Score]
    D --> E[Top N Documents]
```

### **2. Context Building Strategy**

```python
# Context format for each document
"""
[Context 1]
Source: document.pdf, page 3
Content: <actual content>

[Context 2] 
Source: guide.txt
Content: <actual content>
"""
```

### **3. Error Handling & Validation**

```mermaid
graph TD
    A[Request] --> B{File Extension Valid?}
    B -->|No| C[HTTP 400 Error]
    B -->|Yes| D{Question Empty?}
    D -->|Yes| E[HTTP 400 Error]
    D -->|No| F{FAISS Index Exists?}
    F -->|No| G[No Documents Found]
    F -->|Yes| H[Process Query]
```

## 🚀 **Performance Considerations**

### **Optimization Points**

1. **FAISS Index**: Fast similarity search (O(log n))
2. **Chunk Overlap**: Ensures context continuity
3. **Re-ranking**: Improves relevance quality
4. **Query Expansion**: Increases recall
5. **Deduplication**: Reduces redundancy

### **Scalability Architecture**

```mermaid
graph TB
    subgraph "Current Architecture"
        A[Single FastAPI Instance]
        B[Local FAISS Index]
        C[Local File Storage]
    end
    
    subgraph "Scalable Architecture"
        D[Load Balancer]
        E[Multiple FastAPI Instances]
        F[Shared Vector Database]
        G[Distributed File Storage]
        H[Redis Cache]
    end
```

This architecture provides a robust, production-ready RAG system with advanced features like query expansion, multi-query retrieval, and cross-encoder re-ranking, all orchestrated through a clean FastAPI interface.
