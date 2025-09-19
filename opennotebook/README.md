# OpenNotebook

A Google NotebookLM-style AI research assistant. See `../Project Description` for full product brief.

## Repo Structure

- `frontend/` — React SPA notebook UI
- `backend/` — FastAPI backend
  - `api/` — API endpoints
  - `workers/` — background jobs
  - `ingest/` — document parsing
  - `agents/` — agent orchestration
- `services/` — microservices (vectorstore, embeddings, TTS, slidegen)
- `infra/` — infrastructure (terraform, docker-compose)
- `docs/` — architecture and agent patterns

## Quickstart

1. Install Python dependencies in `backend/`
2. Run FastAPI server: `uvicorn api.main:app --reload`
3. Start frontend (see `frontend/`)

## References
- See `Project Description` for architecture, roadmap, and implementation notes.