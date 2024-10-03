import logging

logging.basicConfig(level=logging.INFO)


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log method, path, and additional details
        logging.info(f"Request: {request.method} {request.path} {request.headers}")
        
        # If you want to log query parameters
        logging.info(f"Query Params: {request.GET}")

        # If you want to log the body (for POST or PUT requests)
        if request.method in ['POST', 'PUT', 'PATCH']:
            logging.info(f"Request Body: {request.body}")
            
        # If you want to log the authenticated user (if any)
        if request.user.is_authenticated:
            logging.info(f"User: {request.user}")

        # Get the response
        response = self.get_response(request)

        # Log response status
        logging.info(f"Response: {response.status_code}")
        return response
