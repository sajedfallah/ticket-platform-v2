import httpx

from config import API_BASE_URL


class TicketAPIClient:
    def __init__(self):
        self.base_url = API_BASE_URL

    async def get_events(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/api/events")
            return response.json()

    async def create_order(self, payload):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/api/orders/create",
                json=payload
            )
            return response.json()
