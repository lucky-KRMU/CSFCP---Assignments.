#!/bin/bash

echo "Creating Career Planning Folder Structure..."

mkdir -p Career/Certificates
mkdir -p Career/Projects
mkdir -p Career/Resumes
mkdir -p Career/Hackathons
mkdir -p Career/Notes

echo "Folders created successfully!"

echo "Saving system uptime to a file..."
uptime > Career/system_uptime.txt

echo "All tasks completed!"
