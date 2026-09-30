# System Architecture

```text
                  ┌──────────────────────┐
                  │       User           │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ React Frontend       │
                  │ Vite + CSS           │
                  └──────────┬───────────┘
                             │ HTTP/REST
                             ▼
                  ┌──────────────────────┐
                  │ Express.js Backend   │
                  │ Movie REST API       │
                  └──────────┬───────────┘
                             │
             ┌───────────────┴───────────────┐
             ▼                               ▼
    ┌─────────────────┐             ┌──────────────────┐
    │ movies.csv      │             │ Recommendation   │
    │ Movie Dataset   │             │ Engine           │
    └─────────────────┘             └────────┬─────────┘
                                             │
                                      TF-IDF vectors
                                             │
                                      Cosine similarity
                                             │
                                             ▼
                                    Top-N recommendations
```
