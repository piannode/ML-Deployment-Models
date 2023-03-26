import os
import io
import boto3
import json
import csv

# grab environment variables
ENDPOINT_NAME = os.env