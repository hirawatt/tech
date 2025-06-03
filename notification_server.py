# /Users/vh/Desktop/work/MyCode/myGithub/tech/notification_server.py
import asyncio
import websockets
import json
import time
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

connected_clients = set()

async def register(websocket):
    """Registers a new client connection."""
    connected_clients.add(websocket)
    logging.info(f"Client {websocket.remote_address} connected. Total clients: {len(connected_clients)}")
    try:
        # Send a welcome notification upon connection
        welcome_message = {
            "title": "HirawatTech Backend",
            "body": "Successfully connected for real-time notifications!",
            "icon": "/assets/hirawat-tech-500-logo.webp" # Optional: specify an icon
        }
        await websocket.send(json.dumps(welcome_message))
    except websockets.exceptions.ConnectionClosed:
        # Client might have disconnected immediately after connecting
        logging.warning(f"Could not send welcome message to {websocket.remote_address}, connection closed.")
        pass # Unregister will handle removal

async def unregister(websocket):
    """Unregisters a client connection."""
    connected_clients.discard(websocket) # Use discard to avoid KeyError if already removed
    logging.info(f"Client {websocket.remote_address} disconnected. Total clients: {len(connected_clients)}")

async def send_to_all_clients(message_data):
    """Sends a JSON message to all connected clients."""
    if connected_clients:
        message_str = json.dumps(message_data)
        # Create a list of tasks for sending messages
        # Iterate over a copy of the set in case it's modified during iteration (e.g., by unregister)
        tasks = [client.send(message_str) for client in list(connected_clients)]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for client, result in zip(list(connected_clients), results): # Ensure client list matches results
            if isinstance(result, Exception):
                logging.error(f"Error sending to client {client.remote_address}: {result}. Removing client.")
                # If sending failed, assume client is disconnected and unregister
                await unregister(client) # Ensure unregister is called if send fails

async def connection_handler(websocket, path):
    """Handles individual client WebSocket connections."""
    await register(websocket)
    try:
        # Keep the connection alive and listen for messages from the client (optional)
        async for message in websocket:
            logging.info(f"Received message from {websocket.remote_address}: {message}")
            # Example: Process incoming messages if your application needs two-way communication
            # For now, we primarily focus on server-to-client notifications
            # await websocket.send(f"Server acknowledges: {message}")
            pass
    except websockets.exceptions.ConnectionClosedOK:
        logging.info(f"Client {websocket.remote_address} closed connection normally.")
    except websockets.exceptions.ConnectionClosedError as e:
        logging.warning(f"Client {websocket.remote_address} connection closed with error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error with client {websocket.remote_address}: {e}")
    finally:
        await unregister(websocket)

async def periodic_notifier():
    """Periodically sends a sample notification to all connected clients."""
    counter = 0
    while True:
        await asyncio.sleep(20) # Send a notification every 20 seconds
        counter += 1
        current_time = time.strftime("%H:%M:%S")
        notification_data = {
            "title": "Backend Update",
            "body": f"This is sample message #{counter} from the server at {current_time}.",
            "icon": "/assets/hirawat-tech-500-logo.webp" # You can customize this
        }
        logging.info(f"Backend: Sending periodic notification: '{notification_data['body']}'")
        await send_to_all_clients(notification_data)

# This function would be called from your main Python application logic
# when you want to trigger a specific notification.
async def trigger_custom_notification(title: str, body: str, icon: str = None):
    """Function to be called by other parts of your backend to send a notification."""
    if not icon:
        icon = "/assets/hirawat-tech-500-logo.webp"
    notification_data = {
        "title": title,
        "body": body,
        "icon": icon
    }
    logging.info(f"Backend: Triggering custom notification: '{body}'")
    await send_to_all_clients(notification_data)
    return f"Notification '{title}' sent to {len(connected_clients)} clients."


async def main_server_loop():
    # Start the WebSocket server
    # Listen on all available network interfaces on port 8765
    server = await websockets.serve(connection_handler, "0.0.0.0", 8765)
    logging.info("WebSocket server started on ws://0.0.0.0:8765")

    # Start the periodic notifier task for demonstration
    asyncio.create_task(periodic_notifier())

    # Example: How you might trigger a notification from elsewhere after a delay
    # await asyncio.sleep(10)
    # await trigger_custom_notification("Special Alert!", "A critical event just occurred.")

    # Keep the server running indefinitely
    await server.wait_closed()

if __name__ == "__main__":
    try:
        asyncio.run(main_server_loop())
    except KeyboardInterrupt:
        logging.info("WebSocket server shutting down...")
    except Exception as e:
        logging.critical(f"WebSocket server failed to start or run: {e}")

