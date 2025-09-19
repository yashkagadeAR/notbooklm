# Agent Patterns in OpenNotebook

This document outlines agentic workflows, tool interfaces, and orchestration strategies for OpenNotebook.

## Agentic Workflows
- Researcher agent: Q&A, evidence gathering, summarization
- Slide-builder agent: Generates slide decks from document chunks

## Tool Interfaces
- file_search_tool(query, notebook_id)
- web_search_tool(query, max_results)
- slide_gen_tool(document_chunks, template)

## Orchestration
Agents are orchestrated using the OpenAI Agents SDK, with context built from user queries and retrieved notebook chunks.