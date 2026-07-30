$ErrorActionPreference = "Stop"

Write-Host "[1/4] Validating Docker Compose..."
docker compose config | Out-Null

Write-Host "[2/4] Building and starting services..."
docker compose up --build --detach --wait --wait-timeout 180

try {
    Write-Host "[3/4] Running complete runtime smoke test..."
    python scripts/runtime_smoke.py

    Write-Host "[4/4] Application is running."
    Write-Host "Mini App: http://localhost:8080"
    Write-Host "Backend:  http://localhost:8000"
    Write-Host "Swagger:  http://localhost:8000/docs"
    Write-Host "Evidence: runtime-smoke-local.json"
}
catch {
    Write-Host "Runtime verification failed. Container logs follow:" -ForegroundColor Red
    docker compose ps
    docker compose logs --no-color
    throw
}
