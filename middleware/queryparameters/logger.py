from fastapi import FastAPI, Request
# import time

class QueryParamLoggerMiddleware:
    def __init__(self, app: FastAPI):
        self.app = app

    async def __call__(self, scope, receive, send):
        # Create a new request object from the scope
        request = Request(scope, receive=receive)

        # Log request method, path, and query string
        log_message = f"Incoming request - {request.method} {request.url.path}"
        if request.url.query:
            log_message += f"?{request.url.query}"
        print(log_message)

        # Log request headers
        print("\nRequest Headers:")
        for key, value in request.headers.items():
            print(f"\t{key}: {value}")

        # # Measure execution time
        # start_time = time.time()

        # Call the next middleware or route handler
        response = await self.app(scope, receive, send)

        # # Calculate execution time
        # end_time = time.time()
        # execution_time = end_time - start_time

        # # Log execution time
        # print(f"Execution Time: {execution_time} seconds")

        return response