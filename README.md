# Recommendation System

## Overview
This project implements a recommendation system using Flask and Docker. It consists of two services: a Generator service and an Invoker service. 
The Invoker service handles caching (local and Redis) and aggregates results from multiple calls to the Generator service.

## Architecture
- **Generator Service:** Generates a random number based on model name and viewer ID.
- **Invoker Service:** Manages caching (local and Redis) and aggregates results from multiple calls to the Generator service.
- **Redis:** Used for distributed caching.

## Setup Instructionsgit

### Prerequisites
- Docker


### Building and Running the Services

Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```


### Usage 

We can use the following command to start the service:
```docker-compose up --build```


Call example:

```curl -X POST http://localhost:5001/recommend \
-H "Content-Type: application/json" \
-d '{"model_name": "example_model", "viewerid": "12345"}'
```


