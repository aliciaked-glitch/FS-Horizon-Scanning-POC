FS Horizon clean starter with source drill-down and feedback

What is new
- Thumbs up / thumbs down feedback buttons on each issue card
- POST /api/feedback endpoint on the backend
- Click-through detail panel for each issue
- Source provenance, source type and credibility shown on demand

Deploy steps
1. Deploy backend_clean to Railway
   - Root Directory: backend_clean
   - Builder: Dockerfile
   - Healthcheck Path: /health

2. Test backend URLs
   - /health
   - /api/dashboard
   - /api/feedback (POST only, used by the app)

3. Deploy frontend_clean to Vercel
   - Root Directory: frontend_clean

4. Replace API_BASE in frontend_clean/index.html with your Railway URL
   and redeploy Vercel.

Notes
- The feedback endpoint currently stores votes in memory for a simple starter setup.
- Feedback will reset when the backend restarts unless you later add a database.
- For stronger CORS security, replace allow_origins=["*"] with your Vercel domain.
