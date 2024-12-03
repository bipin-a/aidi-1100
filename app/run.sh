#!/bin/bash

# path_to_your_main:app 
uvicorn app.main:app --host 'localhost' --port 8000 --reload

# This is using uvicorn 
# Most people use Docker to run their FastAPI applications