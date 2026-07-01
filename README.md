# MLOps + Data Engineering Knowledge Platform

## Overview
A Retrieval-Augmented Generation (RAG) system that ingests real-world MLOps and Data Engineering documentation and enables intelligent question answering using LLMs.

## Tech Stack
- Python
- FastAPI
- Qdrant (Vector DB)
- Qwen (LLM via Ollama)
- Docker

## Architecture
- ETL Pipeline (Data ingestion & processing)
- Embeddings + Vector Search
- RAG-based LLM answering system
- REST API via FastAPI
- Containerized deployment using Docker

## Run Locally
```bash
docker compose up --build