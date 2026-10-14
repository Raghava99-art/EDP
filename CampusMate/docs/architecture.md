# Architecture

```text
React + Vite UI
      |
      | HTTP / JSON
      v
FastAPI routes
      |
      v
Answer service
      |
      v
Semantic search engine ---- FAQ CSV
      |
      v
Ranked answer + similarity score
      |
      v
Chat UI and feedback endpoint
```

The search engine embeds each FAQ question/category/answer once when initialized. Each user question is embedded and compared with FAQ vectors using cosine similarity. The best matching FAQ is returned only when its score clears the configurable threshold.
