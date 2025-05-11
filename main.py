#!/usr/bin/env python3
import requests
import json
import os
from datetime import datetime
from sql_solver import solve_sql_problem

def main():
    print("Starting Bajaj Finserv Health Qualifier Application...")
    
    name = "Jyotirjay Narayan Gupta "
    reg_no = "0827CD221039"
    email = "jyotirjaynarayan220749@acropolis.in"
    
    webhook_data = generate_webhook(name, reg_no, email)
    
    if webhook_data:
        print(f"Webhook generated successfully: {webhook_data['webhook']}")
        
        last_digit = int(reg_no[-1])
        problem_number = 1 if last_digit % 2 != 0 else 2
        print(f"Based on registration number {reg_no}, solving problem {problem_number}")
        
        sql_query = solve_sql_problem(problem_number)
        print(f"SQL problem solved. Query generated.")
        
        submit_result = submit_solution(webhook_data['webhook'], webhook_data['accessToken'], sql_query)
        
        if submit_result:
            print("Solution submitted successfully!")
        else:
            print("Failed to submit solution.")
    else:
        print("Failed to generate webhook.")

def generate_webhook(name, reg_no, email):
    url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    payload = {
        "name": name,
        "regNo": reg_no,
        "email": email
    }
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error generating webhook: {e}")
        return None

def submit_solution(webhook_url, access_token, sql_query):
    payload = {
        "finalQuery": sql_query
    }
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(webhook_url, json=payload, headers=headers)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error submitting solution: {e}")
        return False

if __name__ == "__main__":
    main()