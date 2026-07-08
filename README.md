# Multi-Agent MCP Orchestration with Model Context Protocol

A production-inspired multi-agent orchestration system built using the **Model Context Protocol (MCP)**. The project demonstrates how multiple AI agents can share a common MCP client to access centralized tools exposed by an MCP server.

The implementation follows a modular architecture where the **Supervisor Agent** routes incoming requests to specialized agents, while the MCP Server owns the actual tool implementations. This separation of concerns mirrors the architecture used in modern AI agent frameworks.

---

## Features

- Multi-Agent Orchestration
- Shared MCP Client
- MCP Server with Multiple Tools
- MCP Resource Support
- Supervisor Pattern
- Async Communication
- Unit Testing with Pytest
- Structured Logging

---

# Architecture

```text
                    User
                      │
                      ▼
              Supervisor Agent
                      │
             Routes Request
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
 Summary Agent               Keyword Agent
        │                           │
        └─────────────┬─────────────┘
                      ▼
               Shared MCP Client
                      │
                      ▼
                 MCP Server
          ┌───────────┴───────────┐
          ▼                       ▼
     summarize()             keywords()
                      │
                      ▼
                  tools.py
```

---

## Components

### Supervisor Agent
- Receives incoming tasks.
- Selects the appropriate specialized agent.
- Manages the shared MCP client lifecycle.
- Coordinates overall orchestration.

### Summary Agent
Delegates text summarization requests to the MCP Server through the shared MCP Client.

### Keyword Agent
Delegates keyword extraction requests to the MCP Server through the shared MCP Client.

### MCP Client
Provides a reusable interface for:
- Connecting to the MCP Server
- Reading resources
- Invoking tools
- Closing the connection

### MCP Server
Exposes:
- **Resource**
  - `document://demo`
- **Tools**
  - `summarize()`
  - `keywords()`

Business logic is implemented in `tools.py`, while `server.py` only exposes MCP resources and tools.

---

## Running the Project

### Start the MCP Server

```bash
python -m mcp_server.server
```

### Run the MCP Client

```bash
python -m mcp_client.client
```

---

## Running Tests

Execute all tests using:

```bash
python -m pytest tests
```

Current test results:

```
11 passed
```

---

## Technologies

- Python 3.11
- Model Context Protocol (MCP)
- FastMCP
- AsyncIO
- Pytest
- Pydantic

---

## Design Principles

- Separation of Concerns
- Supervisor–Worker (Agent) Pattern
- Shared Resource Management
- Dependency Injection
- Modular Architecture
- Reusable MCP Client
- Centralized Tool Execution

---

## Future Improvements

- Persistent MCP Client lifecycle
- Additional specialized agents
- External APIs and databases as MCP tools
- LLM-powered summarization and keyword extraction
- Multi-agent collaboration workflows