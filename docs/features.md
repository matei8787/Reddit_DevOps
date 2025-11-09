# Features
- F1 — Autentificare (JWT): înregistrare, login, refresh token
- F2 — Bug CRUD: creare, listare, detaliu, filtrare 
- F3 — Voting: upvote / downvote, score calculat
- F4 — Logging: fișiere separate pentru auth, bugs, system
- F5 — Rate limiting: protecție la brute-force și spam
- F6 — Frontend: template-uri Django + JS pentru UX (formular, butoane)
- F7 — DevOps plan: Docker, Nginx, Kubernetes (local), GitHub Actions CI/CD

# User Stories
- US-001 (P1) — Ca user, vreau să mă înregistrez ca să pot raporta bug-uri.
- US-002 (P1) — Ca user autenticat, vreau să raportez un bug cu titlu și descriere.
- US-003 (P1) — Ca user autenticat, vreau să votez un bug (up/down) pentru prioritizare.
- US-004 (P2) — Ca admin, vreau loguri de autentificare pentru audit.
- US-005 (P2) — Ca sistem, trebuie să previn brute-force pe endpoint-ul de login.
- US-006 (P2) — Ca DevOps, vreau pipeline CI care rulează testele și scanările de securitate.