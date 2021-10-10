
## Kubernetes Basics
===================================================================================================
## What is Kubernetes?

Kubernetes is a container management system developed on the Google platform. Kubernetes helps to manage containerised applications in various types of physical, virtual, and cloud environments. Google Kubernetes is a highly flexible container tool to consistently deliver complex applications running on clusters of hundreds to thousands of individual servers.

This is a walkthrough of the basics of the Kubernetes cluster orchestration system.

Deploy a containerized application on a cluster.
Scale the deployment.
Update the containerized application with a new software version.
Debug the containerized application.

## What can Kubernetes do for you?

With modern web services, users expect applications to be available 24/7, and developers expect to deploy new versions of those applications several times a day. Containerization helps package software to serve these goals, enabling applications to be released and updated without downtime. Kubernetes helps you make sure those containerized applications run where and when you want, and helps them find the resources and tools they need to work. Kubernetes is a production-ready, open source platform designed with Google's accumulated experience in container orchestration, combined with best-of-breed ideas from the community.

=======================================================================================

## Project Overview
 
This project is all about how to perform a rolling out Deployment on EKS kubernetes Cluster.
========================================================================================

### Project Tasks

Your project goal is to operationalize this working,  rolliout out an appliction using [kubernetes](https://kubernetes.io/), which is an open-source system for automating the management of containerized applications. In this project you will:

* Test your project code using linting
* Complete a Dockerfile to containerize this application
* Deploy your containerized application using Docker 
* Configure Kubernetes and create a Kubernetes cluster (AWS EKS)
* Deploy a container using Kubernetes 
* perform a rollout deployment
* Upload a complete Github repo with CircleCI to indicate that your code has been tested

===================================================================

## Setup the Environment
* clone git repo https://github.com/cloudarchitectaws/CAPSTONE-PROJECT
* Create a virtualenv and activate it
* Run `make install` to install the necessary dependencies
* Run make lint to test the dokcerfile and app.py file
#test1234
====================================================================

