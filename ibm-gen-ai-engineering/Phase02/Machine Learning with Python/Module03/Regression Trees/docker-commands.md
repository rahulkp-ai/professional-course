1. Build and Start the Application (Detached Mode)

   ```Bash
   docker compose up -d --build
   The -d flag runs it in the background (detached), and --build ensures any code changes in app.py or index.html trigger a fresh image build.

   ```

2. View Live Server Logs

   ```Bash
   docker compose logs -f
   Use Ctrl + C to exit log viewing (the container keeps running).

   ```

3. Check Container Status
   ```Bash
   docker compose ps
   ```
4. Stop the Container
   ```Bash
   docker compose stop
   ```
5. Stop and Remove Containers, Networks & Volumes
   ```Bash
   docker compose down
   ```
