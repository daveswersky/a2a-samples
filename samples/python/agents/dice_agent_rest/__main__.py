import os
import uvicorn
from google.adk.cli.fast_api import get_fast_api_app

# The ADK will automatically discover the 'root_agent' in 'agent.py'
# in the same directory.

if __name__ == "__main__":
    # Get the FastAPI app using the standard ADK helper
    app = get_fast_api_app(
        agents_dir=os.path.dirname(os.path.abspath(__file__)),
        session_service_uri="sqlite:///:memory:", # Use in-memory SQLite DB
        allow_origins=["*"], # Allow all origins for development
        web=False,
    )

    # The port will be passed in by the Agent Gallery runner.
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)