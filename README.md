# Pinterest Data Pipeline

## Table of Contents
- Project Brief
- Project Data
- Project Tools
- Milestone 3

## Project Brief
Build the system that Pinterest uses to analyse both historical, and real-time data generated by post from their users.

Pinterest has world-class machine learning engineering systems. They have billioons of user interactions such as image uploads or image clicks which they need to process every day to inform the decisions to make. In this project, I am building a system in the cloud that takes in those events and runs them throught two separate pipelines. One for computing real-time metrics such as profile popularity, which would be used to recommend that profile in real-time. Another is for computing metrics that depend on historical data such as the most popular category this year.

## Milestone 3: Configure the EC2 Kafka Client
Goals: 
- Connect EC2 instance with SSH
- Create 3 topics with MSK

Tasks:
- Creating a .pem key
- Connecting to EC2
- Set up Kafka in EC2 instance
- Creating Kafka Topics

## Milestone 4: Connect a MSK cluster to a S3 bucket
Goal:
- Use MSK Connect to connect the MSK cluster to a S3 bucket, such that any data going through the cluster will be automatically saved and stored in a dedicated S3 bucket.

Tasks:
- Creating a custom plugin with MSK Connect
- Creating a connector with MSK Connect

## Configuring an API Gateway
Goals: To build our own API that send data to the MSK cluter, which in turn will be stored in an S3 bucket.

## Milestone 5:

## Milestone 6: