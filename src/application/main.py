import uvicorn
from application.adapters.http.http_get_compliment import app
from common.config.infrastructure.instance import config

def main() -> int:
    app_host: str = config.get_or_throw("APP_HOST", str)
    app_port: int = config.get_or_throw("APP_PORT", int)

    uvicorn.run(app, host = app_host, port = app_port)

    return 0

if __name__ == "__main__":
    main()