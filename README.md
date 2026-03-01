# Realtime Media Annotation

A real-time collaborative backend for timestamp-based media annotation.

## Tech
- FastAPI (async)
- PostgreSQL
- Redis (caching + pub/sub)
- WebSockets
- Docker

## Why
Traditional REST APIs require polling for updates. This project explores low latency collaboration using WebSockets and scalable event propagation (Redis pub/sub).

## Status
In progress —> building core APIs, then caching and real-time sync.
