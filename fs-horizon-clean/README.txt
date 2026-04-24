FS Horizon clean starter

1. Deploy backend_clean to Railway
   - Root Directory: backend_clean
   - Builder: Dockerfile
   - Healthcheck Path: /health

2. Test backend URLs
   - /health
   - /api/dashboard

3. Deploy frontend_clean to Vercel
   - Root Directory: frontend_clean

4. Replace API_BASE in frontend_clean/index.html with your Railway URL
   and redeploy Vercel.
