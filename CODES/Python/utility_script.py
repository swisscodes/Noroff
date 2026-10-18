def health_check(service): #type:ignore
    """Evaluates the operational health status of a service based on its HTTP status code and response latency.
        Parameters: service (dict): Dictionary containing service metadata (service_name, status_code, response_time_ms).
        Returns: str: Operational state ("Healthy", "Degraded", or "Critical"). 
    """
    # Check if HTTP status code indicates a successful request (200 OK)
    if service["status_code"] == 200:
        # Evaluate performance against latency threshold (300ms)
        if service["response_time_ms"] < 300:
            return "Healthy"
        else:
            return "Degraded"
    else:
        # Any non-200 HTTP status code triggers a Critical state
        return "Critical"
    
    #  Service Definitions
    
services = [ #type:ignore
    {"service_name": "auth-service", "status_code": 200, "response_time_ms": 145}, 
    { "service_name": "payment-service", "status_code": 200, "response_time_ms": 320, }, 
    {"service_name": "inventory-api", "status_code": 503, "response_time_ms": 800}, 
    {"service_name": "notification-svc", "status_code": 200, "response_time_ms": 78}, 
    {"service_name": "reporting-api", "status_code": 404, "response_time_ms": 210}, 
]

# --- Main Execution Loop & Summary --- 
if __name__ == "__main__": 
    # Initialize state counters
    health_summary = {"Healthy": 0, "Degraded": 0, "Critical": 0} 
    print("=== Deployment Health Check ===") 
    # Process each service, update summary counters, and print formatted status 
    for service in services: #type:ignore
        status = health_check(service) 
        health_summary[status] += 1 
        name = service["service_name"] #type:ignore
        code = service["status_code"] #type:ignore
        time = service["response_time_ms"] #type:ignore
        print(f"{name}: {status} ({code}, {time}ms)") 
    # Print final aggregated summary 
    print("\n=== Health Check Summary ===") 
    print(f"Healthy: {health_summary['Healthy']}") 
    print(f"Degraded: {health_summary['Degraded']}") 
    print(f"Critical: {health_summary['Critical']}") 