# simple_test_app.py
from flask import Flask
import sys
import os

# --- 1. Create the Flask application instance ---
# '__name__' helps Flask find resources like templates (though we don't use them here)
app = Flask(__name__)
print(f"Simple Flask app '{app.name}' created (PID: {os.getpid()}).")

# --- 2. Define a simple route ---
# This function will handle requests to the root URL (e.g., http://127.0.0.1:5000/)
@app.route('/')
def index():
    """Handles requests to the root '/'."""
    print(f"  -> Request received for '/' route!") # Log to terminal when accessed
    # Return a plain text message to the browser
    return "Success! Your simple Flask test app is running."

# --- 3. Define another test route ---
@app.route('/ping')
def ping():
    """Handles requests to the '/ping' URL."""
    print(f"  -> Request received for '/ping' route!") # Log to terminal
    return "Pong!"

print("Routes '/' and '/ping' defined.")

# --- 4. Main execution block ---
# This code runs only when the script is executed directly (not imported)
if __name__ == '__main__':
    HOST = "127.0.0.1"  # Standard localhost address
    PORT = 5000         # Standard Flask development port (change if needed)

    print("\n--- Starting Simple Flask Test Server ---")
    print(f"Attempting to run on: http://{HOST}:{PORT}")
    print("Press CTRL+C to stop the server.")

    try:
        # Run the Flask development server:
        # host=HOST:       Makes it listen only on the local machine interface.
        # port=PORT:       Specifies the port number.
        # debug=True:      Enables debugging features (like error pages, auto-reload *if* reloader is on).
        # use_reloader=False: Explicitly disable the auto-reloader initially to avoid confusion.
        #                   If this basic test works, you can try setting it to True later.
        app.run(host=HOST, port=PORT, debug=True, use_reloader=False)

    except OSError as e:
        # Catch common errors like "Address already in use"
        print(f"\nFATAL ERROR: Could not start server on port {PORT}: {e}", file=sys.stderr)
        print("Please check if another application is already using this port.", file=sys.stderr)
        sys.exit(1) # Exit with an error code
    except Exception as e:
        # Catch any other unexpected errors during startup
        print(f"\nFATAL ERROR: An unexpected error occurred during server startup: {e}", file=sys.stderr)
        sys.exit(1) # Exit with an error code

    # This line will only be reached if the server is stopped gracefully (e.g., Ctrl+C)
    print("\n--- Simple Flask Test Server has been stopped. ---")