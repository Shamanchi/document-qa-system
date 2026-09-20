# Document QA System

[![CI](https://github.com/Shamanchi/document-qa-system/actions/workflows/ci.yml/badge.svg)](https://github.com/Shamanchi/document-qa-system/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://hub.docker.com/r/shamanchi/document-qa-system)
[![License: Shamanchi](https://img.shields.io/badge/License-Shamanchi-green.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/downloads/)

**Система вопросов и ответов по документам** — RAG над загруженными PDF/DOCX/TXT: индексация, семантический поиск, генерация ответов с цитатами.

> **Источник темы**: `Hands-On-AI-Engineering / P-120 (documentation_qna_agent), P-125 (grounded_document_agent)` → портфолио `document-qa-system`

---

## 🎯 Задача

- Загрузка и парсинг документов (PDF, DOCX, TXT, MD)
- Чанкинг с перекрытием, эмбеддинги (bge-m3 / e5)
- Векторный поиск (pgvector / Qdrant) + реранкинг
- Ответы на вопросы с цитированием источников (страницы, чанки)
- Мультиязычность, API для интеграции

---

## 🏗 Архитектура

```mermaid
flowchart TD
    A[Загрузка документа] --> B[Парсер (PyMuPDF / python-docx)]
    B --> C[Чанкинг + Эмбеддинги]
    C --> D[Векторная БД (pgvector/Qdrant)]
    D --> E[Вопрос пользователя]
    E --> F[Эмбеддинг вопроса]
    F --> G[Поиск топ-K чанков]
    G --> H[Реранкинг (cross-encoder)]
    H --> I[LLM генерация ответа + цитаты]
    I --> J[Ответ + источники]
```

**Слои:**
- `api/` — `/documents` (upload, list, delete), `/qa` (ask), `/search`
- `services/` — `parser`, `chunker`, `embedder`, `vector_store`, `retriever`, `reranker`, `generator`
- `core/` — `config`, `logging`, `exceptions`, `metrics`

---

## 🚀 Quickstart

```bash
git clone https://github.com/Shamanchi/document-qa-system.git
cd document-qa-system
cp .env.example .env
# Добавить OPENAI_API_KEY, DATABASE_URL

pip install -r requirements.txt
uvicorn app.main:app --reload

# Docker
docker compose up --build
```

---

## 📦 API Endpoints

| Метод | Путь | Описание |
|-------|------|----------|
| `POST` | `/api/v1/documents` | Загрузить документ |
| `GET` | `/api/v1/documents` | Список документов |
| `DELETE` | `/api/v1/documents/{id}` | Удалить документ |
| `POST` | `/api/v1/qa` | Задать вопрос по документам |
| `POST` | `/api/v1/search` | Семантический поиск чанков |
| `GET` | `/api/v1/health` | Health-check |

---

## ⚙️ Конфигурация (`.env`)

| Переменная | Описание | По умолчанию |
|------------|----------|--------------|
| `OPENAI_API_KEY` | Ключ OpenAI | — |
| `OPENAI_EMBEDDING_MODEL` | Модель эмбеддингов | `text-embedding-3-small` |
| `OPENAI_CHAT_MODEL` | Модель чата | `gpt-4o-mini` |
| `DATABASE_URL` | PostgreSQL + pgvector | `sqlite:///./data.db` |
| `VECTOR_STORE` | pgvector / qdrant | `pgvector` |
| `CHUNK_SIZE` | Размер чанка | `512` |
| `CHUNK_OVERLAP` | Перекрытие чанков | `50` |
| `TOP_K` | Чанков для ретрива | `10` |
| `RERANK_TOP_K` | После реранкинга | `5` |

---

## 🧪 Тесты

```bash
pytest tests/unit -v
pytest tests/integration -v -m integration
```

---

## 🐳 Docker

```bash
docker compose up --build -d
```

---

## 📄 Лицензия

Лицензия Shamanchi 1.0 (source-available) — см. [LICENSE](LICENSE).
---

## 📞 Контакты

- Telegram: @PavelYrevichh
- Email: Lietman46@mail.ru
- GitHub: Shamanchi
- FL.ru: https://www.fl.ru/users/Shamanchi