# Copilot Instructions for AI Coding Agents

## Project Overview
This codebase demonstrates advanced FastAPI concepts, focusing on middleware, authentication, and dependency injection. Each file is a self-contained example of a specific FastAPI feature or pattern. The project is organized for learning and experimentation, not as a monolithic application.

## Key Components & Patterns
- **Middleware Examples:**
  - `cors-middleware.py`, `gzip-middleware.py`, `https-middleware.py`, `custom-middleware.py` each show how to add and configure different FastAPI/Starlette middlewares. Each file creates its own `FastAPI` app instance.
  - Custom middleware (`custom-middleware.py`) uses `BaseHTTPMiddleware` for timing requests. Note: There is a typo in `time.timer` (should be `time.time()`).
- **Authentication:**
  - `user-auth.py` demonstrates OAuth2 password flow with a hardcoded user and token validation logic.
  - `jwt-auth/auth.py` provides JWT token creation and (incomplete) verification using `authlib`. The secret and algorithm are hardcoded for demo purposes.
- **Dependency Injection:**
  - `database-connection-depends.py` shows how to use FastAPI's `Depends` for managing a mock database connection lifecycle.

## Developer Workflows
- **Running Examples:**
  - Each `.py` file is intended to be run independently (e.g., `uvicorn cors-middleware:app`).
  - No central entrypoint or unified app runner.
- **Testing:**
  - No automated tests are present. Manual testing via HTTP requests (e.g., with curl or Postman) is expected.
- **Dependencies:**
  - Core: `fastapi`, `starlette`, `authlib` (for JWT demo)
  - Install with: `pip install fastapi[all] authlib`

## Project Conventions
- Each file is a minimal, focused example. Avoid cross-file imports except for the `jwt-auth` subdirectory.
- Use clear, descriptive endpoint paths and comments to indicate purpose.
- Hardcoded secrets and credentials are for demonstration only—do not use in production.
- All apps use the default FastAPI/Starlette middleware APIs.

## Integration Points
- JWT authentication uses `authlib` for token handling.
- OAuth2 flow in `user-auth.py` is compatible with standard OAuth2 clients.

## Notable Files & Directories
- `cors-middleware.py`, `gzip-middleware.py`, `https-middleware.py`, `custom-middleware.py`: Middleware patterns
- `user-auth.py`: OAuth2 authentication example
- `jwt-auth/auth.py`: JWT authentication logic
- `database-connection-depends.py`: Dependency injection for DB connections

## Example: Running a Middleware Demo
```sh
uvicorn cors-middleware:app --reload
```

## Example: Generating a JWT Token
- Use the `/token` endpoint in `user-auth.py` to get a token, or call `create_access_token` in `jwt-auth/auth.py`.

---

**For AI agents:**
- When adding new examples, follow the single-file, focused-demo pattern.
- Reference this file for project structure and conventions.
- If implementing tests, place them in a new `tests/` directory and use `pytest`.
